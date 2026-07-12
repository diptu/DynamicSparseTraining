# Week N — <outcome headline>

> Copy this file to `weeks/week-0N.md` at the start of each week and fill the angle-bracket
> fields from the matching row in `Plan.md`. One file per week; delete lines that don't apply.

> **Outcome (must exist Sunday night):** <the single deliverable, from Plan.md>
> **Git tag:** <`vX.Y-name`, or — if none> · **Gate:** <"GO/NO-GO: …" for Week 3, else "none">

---

## Definition of done (check all before Sunday)

- [ ] <the "How you'll know it's real" check from Plan.md, made concrete>
- [ ] <second concrete acceptance check>
- [ ] <third, if any>
- [ ] Friday ritual: push, update README results/state, add the Week N row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] <task — write notes/proofs directly into the target .tex, never a scratch file (rule #2)>
- [ ] <task>

### Engineering / Experiments
- [ ] <task>
- [ ] <task>
- [ ] **Verify locally** before calling it done — run the flow, don't just trust that code exists:
      ```bash
      # e.g. pytest -q   |   make figures   |   python experiments/0X_*.py --config ...
      ```

---

## Fallback (from Plan.md — the scope cut if this week's outcome is at risk)
<the row's fallback, or "None needed">

Allowed cuts, in strict order (rule #4): Qwen model → LongBench subsets → per-head
granularity → ablations. **Never cut:** the lemma, the bound-vs-measured plot, the
three-way allocation comparison.

## Parking lot
New ideas that aren't this week's outcome go to `paper/notes/future_work.md`, not code
(especially after the Week 7 experiment freeze).

## Notes / scratch
<!-- running notes for the week -->
