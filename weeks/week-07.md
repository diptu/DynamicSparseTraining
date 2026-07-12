# Week 7 — The full three-way comparison table, frozen

> **Outcome (must exist Sunday night):** README results table filled in; every raw
> output committed to `results/`. **Experiments freeze Sunday night.**
> **Git tag:** `v0.3-results` · **Gate:** none (but a hard freeze)

---

## Definition of done (check all before Sunday)

- [ ] Full comparison run: perplexity (WikiText-2) + 2 LongBench subsets × 3 budgets × 3 schemes
- [ ] README results table filled in
- [ ] Every raw output committed to `results/` (figures regenerate GPU-free)
- [ ] `experiments/04_ablations.py`: per-layer/head gap breakdown produced
- [ ] Abstract + intro drafted (result shape is now known) in `paper/sections/intro.tex`
- [ ] **Experiments frozen** — new ideas → `paper/notes/future_work.md`, not code
- [ ] Tag `v0.3-results` pushed
- [ ] Friday ritual: push, update README, add the Week 7 row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] Draft the abstract + intro now that the result's shape is known.

### Engineering / Experiments
- [ ] Complete `experiments/03_allocation_compare.py`: uniform vs. fixed-asymmetric (KIVI-style)
      vs. derived, at matched average bits — perplexity + LongBench.
- [ ] Implement `experiments/04_ablations.py` and `scripts/plot_allocation_compare.py`.
- [ ] **Verify locally, then FREEZE:**
      ```bash
      python experiments/03_allocation_compare.py --config experiments/configs/llama32_1b.yaml
      python scripts/plot_allocation_compare.py
      ```

---

## Fallback (from Plan.md)
Cut LongBench to 1 subset; perplexity alone + the output-error plot still make the case.

Allowed cuts, in strict order (rule #4): Qwen model → LongBench subsets → per-head
granularity → ablations. **Never cut:** the lemma, the bound-vs-measured plot, the
three-way allocation comparison.

## Parking lot
Post-freeze this is the ONLY place new ideas go: `paper/notes/future_work.md`, not code.

## Notes / scratch
<!-- running notes for the week -->
