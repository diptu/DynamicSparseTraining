# Kernel-Native, Score-Free KV Cache Compression — Experiment Design

**Status:** Draft v1 · **Owner:** Nazmul Alam · **Scope:** long-context autoregressive inference

---

## 1. Summary

Nearly every strong KV-cache eviction method (H2O, SnapKV, Ada-KV) ranks tokens by the attention *scores* they receive. But FlashAttention computes attention with a tiled online-softmax and **never materializes the N×N score matrix** — it only emits the per-query log-sum-exp (the softmax denominator). So score-based methods must fall back to a slow, materialized-attention path to get the signal they need, forfeiting the very kernel that makes long context affordable.

This experiment asks: **can token importance be estimated from quantities that are cheap and available without the score matrix, closely enough to match score-based eviction quality while keeping FlashAttention?** If yes, the accuracy-per-wall-clock frontier moves, because we no longer have to choose between *fast-but-dumb* (StreamingLLM) and *smart-but-slow* (H2O).

The deliverable is a PyTorch harness that (a) implements a family of **score-free importance proxies**, (b) implements score-based and position-only **baselines**, and (c) measures both quality-at-budget **and** end-to-end latency/memory so the kernel-compatibility advantage is actually counted.

---

## 2. Background and the specific gap

Standard per-key importance for a key at position `j` is the total attention mass it receives across all query positions:

```
imp(j) = Σ_i  softmax_j( q_i · k_j / √d )
```

Computing this exactly requires the full score matrix `S ∈ R^{N×N}` — the object FlashAttention deliberately never forms. What FlashAttention *does* return cheaply:

- per-query log-sum-exp `lse_i` (the softmax denominator), and
- anything you can compute from `K`, `V`, `Q` directly without their pairwise product (norms, projections onto a few fixed directions).

So the design constraint is precise:

> An importance signal is **kernel-native** iff it can be computed without materializing `S` (or any O(N²) intermediate), ideally fused into or run alongside the attention kernel in O(N·d) or O(r·N·d) with `r ≪ N`.

Note that **StreamingLLM is already kernel-native** — "keep the first few sink tokens plus a recent window" needs no scores at all. It is therefore the honest baseline to beat, not full attention. The open question is whether *content-aware* score-free signals beat *position-only* StreamingLLM and approach *score-based* H2O.

---

## 3. Research questions and hypotheses

- **RQ1 (quality).** How much of the quality gap between StreamingLLM (position-only, kernel-native) and H2O (score-based, kernel-incompatible) can score-free content proxies recover at a fixed cache budget?
- **RQ2 (efficiency).** What is the true end-to-end cost of the score-based methods once you account for leaving the fast kernel, and how much of that does the proxy approach save?
- **RQ3 (composition).** Which cheap signals matter — key norm, value norm, or a low-rank query-probe sketch — and do they compose?

**H1.** A low-rank query-probe sketch (below) recovers ≥70% of the StreamingLLM→H2O quality gap on LongBench at a 20–50% cache budget.

**H2.** At matched quality, the proxy method delivers strictly higher tokens/sec and lower peak memory than H2O because it retains FlashAttention throughout.

**H3.** Norms alone (‖k‖, ‖v‖) are weak; the probe sketch is what closes most of the gap.

Each hypothesis has a pre-registered success threshold so the result is interpretable even if negative.

---

## 4. Method: score-free importance proxies

Four proxy families, from cheapest to most expressive. All are computed **per KV head** (respecting GQA grouping) and never touch an O(N²) object.

**(P0) Position prior — StreamingLLM.** Keep `s` sink tokens + a recent window of size `w`. Free. This is the kernel-native reference, not our contribution; it is the score-free control.

**(P1) Key/value norms.** `imp(j) = ‖k_j‖` or `‖v_j‖` or their product. O(N·d), trivially fused. Rationale: a large-norm key can dominate dot products; a large-norm value contributes more to the output when attended. Expected to be weak alone (H3) but a useful ablation floor.

**(P2) Low-rank query-probe sketch (primary contribution).** Approximate the column-sum of `S` using `r ≪ N` representative "probe" queries instead of all N real queries. Precompute, per layer/head, a small set of probes `P = {p_1..p_r}` from a calibration corpus (top-r PCA components of observed queries, or k-means centroids). Then:

```
a_mj  = softmax over j of ( p_m · k_j / √d )      # r independent softmaxes over keys
imp(j) = Σ_m  α_m · a_mj                            # α_m optional PCA-eigenvalue weights
```

Cost is O(r·N·d) with `r` in ~8–32, and it needs neither the real queries at decode time nor the N×N matrix. It is a rank-`r` sketch of the true importance column-sum.

