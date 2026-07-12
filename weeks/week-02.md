# Week 2 — A key-side bound attempt on paper

> **Outcome (must exist Sunday night):** a candidate key-side bound and allocation
> corollary exist end-to-end (unverified), plus code that forces the algebra concrete.
> **Git tag:** — · **Gate:** none (the gate is next week)

---

## Definition of done (check all before Sunday)

- [ ] Key-side bound drafted in `paper/sections/theory.tex` (Lemma 2, tight or loose)
- [ ] Bit-allocation corollary (`b_K − b_V` closed form) derived and written down
- [ ] `bounds.py` `predicted_error` implements the RHS as written (already scaffolded — reconcile with the proof)
- [ ] Friday ritual: push, update README state, add the Week 2 row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] Attack the hard half: **softmax-Lipschitz lemma** → key perturbation → output error.
      Key error is scaled by `‖q‖`, passed through softmax (Lipschitz), scaled by value spread.
- [ ] Derive the **Lagrangian bit-allocation corollary** at fixed target output error.
- [ ] Draft both directly into `paper/sections/theory.tex` (Lemma 2, Theorem, Corollary).

### Engineering / Experiments
- [ ] Reconcile `src/kvbits/bounds.py` with the proof — the formula and the constant `C`
      should match what's on paper (leave `C` symbolic until Week 3 pins it).
- [ ] **Verify locally** the code path at least runs:
      ```bash
      PYTHONPATH=src python -c "from kvbits.bounds import BoundInputs, predicted_error; print('ok')"
      ```

---

## Fallback (from Plan.md)
If the tight bound stalls, switch **immediately** to a triangle-inequality key bound —
do not burn Week 3's buffer on elegance. A real loose bound beats a stuck tight one.

Allowed cuts, in strict order (rule #4): Qwen model → LongBench subsets → per-head
granularity → ablations. **Never cut:** the lemma, the bound-vs-measured plot, the
three-way allocation comparison.

## Parking lot
New ideas that aren't this week's outcome go to `paper/notes/future_work.md`, not code.

## Notes / scratch
<!-- running notes for the week -->
