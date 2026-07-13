# todo.md — the research spine (2h/day · 3 days/week)

**This is the research task list only.** The application logistics (letters, tests/TOEFL, transcripts,
program portfolio, the Tianlong Chen RA email, submission) live in
[`phd-readiness-20wk.md`](phd-readiness-20wk.md). Keep this file pure research so the two don't drift.

**Time budget:** 2h/day × 3 days/week = **6h/week**. Each **Day** below is one ~2h block with a single
**Outcome** — the thing that exists when the block ends. Three daily outcomes compound into the week's
deliverable. Milestones (git tags, first public signal, gate) are marked **in bold**.

**The goal this research serves:** a fundable profile for a **US R1 (global rank < 200 preferred)** —
via PhD admission *or* an RA/visiting position. Per [`short-list.md`](short-list.md), the preprint is
table stakes; the **differentiator result** and the **`kvbits`** artifact are what move funding.

### Cadence & timeline reality (read before starting)

At 6h/week the research spine runs **~24 weeks** (vs. 15 at the old ~10h/week). Starting ~Jul 13:

| Milestone | ~Week | ~Date | Bearing on the US Fall-2027 cycle |
|---|---|---|---|
| First public signal (reproduction) | 3 | early Aug | Something real to point at, early |
| `v0.1-lemma` — theorem verified | 8 | late Sep | Enables letter re-contact + wave-1 outreach |
| **arXiv v1 live** | 17 | early Nov | **In time** for the RA email + December apps |
| **arXiv v2 + `kvbits`** | 24 | late Dec | Lands *around/after* Dec-15 deadlines → strengthens **January** apps + interviews |

**Implication:** the December batch rests on **v1**; v2 + `kvbits` are your January/interview edge. If
you need v2 *inside* December applications, you must raise the cadence — this plan does not assume it.

**Definition of done (Week 24):** theorem proven + verified · **arXiv v1** (theory + money plot) ·
**arXiv v2** (adds the differentiator) · public benchmark repo · technical report · blog series
(5 posts) · **`kvbits` released** (`pip install`-able + Colab) · **differentiator result** (derived
allocation vs. eviction at equal memory + measured GB/tokens-sec).

## Operating rules

1. **Outcome-based days.** Each Day's Outcome exists at the end of its 2h block, or it doesn't — if
   it's not real, cut scope, never silently extend. A week is done when its 3 outcomes are real.
2. **Week 8 is the only gate.** The theorem must be proven *and* numerically verified. If the math
   fails twice, ship the loose bound, note it in limitations, and proceed. Never re-enter the gate.
3. **Pre-register predictions (Week 11).** Commit the derived allocations *before* validation runs.
4. **Scope only shrinks.** Allowed cuts, in order: the differentiator layer (W21–24) → Qwen model →
   LongBench subsets → per-head granularity → ablations. **Never cut:** the bound, the
   bound-vs-measured plot, the oracle frontier, the three-way allocation comparison.
5. **Eviction methods are baselines, never a combined method** (per `CLAUDE.md` — mixed
   eviction+quantization is out of scope). They are only things to *compare against at equal memory*.
6. **The differentiator is the first cut.** W21–24 is a stretch on a complete base: if research slips,
   a lean v1 + the benchmark still ship. Never let it delay v1.
7. **One model, ≤2 tasks, depth over breadth.** A 1B model on Colab Pro / one consumer GPU suffices.
8. **End-of-week ritual (Day 3).** Push; update the README results/state; one line in
   `paper/notes/log.md`. A run of entries = a public record of consistent output (app material).
9. **Blog ~every 4 weeks.** Drafts → `docs/blog/drafts/`, then publish in the Write phase.
10. **Buffer is not free time.** If a risk doesn't materialize, pull the next day's outcome forward.

## Phase & tag map

