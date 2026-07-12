# Week 9 — A submission-ready paper and a clean repo

> **Outcome (must exist Sunday night):** a second reader (or you, cold, after a day away)
> finds no blocking gap; the arXiv endorsement path is confirmed.
> **Git tag:** `v0.4-draft` · **Gate:** none

---

## Definition of done (check all before Sunday)

- [ ] Revision pass done: argument tightened, reader-catchable proof gaps fixed, title/abstract sharpened, proofread
- [ ] Repo hygiene: docstrings complete, quickstart verified from a fresh clone, dead code deleted
- [ ] `make figures` re-checked on a clean checkout
- [ ] **arXiv logistics sorted NOW** — cs.LG endorsement can take days; confirm the path
- [ ] Cold read finds no blocking gap
- [ ] Tag `v0.4-draft` pushed
- [ ] Friday ritual: push, update README, add the Week 9 row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] Revision pass: tighten the argument, fix proof gaps a reader would catch, sharpen
      title/abstract, proofread.
- [ ] Sort the arXiv endorsement path this week — do not leave it for Week 10.

### Engineering / Experiments
- [ ] Repo hygiene: docstrings, delete dead code, verify quickstart from a fresh clone.
- [ ] **Verify locally — fresh-clone reproducibility, cold:**
      ```bash
      cd $(mktemp -d) && git clone <repo> && cd theoretical-kv-cache
      pip install -e ".[dev,plot]" && pytest -q && make figures
      ```

---

## Fallback (from Plan.md)
Demote the ablation section to an appendix and ship the core. Never delay the timeline
for polish.

Allowed cuts, in strict order (rule #4): Qwen model → LongBench subsets → per-head
granularity → ablations. **Never cut:** the lemma, the bound-vs-measured plot, the
three-way allocation comparison.

## Parking lot
New ideas that aren't this week's outcome go to `paper/notes/future_work.md`, not code.

## Notes / scratch
<!-- running notes for the week -->
