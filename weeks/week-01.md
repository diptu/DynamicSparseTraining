# Week 1 — Reproducible repo + the easy half of the proof

> **Outcome (must exist Sunday night):** a fresh clone installs, tests pass, and the
> value-side bound is proven on paper.
> **Git tag:** — (no tag this week) · **Gate:** none — this week is deliberately easy and de-risks the tooling.

---

## Definition of done (check all before Sunday)

- [ ] Fresh clone → `pip install -e .` succeeds
- [ ] `pytest` passes (quantizer tests green)
- [ ] Value-side bound written out on paper (`paper/sections/theory.tex`, Lemma 1)
- [ ] `README.md` reflects the real repo state (no dead commands)
- [ ] QJL main lemma reproduced by hand (scratch in `paper/notes/reading/`)
- [ ] `paper/main.tex` stubbed: every section header + a one-line claim under each
- [ ] Friday ritual: push, update README, add the Week 1 row to `paper/notes/log.md`

---

## Tasks

### Theory / Writing
- [ ] **Read QJL carefully** (arxiv.org/abs/2406.03482) — it's the structural template for the whole paper.
- [ ] **Reproduce QJL's main lemma by hand** — notes to `paper/notes/reading/qjl.md`.
- [ ] **Prove the value-side bound** (the easy half): attention output `o = a·V` is a
      convex combination (weights sum to 1) ⇒ value perturbation passes through at most
      linearly. Write into `paper/sections/theory.tex` as Lemma 1.
- [ ] **Stub `paper/main.tex`**: all section headers present, one-line claim per section. ✅ (scaffolded)

### Engineering / Experiments
- [ ] **Repo reorg** to the target layout. ✅ (scaffolded)
- [ ] **`pyproject.toml`** — installable `kvbits` package. ✅ (scaffolded)
- [ ] **`src/kvbits/` skeleton** with per-module docstrings + plan-week TODOs. ✅ (scaffolded)
- [ ] **`quantizers.py`** — stochastic uniform, per-channel & per-token. ✅ (scaffolded, needs verification)
- [ ] **Unit tests** — `tests/test_quantizers.py`. ✅ (scaffolded, needs a green run)
- [ ] **Verify locally:** create the env and confirm the tests actually pass:
      ```bash
      python -m venv .venv && source .venv/bin/activate
      pip install -e ".[dev]"
      pytest -q
      ```

---

## Fallback
None needed — this week carries no research risk. If anything slips, it's tooling, not
the proof. Do **not** start the key-side bound early; Week 2 owns it.

## Notes / scratch
<!-- running notes for the week -->
