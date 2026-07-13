# The Research Journey

This repository is a **long-term research home**, not a single deliverable. Its spine is
one technical thesis — *keys and values should get different bit budgets, and the optimal
gap is derivable, not tuned* — and everything here is a stage in taking that idea from a
hunch to a published, defensible contribution.

Read this file top to bottom to understand the arc. Each stage links to the folder that
holds the real work.

```
   idea ──▶ literature ──▶ reproductions ──▶ benchmarks ──▶ experiments ──▶ paper
              │                                                  │            │
              └──────────────── technical report ◀──────────────┘            │
                                     │                                        │
                                  blog posts ◀──────────────────────────── (translate)
                                     │
                            PhD application materials  (the journey, packaged for admissions)
```

---

## The eight artifacts

| # | Artifact | Lives in | What "done" looks like | Status |
|---|----------|----------|------------------------|--------|
| 1 | **Literature review** | [`docs/literature/`](docs/literature/) | A standing, indexed map of the KV-cache compression field; every claim in the paper traces to a note here. | 🌱 seeded |
| 2 | **Reproductions** | [`research/reproductions/`](research/reproductions/) | Prior methods (QJL, KIVI, …) re-run and matched to reported numbers, so our baselines are honest. | 🌱 seeded |
| 3 | **Benchmark** | [`research/benchmarks/`](research/benchmarks/) | A frozen evaluation protocol + leaderboard: WikiText-2 perplexity and LongBench subsets at fixed bit budgets. | 🌱 seeded |
| 4 | **Experiments** | [`experiments/`](experiments/) · logs in [`weeks/`](weeks/) | Hypothesis-driven runs that test the bound and the allocation rule; every raw output committed. | 🏗️ scaffolded |
| 5 | **Technical report** | [`docs/reports/`](docs/reports/) | The long-form, no-page-limit record — including negative results and engineering detail the paper cuts. | 🌱 seeded |
| 6 | **Blog posts** | [`docs/blog/`](docs/blog/) | Accessible narratives of the ideas, for a general ML audience. | 🌱 seeded |
| 7 | **Research paper + OSS artifact** | [`paper/`](paper/) · `src/kvbits/` | A **two-stage arXiv preprint** (v1: theorem + money plot; v2: adds the equal-memory differentiator) **plus `pip install kvbits`** — an adoptable library that auto-derives the allocation on any HF model. Sequenced by [`Plan.md`](Plan.md) / [`todo.md`](todo.md). | 🏗️ scaffolded |
| 8 | **PhD / funding application materials** | [`docs/applications/`](docs/applications/) | SOP, research statement, CV, a **program portfolio** and letters campaign — the journey packaged to **secure funding at a US R1 (global rank < 200 preferred)**, via PhD admission or an RA/visiting position. Scheduled by [`phd-readiness-20wk.md`](phd-readiness-20wk.md); tiered by [`short-list.md`](short-list.md). | 🌱 templates |

Legend: 🌱 seeded (index + templates in place) · 🏗️ scaffolded (code/structure exists, content pending) · ✅ done.

---

## How the stages feed each other

- **Literature → everything.** The review in `docs/literature/` is the source of truth for
  prior work. The paper's `paper/sections/related.tex` is a *curated subset* of it, not a
  parallel effort. Add a paper's note once, in `docs/literature/papers/`; cite it everywhere.
- **Reproductions → benchmark.** A method isn't a baseline until it's reproduced. Numbers
  that land the leaderboard in `research/benchmarks/` come from `research/reproductions/`.
- **Benchmark + experiments → paper.** The paper's headline plots are experiments measured
  against the frozen benchmark protocol. Raw outputs live in `results/` and regenerate
  figures GPU-free (`make figures`).
- **Everything → technical report → blog → paper.** The report is the maximal record; the
  paper is its disciplined compression; the blog is its translation. Write the report as you
  go so the paper is an editing job, not a writing job.
- **The whole journey → applications.** The PhD/funding materials in `docs/applications/` narrate
  this repository: the question, the derivation, the validation, the taste shown by what was cut.
  Per [`short-list.md`](short-list.md), the preprint is *table stakes*; what converts a professor is
  the **differentiator result** (allocation-optimal quantization vs. eviction at equal memory; measured
  memory/throughput) and the **`kvbits`** artifact. The RA/visiting route is the one channel that
  secures funding on a rolling basis — kept front-and-center in [`phd-readiness-20wk.md`](phd-readiness-20wk.md).

---

## Sequencing & discipline

The **paper's** internal scope is fixed and only ever shrinks — see [`CLAUDE.md`](CLAUDE.md)
and [`Plan.md`](Plan.md). That discipline is unchanged by this reorganization. The journey
layer *around* the paper is where breadth lives: exploratory reproductions, negative results,
and writing that wouldn't fit an 8-page limit belong in `docs/` and `research/`, never bolted
onto the paper's scope.

The weekly cadence and the Friday commit ritual are tracked in [`weeks/`](weeks/) and
[`paper/notes/log.md`](paper/notes/log.md). Ten log entries is itself an artifact — a public
record of consistent output — which is why it feeds artifact #8.

## The goal this serves

The journey is not open-ended — it targets a concrete outcome: **secured funding at a US R1
(global rank < 200 preferred)**, through PhD admission *or* an RA/visiting-researcher position.
The strategy, honestly tiered, lives in [`short-list.md`](short-list.md); the 20-week execution
schedule (research + application logistics: letters, tests, program portfolio, outreach, submission)
lives in [`phd-readiness-20wk.md`](phd-readiness-20wk.md). Two disciplines from that analysis bind the
whole repo:

- **Apply to a survivable portfolio, not a wishlist.** A band of funded US R1s (global rank < 200)
  hosts efficiency/quantization/serving labs where six years of production ML/MLOps is a
  *differentiator*, not an apology — that is the core of the list, with a small number of reach labs.
- **The artifact is the ballgame, but the preprint is only table stakes.** What actually moves a
  funding decision is the **differentiator result** and the **`kvbits`** OSS artifact (artifact #7),
  plus the **RA/visiting side door**, which converts on a rolling basis independent of any committee.

## The lens

Every technical decision answers one question (from `Requirements.md`):

> *How does this reduce or explain memory in transformers?*
