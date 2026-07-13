# Leaderboard

Every measured configuration under [`protocol.md`](protocol.md), one row each. This is the
human-readable digest; raw outputs live in the repo's top-level `results/`. Fill in as
`experiments/` lands (Plan Weeks 6–7). Empty cells are honest — leave them blank, don't guess.

**Protocol version:** `v0` (draft)

## Llama 3.2 1B — WikiText-2 perplexity

| Scheme | Avg bits | PPL | Δ vs. fp16 | Raw output | Source |
|--------|----------|-----|-----------|------------|--------|
| fp16 (reference) | 16 | | — | | — |
| uniform | 2 | | | | `experiments/03_allocation_compare.py` |
| fixed-asymmetric (KIVI) | 2 | | | | `research/reproductions/kivi/` |
| **derived** | 2 | | | | `src/kvbits/allocation.py` |
| uniform | 3 | | | | |
| fixed-asymmetric (KIVI) | 3 | | | | |
| **derived** | 3 | | | | |
| uniform | 4 | | | | |
| fixed-asymmetric (KIVI) | 4 | | | | |
| **derived** | 4 | | | | |

## Llama 3.2 1B — LongBench

| Scheme | Avg bits | Subset | Score | Δ vs. fp16 | Raw output |
|--------|----------|--------|-------|-----------|------------|
| | | | | | |

## Qwen 2.5 1.5B (secondary — may be cut)

| Scheme | Avg bits | Metric | Score | Δ | Raw output |
|--------|----------|--------|-------|---|------------|
| | | | | | |

---

**The claim this table must support:** at matched average bits, **derived ≥ fixed-asymmetric ≥
uniform** on quality — and derived wins *without* per-scheme tuning, because the gap is predicted
from measured statistics. If derived doesn't beat fixed-asymmetric, the honest headline becomes
"a first-order analysis explains X% of the asymmetry" (Plan Week 6 fallback) — still a paper.
