# unified.md — Unifying Three Repos into One Long-Term Research Home

Goal: merge the three repos below into a **single, sustainably-maintained monorepo** whose narrative
runs **read the field → build the machinery → contribute at the frontier → paper → career.**

| Input repo | What it is | Pillar in the unified repo | Lands at |
|------------|-----------|----------------------------|----------|
| [`attention-papers`](https://github.com/diptu/attention-papers) | Curated literature roadmap (notes, not code): papers by year + taxonomy, across 6 stages from Neural Attention (2014) to KV-Cache Compression (2024+) and Open Problems. | **Literature** — the map of the field. | `docs/literature/` |
| [`transformer-from-scratch`](https://github.com/diptu/transformer-from-scratch) | Bottom-up transformer implementations in NumPy/PyTorch (attention, BERT, GPT, ViT, Llama…), FastAPI app, 7-day learning roadmap. | **Foundations** — the machinery + understanding. | `foundations/` |
| `theoretical-kv-cache` (this repo) | KV-cache compression research journey: reproductions, benchmarks, experiments, paper, blog, PhD apps. | **Research** — the original contribution. | umbrella (root) |

## Why unify (the three layers are one arc)

These three are not parallel hobbies — they're **three layers of a single research stack**, and they
line up perfectly at the KV cache:

1. **Literature** (`attention-papers`) ends at *Stage 5 — KV Cache Compression* and *Stage 6 — Open
   Problems*. That is precisely the research's starting point. Its bibliography should be the repo's
   single source of truth.
2. **Foundations** (`transformer-from-scratch`) implements attention from a blank file; its roadmap
   ends at **KV Cache, Flash Attention, rotary, GQA** — the research's substrate. A transparent,
   from-scratch model is the ideal *white-box instrument* to read off `‖q‖`, `r_K`, `r_V`, `diam(V)`
   and validate the perturbation bound before trusting a black-box HF model.
3. **Research** (`theoretical-kv-cache`) is the contribution at the frontier the other two point to.

**Unifying thesis:** *I read the field's whole arc (2014→open problems), built it from scratch to
understand it, and produced an original KV-cache compression result — theorem, benchmark, and paper.*
That is a complete PhD-application narrative in one repository.

## Decisions to confirm (my recommendation in bold)

1. **Umbrella:** **this repo (`theoretical-kv-cache`) is the umbrella** — it already has the journey
   scaffolding. Bring the other two in under it.
2. **Merge mechanism:** **`git subtree`** for both, so `attention-papers` and `transformer-from-scratch`
   commit history is preserved inside `docs/literature/` and `foundations/`. *(Alt: submodule — rejected,
   defeats "unified"; plain copy — rejected, loses history.)*
3. **Literature placement:** keep the established **`docs/literature/`** location (honors the earlier
   `docs/` + `research/` grouping). `attention-papers` becomes its canonical content; the KV-cache notes
   already scaffolded there get **merged into** its taxonomy, not duplicated.
4. **Optional rename:** the umbrella's scope is now the whole attention-memory arc. Consider renaming later
   (e.g. `transformers-memory-lab`) with kv-cache as the flagship. Not required to start.
5. **Packaging:** a single **`uv` workspace** — `kvbits` (research) + the foundations app. `attention-papers`
   is docs (HTML/Makefile), not a Python package, so it joins as content, not a workspace member.

## Target structure (monorepo)

```
theoretical-kv-cache/                 umbrella
├── README.md            portal to the THREE pillars
├── JOURNEY.md           extended: Literature → Foundations → Research arc
├── unified.md           this merge plan
├── todo.md              the 15-week research plan (unchanged)
├── ROADMAP.md           NEW: literature stages + 7-day build + 15-week research, one timeline
│
├── docs/
│   ├── literature/      ← attention-papers (subtree): papers/ (by year), taxonomy/, notes/,
│   │                      bibliography/, resources/ — plus the migrated KV-cache curated notes
│   ├── reports/  blog/  applications/          (existing)
│
├── foundations/         ← transformer-from-scratch (subtree): app/ (FastAPI + papers/), notebooks/
│
├── src/kvbits/          research package (unchanged)
├── research/{reproductions,benchmarks}
├── experiments/  paper/  results/  scripts/  tests/  weeks/
│
├── pyproject.toml       uv workspace root (members: ., foundations)
├── Makefile             unified targets, delegating per pillar
└── .github/workflows/   one CI running both code test suites
```

---

## Phase 0 — Decide & back up (do first)

- [ ] Confirm the five decisions above (umbrella, subtree, `docs/literature` placement, rename-later, uv workspace)
- [ ] Push a backup branch of **this** repo: `git branch backup/pre-unify`
- [ ] Clone `attention-papers` and `transformer-from-scratch`; confirm each builds/renders locally
- [ ] Note Python versions (this ≥3.10; foundations 3.12) → target **3.12** for the workspace
- [ ] Scan both external repos for secrets/large files that shouldn't enter history (checkpoints, datasets, built HTML)

## Phase 1 — Bring both external repos in (history-preserving subtrees)

- [ ] Add remotes: `git remote add lit https://github.com/diptu/attention-papers` and `git remote add foundations https://github.com/diptu/transformer-from-scratch`
- [ ] Fetch both: `git fetch lit && git fetch foundations`
- [ ] Subtree-add foundations: `git subtree add --prefix=foundations foundations main`
- [ ] Subtree-add literature into a staging prefix: `git subtree add --prefix=docs/literature-incoming lit main` (staging avoids clobbering existing `docs/literature/`)
- [ ] Verify history survived for both: `git log --oneline foundations/ | tail` and `... docs/literature-incoming/ | tail`
- [ ] Confirm no root-level collisions (both externals have `Makefile`/`scripts/`/`tests/` — now nested)
- [ ] Add `foundations/checkpoints/`, `foundations/datasets/raw/`, and any built-HTML dirs to `.gitignore`
- [ ] Commit on a `unify` branch; do **not** touch `main` yet

## Phase 2 — Reconcile the LITERATURE overlap (attention-papers ⇄ existing docs/literature)

The one genuinely overlapping merge — do it carefully, it's the repo's knowledge base.

- [ ] Compare `docs/literature-incoming/` structure to existing `docs/literature/` (papers/ vs papers-by-year, taxonomy/, reviews/)
- [ ] Adopt `attention-papers` as the canonical skeleton (its 6-stage chronology + taxonomy is more complete)
- [ ] Migrate the KV-cache curated notes I scaffolded (`qjl.md`, `kivi.md`, `kvquant.md`, …) into its `taxonomy/kv-cache/`
- [ ] Merge the two bibliographies into one canonical `docs/literature/bibliography.bib`; dedupe cite keys
- [ ] Reconcile `attention-papers/benchmarks/` with `research/benchmarks/` (keep the frozen protocol in `research/`; literature-side benchmarks become references)
- [ ] Fold the existing `docs/literature/README.md` index into the incoming one; keep the "how to add a paper" workflow
- [ ] Swap staging into place: replace `docs/literature/` with the reconciled tree; delete `docs/literature-incoming/`
- [ ] Fix cross-links from `paper/sections/related.tex` and `docs/reports/` to the reconciled paths

## Phase 3 — Reconcile tooling into one workspace

- [ ] Convert root `pyproject.toml` to a `uv` workspace; add `foundations` as a member
- [ ] Give `foundations/` its own `pyproject.toml` (e.g. package `tfs`) if it lacks one
- [ ] Resolve dependency overlaps (numpy, torch, pandas) to compatible pins
- [ ] Regenerate one root `uv.lock`; delete nested lockfiles
- [ ] Merge `.gitignore` files into one at root; remove redundant nested rules
- [ ] Unify `ruff`: one config covering `src/`, `experiments/`, `foundations/`
- [ ] Unify `pytest`: `testpaths = ["tests", "foundations/tests"]`; run `pytest -q` — both suites green
- [ ] Extend root `Makefile`: `foundations-test`, `foundations-serve`, `lit-build` (attention-papers HTML), keep existing targets
- [ ] Reconcile Dockerfiles (research vs foundations app) — one per pillar, documented

## Phase 4 — Structural integration & navigation

- [ ] Rewrite root `README.md` as a **three-pillar portal** (Literature · Foundations · Research), each a one-para pitch
- [ ] Extend `JOURNEY.md`: prepend a **Literature** and **Foundations** stage before the research arc; show read → build → contribute
- [ ] Add `foundations/` and the merged `docs/literature/` rows to the `JOURNEY.md` artifact table
- [ ] Keep `foundations/README.md` and the literature index intact but add "part of the unified repo" banners + backlinks
- [ ] Update `CLAUDE.md`: describe the three pillars, the workspace layout, and where each kind of work goes
- [ ] Create `ROADMAP.md`: attention-papers' 6 stages + the 7-day build roadmap + the 15-week research plan on one timeline

## Phase 5 — The intellectual bridges (this is why unification pays off)

- [ ] **Lit → research:** link every `docs/literature/` Stage-5/6 paper to its slot in `research/reproductions/` or `paper/sections/related.tex`
- [ ] **Foundations → research:** ensure `foundations/` attention exposes the KV cache explicitly (its roadmap's KV-Cache item)
- [ ] Implement stochastic-uniform quantization in `foundations/` mirroring `src/kvbits/quantizers.py`
- [ ] Notebook: instrument the from-scratch model to read `‖q‖`, `r_K`, `r_V`, `diam(V)` per layer/head
- [ ] Validate the research perturbation bound on the transparent from-scratch model (white-box sibling of `tests/test_bound.py`)
- [ ] Document both bridges in `docs/reports/`: "the field map and the white-box testbed behind the result"

## Phase 6 — Long-term maintenance conventions

- [ ] Write `CONTRIBUTING.md`: where each kind of work lives (literature / foundations / research / docs), naming, the ≤1h task habit
- [ ] One versioning scheme across pillars; keep research tags (`v0.1-lemma`…), add foundations + literature milestones
- [ ] Single **status dashboard** (`STATUS.md` or README top): all three roadmaps' checklists at a glance
- [ ] CI (`.github/workflows/`): one workflow — lint + both test suites + `make figures` smoke + literature HTML build
- [ ] Monthly **retro**: prune dead scaffolding, refresh `JOURNEY.md`/`ROADMAP.md` statuses, one log line
- [ ] Repo-wide **Friday ritual**: push, update statuses, one line in `paper/notes/log.md`
- [ ] Dependency hygiene: scheduled `uv lock --upgrade`; pin torch deliberately
- [ ] Docs single-source: one entry point linking `docs/literature/`, `foundations/docs/`, and the paper

## Phase 7 — Land it

- [ ] Open a PR `unify` → `main` summarizing the three-repo merge, structure, and bridges
- [ ] Self-review from a fresh clone: `uv sync` → `pytest` (both suites) → `make figures` → foundations app serves → literature renders
- [ ] Merge to `main`; tag `v0.5-unified`
- [ ] Update `diptu.github.io` to point at the one unified repo
- [ ] Add "merged into …" redirect notes to the `attention-papers` and `transformer-from-scratch` READMEs (or archive them)

---

## Long-term maintenance principles (evergreen)

1. **Three pillars, one story.** Literature = the map; Foundations = the machinery; Research = the
   contribution. Every addition belongs clearly to one, and `JOURNEY.md`/`ROADMAP.md` keep them on one arc.
2. **The bridges are the point.** Prefer work that connects pillars — a Stage-6 open problem becoming a
   reproduction, a from-scratch model validating a bound — over deepening one pillar in isolation.
3. **One bibliography, one workspace, one CI, one lockfile.** Divergent tooling and duplicate references
   are how a merged repo rots. Keep each single-source.
4. **Scope still only shrinks (per pillar).** The research discipline from `Plan.md`/`todo.md` is unchanged;
   literature and foundations grow one paper at a time, never all at once.
5. **Everything regenerates from a fresh clone.** `make figures` (research), the foundations quickstart,
   and the literature build must all work cold — that reproducibility is the long-term asset.
6. **Status is always visible.** A stale checklist is a lie; update it Fridays.
