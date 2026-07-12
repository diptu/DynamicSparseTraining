# Week 6 — The money plot: predicted vs. measured attention error

> **Outcome (must exist Sunday night):** the bound-vs-measured plot exists and the bound
> *tracks* reality (correlation is the bar, not tightness).
> **Git tag:** — · **Gate:** none

---

## Definition of done (check all before Sunday)

- [ ] `experiments/02_bound_vs_measured.py` produces a per-layer predicted-vs-measured table
- [ ] `results/figures/bound_vs_measured.png` committed
- [ ] The bound tracks measured error across 2/3/4-bit (visible correlation)
- [ ] `experiments/03_allocation_compare.py` scaffolding in place for Week 7
- [ ] Friday ritual: push, update README, add the Week 6 row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] — (experiments have priority this week; heavy-compute week, queue overnight runs, rule #5)

### Engineering / Experiments
- [ ] Implement `experiments/02_bound_vs_measured.py`: predicted vs. measured attention-output
      error across 2/3/4-bit, per layer.
- [ ] Scaffold `experiments/03_allocation_compare.py` (uniform vs. fixed-asymmetric/KIVI vs. derived).
- [ ] Implement `scripts/plot_bound_vs_measured.py`.
- [ ] **Verify locally:**
      ```bash
      python experiments/02_bound_vs_measured.py --config experiments/configs/llama32_1b.yaml
      python scripts/plot_bound_vs_measured.py    # writes results/figures/bound_vs_measured.png
      ```

---

## Fallback (from Plan.md)
If the bound is very loose, reframe the headline: **"a first-order analysis explains X%
of quantization error."** That is still the paper.

Allowed cuts, in strict order (rule #4): Qwen model → LongBench subsets → per-head
granularity → ablations. **Never cut:** the lemma, the bound-vs-measured plot, the
three-way allocation comparison.

## Parking lot
New ideas that aren't this week's outcome go to `paper/notes/future_work.md`, not code.

## Notes / scratch
<!-- running notes for the week -->
