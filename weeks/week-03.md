# Week 3 — GATE: the theorem, proven *and* numerically verified

> **Outcome (must exist Sunday night):** the perturbation theorem is proven (tight or
> loose) AND `tests/test_bound.py` passes across bit widths and seeds.
> **Git tag:** `v0.1-lemma` · **Gate:** ⛔ **GO/NO-GO — the only gate in the project.**

---

## Definition of done (check all before Sunday)

- [ ] Proof of the output-error theorem complete in `paper/sections/theory.tex`
- [ ] Allocation corollary finalized; `theory.tex` core result **locked**
- [ ] Constant `C` pinned in `src/kvbits/bounds.py`
- [ ] `tests/test_bound.py`: flip `_BOUND_PROVEN = True`, set real `C`, and it **passes**
      (measured error ≤ predicted, across 2/3/4-bit × many seeds)
- [ ] Tag `v0.1-lemma` pushed
- [ ] Friday ritual: push, update README state, add the Week 3 row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] Close the proof — tight (softmax-Lipschitz) or the loose triangle bound from the fallback.
- [ ] Finalize the corollary and lock the section.

### Engineering / Experiments
- [ ] Pin `C` in `bounds.py` from the proof.
- [ ] **Verify locally — this IS the gate:**
      ```bash
      pip install -e ".[dev]"
      pytest tests/test_bound.py -q      # must be green with _BOUND_PROVEN = True
      ```

---

## Fallback (from Plan.md)
A real loose bound beats a stuck tight one. **If the math has failed twice by now, ship
the loose bound and say so in limitations — then proceed. Never re-enter this week.**

Allowed cuts, in strict order (rule #4): Qwen model → LongBench subsets → per-head
granularity → ablations. **Never cut:** the lemma, the bound-vs-measured plot, the
three-way allocation comparison.

## Parking lot
New ideas that aren't this week's outcome go to `paper/notes/future_work.md`, not code.

## Notes / scratch
<!-- running notes for the week -->
