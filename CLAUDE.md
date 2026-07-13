# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current state

This repository is a **long-term research home** that documents the whole journey of one idea,
scaffolded but pre-results. It is organized around eight artifacts — see **`JOURNEY.md`** for the
map. The code trees are skeletons: modules and tests exist with docstrings/TODOs, but the proof,
statistics, experiments, and figures are not done yet.

- `README.md` — research vision, main result, repository structure
- `JOURNEY.md` — the narrative map tying all eight artifacts together (read this first)
- `Plan.md` — the paper's 10-week outcome-based plan (source of truth for sequencing)
- `Requirements.md` — functional spec for a separate "Live Paper" web platform (not built)

The journey layer (added around the original paper scaffold):

- `docs/literature/` — standing literature review (per-paper notes, `bibliography.bib`, thematic reviews). Supersedes the old "notes go straight into `related.tex`" convention: notes live here once; the paper cites from here. `paper/sections/related.tex` is a *curated subset*.
- `docs/reports/` — the technical report: the unabridged record incl. negative results. Write it as you go so the paper is an editing job.
- `docs/blog/` — blog posts (Markdown + front-matter, portable to the Next.js "Live Paper").
- `docs/applications/` — PhD application materials (templates only; do not fabricate personal content).
- `research/reproductions/` — prior methods (QJL, KIVI) re-run and matched to reported numbers before they become baselines.
- `research/benchmarks/` — the frozen eval protocol (`protocol.md`) and leaderboard (`RESULTS.md`).

Most content is index + template scaffolding: real content lands as the Plan progresses. When asked to "run tests" or "build," check whether the relevant files exist and are implemented; the scaffolds have TODOs, not finished code. The Next.js app does not exist.

## What this project is

Two related but distinct efforts live in this repo:

**1. The research paper — "Where Should the Bits Go?"** (the primary work; `README.md` + `Plan.md`)

A theory-first paper on KV cache quantization. The single technical thesis: keys and values should get *different* bit budgets, and the optimal gap is derivable, not tuned. The core claim to preserve in all work:

- Attention output `o = a·V` is a convex combination, so **value** quantization error passes through at most linearly.
- **Key** error sits inside the softmax and amplifies (scaled by query norm and value spread).
- A first-order perturbation bound turns this asymmetry into a closed-form allocation `b_K − b_V ≈ log₂(‖q‖·diam(V)/√d) + log₂(r_K/r_V)`, where every right-hand quantity is measurable on a running model.

Intended Python package layout (to be built): `src/kvbits/` with `stats.py` (per-layer/head hooks for ‖q‖, r_K, r_V, diam(V)), `quantizers.py` (stochastic uniform, per-channel & per-token), `allocation.py` (the closed-form rule), `bounds.py` (predicted error), `patch.py` (HF attention patching). Experiments are config-driven (one YAML per run under `experiments/configs/`). Target models: Llama 3.2 1B and Qwen 2.5 1.5B; a single consumer GPU / Colab Pro is sufficient.

**2. The "Live Paper" platform** (`Requirements.md`)

A separate Next.js (App Router) web app that renders the research as an interactive "living document" — MDX + KaTeX for the narrative, in-browser recomputation (Math.js/TensorFlow.js, Web Workers) for reactive simulations, Zustand for cross-component state, Tailwind for styling, Vercel for deploy. This is a *presentation layer* for the research, not the research itself. Do not conflate the two: the paper's deliverable is an arXiv PDF + reproducible figures; the platform's deliverable is a website.

## How to work here

- **The plan is the source of truth for sequencing.** `Plan.md` defines what happens each week, the one exit criterion per week, and the git tag that marks it (`v0.1-lemma` … `v1.0-arxiv`). Match new work to the current phase rather than jumping ahead.
- **Scope only shrinks, never grows.** Allowed cuts, in strict order: Qwen model → LongBench subsets → per-head granularity → ablations. Never cut: the perturbation lemma, the bound-vs-measured plot, the three-way allocation comparison (uniform vs. fixed-asymmetric/KIVI-style vs. derived).
- **Week 2 is the only hard gate:** the lemma + allocation corollary must be *both* proven on paper and numerically verified in `tests/test_bound.py` (random q/K/V → quantize → assert measured error ≤ bound across bit widths). If the tight (softmax-Lipschitz) bound is stuck, fall back to a looser triangle-inequality bound — a real loose bound beats a stuck tight one.
- **Pre-register predictions.** Derived optimal allocations (Week 4) get committed *before* the validation experiments run — this is deliberate for credibility. Don't retrofit predictions to results.
- **Reproducibility is a hard requirement.** Raw outputs go in `results/` and are committed so figures regenerate without a GPU; every paper figure must be the output of a script in `scripts/` (target: `make figures` regenerates all of them from a fresh clone).
- **Stay in scope.** Rotation-based schemes (QuaRot, PolarQuant), mixed eviction+quantization, and residual corrections are explicitly out of scope for the paper — treat them as related/future work, not implementation targets.

## Guiding question

From `Requirements.md`, the lens for every technical decision: *"How does this reduce or explain memory in transformers?"*
