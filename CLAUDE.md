# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current state

This repository is **pre-code**. It currently contains only planning and specification documents:

- `README.md` — the research vision and intended package layout
- `Plan.md` — an 8-week execution plan with weekly exit criteria and git tags
- `Requirements.md` — functional spec for a separate "Live Paper" web platform

None of the source trees described below (`src/kvbits/`, `experiments/`, `paper/`, `tests/`, or the Next.js app) exist yet. Commands in `README.md` (`pip install -e .`, `pytest tests/test_bound.py`) will not run until that scaffolding is created — the earliest tasks in `Plan.md` (Week 1) are to create it. When asked to "run tests" or "build," first check whether the relevant files exist; do not assume the README reflects the working tree.

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