| Phase | Weeks | Focus | Tag / milestone |
|-------|-------|-------|-----------------|
| 0 · Instrument & reproduce | 1–3 | repo + KV dump + one heuristic | first public signal (W3) |
| 1 · Theory spike | 4–8 | value bound → key bound → allocation → **gate** | `v0.1-lemma` (W8) |
| 2 · Measure structure | 9–11 | spectra, entropy, pre-registered predictions | `v0.2-stats` (W11) |
| 3 · Oracle frontier | 12–14 | empirical rate–distortion upper bound + KIVI | — |
| 4 · Validate, benchmark & ship v1 | 15–17 | money plot + full comparison + **lean arXiv v1** | `v0.3-results` (W16) · **v1 live** (W17) |
| 5 · Write | 18–20 | report + paper draft + revision + blog series | `v0.4-draft` (W20) |
| 6 · Differentiate & ship v2 | 21–24 | equal-memory differentiator + `kvbits` + **arXiv v2** | `v1.0-arxiv` (W24) |

---

## Phase 0 — Instrument & reproduce

### Week 1 — Reproducible repo
- [ ] **Day 1** — Fresh-clone install (`venv` → `pip install -e ".[dev]"`); run `pytest -q`; fix import breakage. *Outcome:* clean env, quantizer tests green.
- [ ] **Day 2** — Read `src/kvbits/quantizers.py` (confirm stochastic uniform per-channel & per-token), fill docstrings; pick the target model (Llama-3.2-1B vs Qwen2.5-1.5B) → record in `experiments/configs/*.yaml`. *Outcome:* model chosen, quantizers understood.
- [ ] **Day 3** — Load the model; generate ~50 tokens to confirm GPU/Colab; end-of-week ritual. *Outcome:* model runs end-to-end locally.

### Week 2 — KV-cache instrumentation
- [ ] **Day 1** — Forward hook capturing K and V per layer during generation. *Outcome:* per-layer KV dump works.
- [ ] **Day 2** — Extend the hook per-head; dump to disk (npz/safetensors) under `results/`; verify shapes `[layers, heads, seq, dim]`. *Outcome:* **full KV cache dumped + shape-verified** (instrumentation done).
- [ ] **Day 3** — Pick 1–2 long-context tasks (LongBench/RULER); download a small slice; ritual. *Outcome:* eval data staged.

### Week 3 — Reproduce one eviction heuristic
- [ ] **Day 1** — Read H2O + SnapKV method sections; pick the simpler; create `research/reproductions/<method>/` from TEMPLATE; pre-register the target number. *Outcome:* reproduction target pre-registered.
- [ ] **Day 2** — Implement attention-score accumulation + eviction step (top-k heavy hitters + recent window); wire behind a config flag. *Outcome:* eviction runs behind a flag.
- [ ] **Day 3** — Run on one task; reproduce the paper's headline plot; record match/gap + fidelity rung; draft **blog #1**; ritual. *Outcome:* **faithful reproduction with a matching plot — first public signal.**

## Phase 1 — Theory spike

### Week 4 — Value-side bound + QJL
- [ ] **Day 1** — Read QJL §1–2 (setup) + §3 (main lemma + proof). *Outcome:* QJL lemma understood.
- [ ] **Day 2** — Reproduce the QJL main lemma by hand → `reproductions/qjl/`; numerical check (random vectors, variance ≤ bound). *Outcome:* QJL lemma reproduced + checked.
- [ ] **Day 3** — State the `o = a·V` convex-combination lemma in `theory.tex`; prove value perturbation passes ≤ linearly → Lemma 1; ritual. *Outcome:* **value-side bound proven (Lemma 1).**

### Week 5 — Value wrap-up + key-side setup
- [ ] **Day 1** — Fill `docs/literature/papers/qjl.md`; stub `paper/main.tex` (headers + one-line claim each). *Outcome:* QJL note + paper skeleton.
- [ ] **Day 2** — Write the softmax-Lipschitz lemma statement in `theory.tex`; derive the key-perturbation → softmax → output-error chain (scratch). *Outcome:* key-side chain drafted.
- [ ] **Day 3** — Identify amplification factors (`‖q‖`, `diam(V)`, `1/√d`); write into `theory.tex`; ritual. *Outcome:* amplification factors formalized.

