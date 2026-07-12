# Week 8 — A complete first-draft PDF

> **Outcome (must exist Sunday night):** a complete first-draft PDF, and a stranger can
> clone → `make figures` → obtain every figure in the paper.
> **Git tag:** — · **Gate:** none

---

## Definition of done (check all before Sunday)

- [ ] All sections drafted: intro, theory, experiments, related work, limitations, future work
- [ ] `paper/main.tex` compiles end to end to a PDF
- [ ] `make figures` regenerates every plot from `results/` on a clean checkout (no GPU)
- [ ] Structure reviewed against QJL as the template
- [ ] Friday ritual: push, update README, add the Week 8 row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] Write the full draft, all sections. Completeness over depth this week — mark thin
      spots `TODO` and keep moving (Week 9 is for depth).
- [ ] Structure-review against QJL.

### Engineering / Experiments
- [ ] Wire `make figures` so every paper figure regenerates from committed `results/`.
- [ ] **Verify locally — the reproducibility check:**
      ```bash
      git clean -xdn          # confirm results/ is committed, not ignored
      make figures            # must produce every figure with no GPU
      pdflatex -output-directory=paper paper/main.tex
      ```

---

## Fallback (from Plan.md)
If any section is thin, mark it `TODO` and keep moving — Week 9 is for depth, Week 8 is
for completeness.

Allowed cuts, in strict order (rule #4): Qwen model → LongBench subsets → per-head
granularity → ablations. **Never cut:** the lemma, the bound-vs-measured plot, the
three-way allocation comparison.

## Parking lot
New ideas that aren't this week's outcome go to `paper/notes/future_work.md`, not code.

## Notes / scratch
<!-- running notes for the week -->
