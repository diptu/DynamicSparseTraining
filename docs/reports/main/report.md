# Where Should the Bits Go? — Technical Report

- **Author:** Nazmul Alam Diptu
- **Started:** 2026-07-13 · **Last updated:** 2026-07-13
- **Status:** outline
- **Companion:** the arXiv paper in [`paper/`](../../../paper/); this is its unabridged source.

## Abstract / TL;DR

Keys and values in attention deserve different quantization bit budgets, and the optimal gap is
derivable from a first-order perturbation bound rather than tuned. This report is the full
account — every derivation step, all experiments, and the dead ends — behind the paper.

## 1. Problem & motivation

_TODO._ Value error passes through attention at most linearly (convex combination `o = a·V`);
key error amplifies inside the softmax. See [`docs/literature/papers/kivi.md`](../../literature/papers/kivi.md)
for the empirical anchor.

## 2. Background

_TODO._ Link the literature review: [`docs/literature/`](../../literature/).

## 3. Theory / derivation

_TODO — grows with Plan Weeks 1–3._

- **§3.1 Value-side bound** (easy half, Week 1): convex combination ⇒ linear pass-through.
- **§3.2 Key-side bound** (hard half, Week 2): softmax-Lipschitz ⇒ amplification by `‖q‖`,
  `diam(V)`. Fallback: triangle-inequality loose bound.
- **§3.3 Allocation corollary** (Week 3): Lagrangian ⇒ `b_K − b_V ≈ log₂(‖q‖·diam(V)/√d) + log₂(r_K/r_V)`.
- **§3.4 Numerical verification** ties to `tests/test_bound.py`.

## 4. Method / implementation

_TODO._ `src/kvbits/`: `stats.py`, `quantizers.py`, `allocation.py`, `bounds.py`, `patch.py`.

## 5. Experiments & results

_TODO — Weeks 5–7._ Frozen numbers in [`research/benchmarks/RESULTS.md`](../../../research/benchmarks/RESULTS.md).

## 6. Negative results & dead ends

_TODO._ Record every abandoned bound and surprising diagnostic here as they happen — this is the
section the paper can't carry and a future reader most needs.

## 7. Limitations

_TODO._

## 8. Future work

_TODO._ Mirror [`paper/notes/future_work.md`](../../../paper/notes/future_work.md).

## References

See [`docs/literature/bibliography.bib`](../../literature/bibliography.bib).