### Week 6 — Key-side bound + allocation corollary
- [ ] **Day 1** — Set up the Lagrangian: minimize total bits subject to a target output error. *Outcome:* optimization set up.
- [ ] **Day 2** — Derive the closed-form `b_K − b_V` corollary → `theory.tex`. *Outcome:* **allocation corollary derived.**
- [ ] **Day 3** — Implement `src/kvbits/bounds.py` (predicted-error formula) + a smoke test on random inputs; draft **blog #2**; ritual. *Outcome:* predicted-error code runs.

### Week 7 — Fallback + close the proof
- [ ] **Day 1** — Fallback prep: sketch the triangle-inequality loose key bound (in case the tight one stalls). *Outcome:* loose-bound fallback ready.
- [ ] **Day 2** — Close the proof (tight or loose); finalize the corollary in `theory.tex`. *Outcome:* proof closed on paper.
- [ ] **Day 3** — Lock `theory.tex` (mark frozen); implement the random q/K/V generator in `tests/test_bound.py`; ritual. *Outcome:* theory frozen, test harness started.

### Week 8 — GATE: numerically verified · `v0.1-lemma`
- [ ] **Day 1** — Add the quantize step (2/3/4-bit) + measured-error computation to `tests/test_bound.py`. *Outcome:* measured error computed.
- [ ] **Day 2** — Assert measured ≤ predicted across bit widths; loop many seeds; run `pytest` — **the gate**. If it has failed twice: adopt the loose bound + a limitations note. *Outcome:* **bound numerically verified (GO/NO-GO passed).**
- [ ] **Day 3** — Tag **`v0.1-lemma`**; publish **blog #1**; ritual. *Outcome:* **theorem proven + verified — `v0.1-lemma` shipped.**

## Phase 2 — Measure structure

### Week 9 — Spectra
- [ ] **Day 1** — Read Trefethen & Bau Lec 1–5 (matrix–vector, orthogonality, SVD, low-rank, Eckart–Young); public notes → `docs/literature/notes/math/`. *Outcome:* NLA/SVD notes public.
- [ ] **Day 2** — Per-layer/head SVD of the dumped K matrices. *Outcome:* K spectra computed.
- [ ] **Day 3** — SVD of the V matrices; store singular-value spectra; ritual. *Outcome:* K/V spectra stored.

### Week 10 — Entropy + stats hooks
- [ ] **Day 1** — Compute attention-weight entropy per layer/head. *Outcome:* attention entropy computed.
- [ ] **Day 2** — Compute a token-importance concentration metric. *Outcome:* concentration metric computed.
- [ ] **Day 3** — Implement `src/kvbits/stats.py` hooks for `‖q‖`, `r_K`, `r_V`, `diam(V)`; run collection; dump JSON to `results/stats/`; ritual. *Outcome:* **`stats.py` collecting all four quantities.**

### Week 11 — Writeup + pre-registered predictions · `v0.2-stats`
- [ ] **Day 1** — Plot K/V spectra across depth + attention entropy across layers/heads (`scripts/`). *Outcome:* structure plots.
- [ ] **Day 2** — Write "How compressible is the KV cache, really?" → `report.md` §5; compute derived allocations via `allocation.py` + the predicted `b_K − b_V` heatmap. *Outcome:* writeup + predicted allocations.
- [ ] **Day 3** — Sanity-check the story; commit the prediction heatmap to README (timestamped = pre-registration); narrate into `experiments.tex`; tag **`v0.2-stats`**; draft **blog #3**; ritual. *Outcome:* **predictions pre-registered — `v0.2-stats` shipped.**

## Phase 3 — Oracle frontier

