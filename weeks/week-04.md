# Week 4 — One model generating coherent text with quantized KV

> **Outcome (must exist Sunday night):** a model produces coherent text with quantized
> KV at 4-bit, and a full per-layer/head statistics dump exists on disk.
> **Git tag:** — · **Gate:** none

---

## Definition of done (check all before Sunday)

- [ ] Llama 3.2 1B generates coherent text with quantized KV at 4-bit end-to-end
- [ ] Per-layer/head statistics dump written to `results/stats/llama32_1b.json`
- [ ] Related-work notes drafted directly into `paper/sections/related.tex`
- [ ] Friday ritual: push, update README state, add the Week 4 row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] Skim **KIVI + KVQuant** fully; write related-work notes **directly** into
      `paper/sections/related.tex` (reading = writing, rule #2).

### Engineering / Experiments
- [ ] Implement `kvbits/stats.py` hooks: collect `‖q‖`, `r_K`, `r_V`, `diam(V)` per layer/head.
- [ ] Implement `kvbits/patch.py`: HF attention patching for on-the-fly KV quantization.
- [ ] Get Llama 3.2 1B running end-to-end at 4-bit KV.
- [ ] **Verify locally** — eyeball a generation and confirm the dump exists:
      ```bash
      pip install -e ".[experiments]"
      python experiments/01_collect_stats.py --config experiments/configs/llama32_1b.yaml
      ```

---

## Fallback (from Plan.md)
Drop Qwen 2.5 entirely — a single-model paper is fine; declare it in limitations.

Allowed cuts, in strict order (rule #4): Qwen model → LongBench subsets → per-head
granularity → ablations. **Never cut:** the lemma, the bound-vs-measured plot, the
three-way allocation comparison.

## Parking lot
New ideas that aren't this week's outcome go to `paper/notes/future_work.md`, not code.

## Notes / scratch
<!-- running notes for the week -->