**(P3) Sketch + position prior (composed).** Force-keep sinks + recent window, rank the *rest* by P2. This is the intended production form; sinks and recency are cheap and known to be high-value, so spending the sketch budget on the ambiguous middle is the right allocation.

**Kernel-compatibility argument.** P1–P3 are all O(N·d) or O(r·N·d) and depend only on `K`, `V`, and fixed probes — no query-key score matrix. In a prototype they run as a cheap **second pass** alongside standard FlashAttention (attention output is computed normally; the proxy is computed separately and used only to decide eviction). A production version fuses the probe dot-products into the prefill kernel. The prototype already validates the science; fusion is an engineering follow-up and is explicitly out of scope for v1.

---

## 5. Baselines

A clean ladder from lower bound to upper bound, so any result is anchored on both sides:

| Tier | Method | Score-based? | Kernel-native? | Role |
|---|---|---|---|---|
| Floor | Random eviction | no | yes | sanity lower bound |
| Position-only | **StreamingLLM** (sink + window) | no | **yes** | the control to beat |
| Ours (norms) | P1 key/value norm | no | yes | ablation |
| **Ours** | **P2/P3 probe sketch** | **no** | **yes** | the proposed method |
| Score ceiling | **H2O** (heavy-hitters) | **yes** | **no** | quality target |
| Score ceiling | SnapKV | yes | no | quality target (prompt-aware) |
| Absolute ceiling | Full cache (no eviction) | — | yes | upper bound |

The two comparisons that carry the paper: **P3 vs StreamingLLM** (does content help over position alone, kernel-native to kernel-native?) and **P3 vs H2O** (how close to the score-based ceiling, and at what latency?).

---

## 6. Experimental setup

**Models.** Start with one 7–8B long-context model (e.g., Llama-3.1-8B-Instruct or Qwen2.5-7B-Instruct, 128K context). Add a second model family before publishing to show the effect isn't model-specific. Use a ~1.5B model for fast iteration during development.

**Datasets / tasks.**
- **LongBench** (multi-doc QA, summarization, few-shot, code) — primary quality suite.
- **Needle-in-a-Haystack (NIAH)** across depths × context lengths — retrieval stress test; eviction methods often fail here, so it's diagnostic.
- **RULER** — harder synthetic long-context, less saturated than NIAH.
- **Perplexity** on held-out long documents (PG-19 / a code corpus) — cheap smoke test during development.

**Cache budgets.** Sweep retained fraction `{5, 10, 20, 30, 50}%` of full cache. The interesting regime is 10–30%.

**Hardware.** Single A100/H100 80GB. Fix batch size, dtype (bf16), and sequence lengths across all methods; log the exact kernel path each method takes.

---

## 7. Metrics

**Quality.** Task score per LongBench subtask; NIAH/RULER accuracy heatmap over (depth, length); perplexity. Always reported **at matched budget**.

**Efficiency (the part most eviction papers under-report).**
- Prefill latency and decode latency (ms/token).
- Peak GPU memory and KV-cache bytes.
- Tokens/sec end-to-end.
- **Kernel path flag**: did the method run FlashAttention, or did it fall back to materialized attention? Report the throughput penalty of falling back explicitly — this is the whole thesis.

**The headline plot.** Quality (y) vs tokens/sec (x), one point per method per budget. The claim succeeds iff the proxy method sits **up-and-to-the-right** of both StreamingLLM and H2O — i.e., it dominates the accuracy/throughput frontier.

---

## 8. Implementation plan (PyTorch)

Built on HuggingFace `transformers`, whose `Cache` API is the natural extension point (models accept `past_key_values=<Cache>`; a `Cache` implements `update(...)` and can evict). HF ships `SinkCache` (StreamingLLM) and `DynamicCache` (full cache) — two baselines for free.

### 8.1 Environment

```bash
pip install "torch>=2.4" transformers accelerate datasets flash-attn --break-system-packages
# load models with attn_implementation="flash_attention_2"
```

### 8.2 Core abstraction: a proxy-eviction cache