### Week 12 — Oracle compressor
- [ ] **Day 1** — Read Cover & Thomas ch.2 (entropy, MI); define the oracle objective (min cache s.t. output error ≤ ε). *Outcome:* oracle objective defined.
- [ ] **Day 2** — Implement the token-eviction oracle (full future knowledge, greedy drop). *Outcome:* eviction oracle.
- [ ] **Day 3** — Implement the bit-quantization oracle (search bit budget per layer); ritual. *Outcome:* quantization oracle.

### Week 13 — Validate + rate–distortion framing
- [ ] **Day 1** — Validate the oracle on one prompt (recover full-cache output as ε → 0); sweep ε; record points. *Outcome:* oracle validated + swept.
- [ ] **Day 2** — Store frontier data to `results/`; read Cover & Thomas ch.10 intro (rate–distortion). *Outcome:* frontier data stored.
- [ ] **Day 3** — Frame the oracle sweep as an empirical rate–distortion curve; plot it; ritual. *Outcome:* **rate–distortion frontier plotted.**

### Week 14 — KIVI baseline
- [ ] **Day 1** — Implement KIVI-style quant (per-channel K, per-token V) via `quantizers.py`. *Outcome:* KIVI quant implemented.
- [ ] **Day 2** — Reproduce the KIVI baseline on WikiText-2 → `reproductions/kivi/`; add the KIVI point to the R–D plot. *Outcome:* KIVI baseline on the frontier.
- [ ] **Day 3** — Document the heuristic-vs-oracle gap (the novel measurement) in the report; update `benchmarks/protocol.md`; draft **blog #4**; ritual. *Outcome:* gap documented; protocol updated.

## Phase 4 — Validate, benchmark & ship v1

### Week 15 — The money plot
- [ ] **Day 1** — Implement `src/kvbits/patch.py` (HF attention patching for on-the-fly KV quant); run the model at 4-bit KV; confirm coherent text. *Outcome:* quantized-KV generation works.
- [ ] **Day 2** — Implement `experiments/02_bound_vs_measured.py`; run across 2/3/4-bit per layer; commit raw outputs. *Outcome:* predicted-vs-measured data.
- [ ] **Day 3** — Plot predicted vs. measured; check the bound *tracks* reality (correlation is the bar); if loose, reframe the headline; **start the arXiv cs.LG endorsement path** (it takes days); ritual. *Outcome:* **money plot — the bound tracks reality.**

### Week 16 — Full benchmark, frozen · `v0.3-results`
- [ ] **Day 1** — Allocation comparison: WikiText-2 PPL × 3 budgets × 3 schemes; add 2 LongBench subsets. *Outcome:* three-way comparison run.
- [ ] **Day 2** — Add H2O/SnapKV/StreamingLLM/KIVI/derived to `RESULTS.md`; plot quality vs. budget against the oracle frontier; check the gap ↔ rank/entropy correlation. *Outcome:* leaderboard vs. oracle.
- [ ] **Day 3** — Commit all raw outputs (figures regenerate GPU-free); freeze experiments (new ideas → `future_work.md`); tag **`v0.3-results`**; ritual. *Outcome:* **benchmark frozen — `v0.3-results` shipped.**

