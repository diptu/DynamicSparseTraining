# Benchmark protocol (freeze target: Plan Week 7)

> **Status:** 🌱 draft. Fill the TODOs as `experiments/` comes online, then **freeze**. After
> freezing, edits require a version bump (`v1 → v2`) and a changelog line at the bottom.

**Protocol version:** `v0` (draft, not yet frozen)

## Models

| Role | Model | HF id | Notes |
|------|-------|-------|-------|
| Primary | Llama 3.2 1B | `meta-llama/Llama-3.2-1B` | Everything must pass on this. |
| Secondary | Qwen 2.5 1.5B | `Qwen/Qwen2.5-1.5B` | First allowed scope cut if time-constrained. |

## Data & metrics

| Metric | Dataset | Slice / config | Scoring |
|--------|---------|----------------|---------|
| Perplexity | WikiText-2 (raw) | TODO: split, stride, seq len | standard PPL |
| Long-context | LongBench | TODO: which 2 subsets | task-native metric |

## Quantization budgets

- Average KV bits ∈ {2, 3, 4}.
- Quantizer family: **stochastic uniform** only (per-channel keys, per-token values).
- Recent-token full-precision window: TODO (state size or "none").

## Schemes compared

1. **uniform** — same bits to K and V.
2. **fixed-asymmetric** — KIVI-style fixed K>V split. See `research/reproductions/kivi/`.
3. **derived** — closed-form `b_K − b_V` from `src/kvbits/allocation.py`.

All three evaluated at each budget, at **matched average bits**.

## Determinism

- Seeds: TODO (list). Report mean ± std where stochastic quantization is used.
- Hardware: single consumer GPU / Colab Pro is sufficient; results are hardware-independent
  once raw outputs are committed.

## Output contract

- Raw per-run outputs → repo `results/` (committed).
- Digest → `RESULTS.md` in this folder.
- Figures → `results/figures/` via `scripts/` (`make figures`).

## Changelog

- `v0` — initial draft.