```python
# score_free_cache.py
import torch
from transformers.cache_utils import DynamicCache

class ScoreFreeEvictCache(DynamicCache):
    """
    KV cache that evicts down to `budget` tokens per layer using a *score-free*
    importance proxy. Never materializes an N×N attention matrix.

    proxy: one of {"random", "knorm", "vnorm", "kvnorm", "sketch"}
    sinks / recent: always-kept sink prefix and recent window (StreamingLLM prior)
    probes: dict[layer_idx] -> Tensor[num_kv_heads, r, head_dim]  (for "sketch")
    """
    def __init__(self, budget, proxy="sketch", sinks=4, recent=64, probes=None):
        super().__init__()
        self.budget = budget
        self.proxy = proxy
        self.sinks = sinks
        self.recent = recent
        self.probes = probes or {}

    def _importance(self, layer_idx, k, v):
        # k, v: [B, H_kv, T, D]
        if self.proxy == "random":
            return torch.rand(k.shape[:3], device=k.device)   # [B,H,T]
        if self.proxy == "knorm":
            return k.norm(dim=-1)
        if self.proxy == "vnorm":
            return v.norm(dim=-1)
        if self.proxy == "kvnorm":
            return k.norm(dim=-1) * v.norm(dim=-1)
        if self.proxy == "sketch":
            P = self.probes[layer_idx].to(k.dtype)            # [H_kv, r, D]
            d = k.shape[-1] ** 0.5
            # scores: [B,H,r,T] = probes · keys
            s = torch.einsum("hrd,bhtd->bhrt", P, k) / d
            a = torch.softmax(s, dim=-1)                       # softmax over keys T
            return a.sum(dim=2)                                # Σ_r  -> [B,H,T]
        raise ValueError(self.proxy)

    def _evict(self, layer_idx):
        k = self.key_cache[layer_idx]      # [B,H,T,D]
        v = self.value_cache[layer_idx]
        B, H, T, D = k.shape
        if T <= self.budget:
            return
        imp = self._importance(layer_idx, k, v)               # [B,H,T]
        # force-keep sinks + recent window (StreamingLLM prior)
        imp[..., : self.sinks] = float("inf")
        imp[..., T - self.recent :] = float("inf")
        keep = imp.topk(self.budget, dim=-1).indices          # [B,H,budget]
        keep, _ = keep.sort(dim=-1)                            # preserve order
        idx = keep.unsqueeze(-1).expand(-1, -1, -1, D)
        self.key_cache[layer_idx]   = k.gather(2, idx)
        self.value_cache[layer_idx] = v.gather(2, idx)

    def update(self, key_states, value_states, layer_idx, cache_kwargs=None):
        k, v = super().update(key_states, value_states, layer_idx, cache_kwargs)
        self._evict(layer_idx)
        return self.key_cache[layer_idx], self.value_cache[layer_idx]
```

> Note: real per-head eviction with GQA needs per-head index bookkeeping so all heads in the cache stay length-aligned; the simplest correct v1 evicts on the **mean importance across heads** (single shared keep-set per layer). Start there; add head-independent eviction as an ablation.

### 8.3 Building probes from calibration

```python
# build_probes.py — collect queries per layer/head, take top-r PCA directions
import torch

@torch.no_grad()
def collect_queries(model, tokenizer, texts, layers, max_len=4096):
    buf = {l: [] for l in layers}
    hooks = []
    def mk(l):
        def hook(mod, inp, out):
            # out or a projected q; capture q_proj output, reshape to [*, H, D]
            buf[l].append(out.detach().float().cpu())
        return hook
    for l in layers:
        hooks.append(model.model.layers[l].self_attn.q_proj.register_forward_hook(mk(l)))
    for t in texts:
        ids = tokenizer(t, return_tensors="pt", truncation=True,
                        max_length=max_len).input_ids.to(model.device)
        model(ids)
    for h in hooks: h.remove()
    return {l: torch.cat(v, 0) for l, v in buf.items()}   # [tokens, H*D] per layer

def pca_probes(Q, num_kv_heads, head_dim, r=16):
    # Q: [N, H*D] -> per-head top-r right singular vectors -> [H_kv, r, D]
    H = Q.shape[1] // head_dim
    Q = Q.view(-1, H, head_dim)
    probes = []
    for h in range(H):
        Xc = Q[:, h] - Q[:, h].mean(0, keepdim=True)
        _, _, Vh = torch.linalg.svd(Xc, full_matrices=False)
        probes.append(Vh[:r])                              # [r, D]
    probes = torch.stack(probes)                           # [H, r, D]
    # map query heads -> kv heads for GQA (group-mean) if H != num_kv_heads
    if H != num_kv_heads:
        g = H // num_kv_heads
        probes = probes.view(num_kv_heads, g, r, head_dim).mean(1)
    return probes                                          # [H_kv, r, D]
```

### 8.4 Baselines

- **Full cache:** `DynamicCache()` (HF default).
- **StreamingLLM:** HF `SinkCache(window_length=budget, num_sink_tokens=4)`.
- **Random / norms:** `ScoreFreeEvictCache(proxy="random" | "knorm" | ...)`.
- **H2O / SnapKV (score-based ceilings):** these need attention weights, so run them with `attn_implementation="eager"` (materialized scores) and accumulate per-key attention mass to drive eviction. Wrap in their own cache subclass. **Log that they force the eager path** — that penalty is a result, not a nuisance.