### Week 17 — Ship lean arXiv v1
- [ ] **Day 1** — Assemble the lean **v1** (lemma + allocation corollary + money plot + comparison) from the report; `make figures`. *Outcome:* v1 manuscript assembled.
- [ ] **Day 2** — Confirm the cs.LG endorsement; set arXiv metadata + categories. *Outcome:* arXiv-ready.
- [ ] **Day 3** — **Submit v1 to arXiv** (or post the PDF to the site if endorsement stalls — don't wait); link from the site; ritual. *Outcome:* **arXiv v1 LIVE — a citable artifact for outreach + the RA email.**

## Phase 5 — Write

### Week 18 — Paper draft I
- [ ] **Day 1** — Draft the abstract + intro in `paper/sections/`. *Outcome:* abstract + intro.
- [ ] **Day 2** — Polish the theory-section proofs. *Outcome:* theory section clean.
- [ ] **Day 3** — Write the experiments section from the frozen results; ritual. *Outcome:* experiments section.

### Week 19 — Paper draft II + report
- [ ] **Day 1** — Write related work in `related.tex` from the `docs/literature/` notes. *Outcome:* related work.
- [ ] **Day 2** — Write limitations + future work; fill `report.md` (unabridged, incl. negative results). *Outcome:* limitations + report.
- [ ] **Day 3** — Verify `make figures` regenerates all plots on a clean checkout; compile `paper/main.tex` end to end; draft **blog #5**; ritual. *Outcome:* **full first-draft PDF compiles.**

### Week 20 — Revision + blog + hygiene · `v0.4-draft`
- [ ] **Day 1** — Revision pass: tighten the argument, fix proof gaps a reader would catch; sharpen title/abstract; proofread. *Outcome:* revised draft.
- [ ] **Day 2** — Publish **blog #1–#5** → `docs/blog/published/`; repo hygiene (docstrings, dead code); verify quickstart from a fresh clone. *Outcome:* blog series live; repo clean.
- [ ] **Day 3** — Mark where the W21–22 differentiator slots into **v2**; cold-reader pass; tag **`v0.4-draft`**; ritual. *Outcome:* **submission-ready base — `v0.4-draft` shipped.**

## Phase 6 — Differentiate & ship v2

### Week 21 — Beidi lever: the equal-memory comparison
- [ ] **Day 1** — Design the comparison: derived-allocation quantization vs. H2O/SnapKV eviction at **matched KV memory** on 2 LongBench subsets (comparison only — no hybrid, per `CLAUDE.md`). *Outcome:* comparison designed.
- [ ] **Day 2** — Run it; commit raw outputs. *Outcome:* equal-memory results.
- [ ] **Day 3** — Analyze — is allocation-optimal *quantization* competitive with / better than *eviction* at equal memory? Write into the paper (v2) + report; ritual. *Outcome:* **the differentiator finding.**

### Week 22 — Tri Dao lever: the systems measurement
- [ ] **Day 1** — Instrument end-to-end KV memory (GB) + throughput (tokens/s) at the derived allocation vs. FP16 KV, real model + long context. *Outcome:* measurement harness.
- [ ] **Day 2** — Run it; commit numbers; note kernel-feasibility honestly (what would need a custom kernel). *Outcome:* measured GB + tokens/s.
- [ ] **Day 3** — Write into the paper + report; update `RESULTS.md`; re-run `make figures`; sanity-check against the frozen v1 claims; ritual. *Outcome:* systems result in v2.

### Week 23 — `kvbits` OSS
- [ ] **Day 1** — Package `kvbits`: `pip install`-able; `apply_kvbits(model)` auto-derives the allocation on any HF model from measured `‖q‖, r_K, r_V, diam(V)`. *Outcome:* installable package.
- [ ] **Day 2** — One-click **Colab demo** (load → apply → GB saved + quality retained). *Outcome:* Colab demo.
- [ ] **Day 3** — Clean, honest **README** (what it does, its limits, one figure); verify install from a fresh env; ritual. *Outcome:* **`kvbits` ready to release.**

### Week 24 — Ship arXiv v2 · `v1.0-arxiv`
- [ ] **Day 1** — Final formatting; set metadata; **submit arXiv v2** (adds the differentiator); update the site's preprint link. *Outcome:* **arXiv v2 LIVE.**
- [ ] **Day 2** — **Release `kvbits` publicly** (PyPI + repo + a short, non-hyped launch post). *Outcome:* **`kvbits` public.**
- [ ] **Day 3** — Publish the technical-report link; confirm `make figures` is GPU-free from a clean clone; tag **`v1.0-arxiv`**; final log entry. *Outcome:* **research spine complete — `v1.0-arxiv` shipped.**

> **Handoff:** outreach (RA email to Tianlong Chen after **v1**, wave-1/2 faculty), the program
> portfolio for a **US R1 global rank < 200**, letters, and submission are scheduled in
> [`phd-readiness-20wk.md`](phd-readiness-20wk.md) — they consume the artifacts shipped above.
