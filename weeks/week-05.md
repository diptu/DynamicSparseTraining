# Week 5 — Pre-registered allocation predictions, committed before any validation

> **Outcome (must exist Sunday night):** prediction heatmaps of `b_K − b_V` across
> layers/heads, committed **and timestamped before** the comparison runs.
> **Git tag:** `v0.2-stats` · **Gate:** none

---

## Definition of done (check all before Sunday)

- [ ] Derived optimal allocations computed from the corollary (`kvbits/allocation.py`)
- [ ] `results/figures/allocation_heatmap.png` committed (predicted `b_K − b_V` per layer/head)
- [ ] Heatmap committed to README **before** any Week 6/7 validation runs (pre-registration = credibility)
- [ ] Observations narrated into `paper/sections/experiments.tex`: keys > values? gap varies by layer?
- [ ] Tag `v0.2-stats` pushed
- [ ] Friday ritual: push, update README, add the Week 5 row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] Sanity-check the story against theory: does it predict keys need more bits? Does the gap vary by layer?
- [ ] Write findings into `paper/sections/experiments.tex` as they land.

### Engineering / Experiments
- [ ] Implement `kvbits/allocation.py` (`allocate`) — integer `(b_K, b_V)` at matched avg budget.
- [ ] Run `experiments/01_collect_stats.py` on the model(s).
- [ ] Implement `scripts/plot_allocation_heatmap.py`; produce the first heatmap.
- [ ] **Verify locally:**
      ```bash
      python scripts/plot_allocation_heatmap.py   # writes results/figures/allocation_heatmap.png
      ```

---

## Fallback (from Plan.md)
If per-head statistics are noisy, aggregate to per-layer only.

Allowed cuts, in strict order (rule #4): Qwen model → LongBench subsets → per-head
granularity → ablations. **Never cut:** the lemma, the bound-vs-measured plot, the
three-way allocation comparison.

## Parking lot
New ideas that aren't this week's outcome go to `paper/notes/future_work.md`, not code.

## Notes / scratch
<!-- running notes for the week -->