### 8.5 Evaluation harness (skeleton)

```python
# run_eval.py
def evaluate(model, tokenizer, task, cache_factory, budget):
    latencies, correct = [], 0
    for ex in task:
        cache = cache_factory(budget)
        ids = tokenizer(ex["prompt"], return_tensors="pt").input_ids.to(model.device)
        torch.cuda.synchronize(); t0 = time.time()
        out = model.generate(ids, past_key_values=cache, max_new_tokens=ex["gen_len"],
                             use_cache=True)
        torch.cuda.synchronize(); latencies.append(time.time() - t0)
        correct += task.score(ex, tokenizer.decode(out[0, ids.shape[1]:]))
    return dict(acc=correct/len(task),
                ms_per_tok=1e3*sum(latencies)/total_tokens,
                peak_mem=torch.cuda.max_memory_allocated())
```

Sweep `{method} × {budget} × {task}`; dump to a dataframe; render the quality-vs-throughput frontier plot.

---

## 9. Experimental protocol (phases)

1. **Plumbing.** Full-cache + StreamingLLM + random on the 1.5B model, short contexts, perplexity only. Confirms the cache wiring and eviction don't corrupt generation.
2. **Baselines.** Add H2O/SnapKV (eager path). Confirm they reproduce published quality and **measure their kernel-path throughput penalty**.
3. **Proxies.** Add P1 norms, then P2/P3 sketch + probe calibration. LongBench + NIAH at all budgets.
4. **Frontier.** The quality-vs-throughput plot on the 8B model. Test H1/H2/H3 against thresholds.
5. **Generalize.** Second model family; RULER; head-independent eviction ablation.

Gate: if Phase 2 shows H2O's fallback penalty is negligible on your hardware/kernels, the core motivation weakens — **re-scope before Phase 3** rather than after.

---

## 10. Ablations

- `r ∈ {4, 8, 16, 32}` probes — quality vs sketch cost.
- Probe source: PCA vs k-means vs mean-query vs random directions.
- Norms vs sketch vs (norms + sketch).
- Shared-across-heads vs per-head eviction.
- Sink/recent window sizes.
- Calibration domain shift (calibrate on domain A, test on B).
- Layer-wise budgets (early layers keep more, per PyramidInfer-style intuition).

---

## 11. Expected outcomes and interpretation

- **Success:** P3 lands ≥70% of the way from StreamingLLM to H2O on LongBench at 20–30% budget (H1), while beating H2O on tokens/sec at matched quality (H2). Headline frontier plot dominates.
- **Partial:** P3 beats StreamingLLM but trails H2O substantially — still publishable as "content helps score-free eviction," with an honest quality gap and a throughput win.
- **Negative:** P3 ≈ StreamingLLM. That means position priors already capture what cheap content signals offer, which is itself a clean, useful finding (and points toward needing the actual scores — i.e., the fusion/kernel-modification route, not proxies).

Pre-registering these three readings keeps a null result informative.

---

## 12. Risks and mitigations

- **Proxy just relearns recency.** If P2 without the position prior mostly keeps recent tokens, it adds nothing over StreamingLLM. *Mitigation:* report P2 alone (no sink/recent forcing) to isolate content signal; inspect kept-index distributions.
- **NIAH cliff.** Eviction notoriously drops the needle. *Mitigation:* treat NIAH as a diagnostic, not just a number; analyze at which depth/length the proxy fails and whether the sketch can be biased toward rare high-norm keys.
- **Prototype ≠ fused kernel.** The v1 "second pass" proves quality and *plausible* speed, not the final fused throughput. *Mitigation:* be explicit that fusion is future work; still measure the second-pass overhead so the claim is bounded.
- **H2O fallback penalty is hardware/kernel-dependent.** *Mitigation:* the Phase-2 gate; report the penalty as a measured quantity on your exact stack, not a general claim.
- **Prefill is untouched.** This method compresses the cache, not the O(N²) prefill. *Mitigation:* scope the paper to decode/memory; don't overclaim.

---

## 13. Reference points (position against, not cite verbatim)

H2O (heavy-hitter eviction, NeurIPS 2023), SnapKV (prompt-aware selection), StreamingLLM (attention sinks + window), Ada-KV (adaptive per-head budget), Quest / InfiniGen (query-aware sparse loading), Expected Attention (compression via future-query estimation), FlashAttention-2 (the kernel whose score-hiding motivates this work). Do a fresh arXiv/OpenReview pass before writing — this subfield ships weekly, and score-free eviction under kernel constraints is exactly the kind of idea someone may have just posted.
