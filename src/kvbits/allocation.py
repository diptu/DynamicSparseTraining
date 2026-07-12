"""Closed-form optimal key-value bit allocation (the corollary).

Plan Week 5. Minimizing total bits (b_K + b_V) subject to a target output error,
via a Lagrangian on the `bounds.py` bound, yields a closed form for the *gap*:

    b_K − b_V ≈ log2( ‖q‖ · diam(V) / √d ) + log2( r_K / r_V )

Every quantity on the right is measurable per layer and per head (see stats.py), so
the optimal gap is a *prediction*, not a tuned hyperparameter. This module turns
measured statistics into (b_K, b_V) integer allocations at a target average budget.

The gap formula depends only on `bounds.BoundInputs`; deriving concrete integer bit
widths at a fixed average budget is the remaining Week 5 work.
"""

from __future__ import annotations

import math

from kvbits.bounds import BoundInputs


def optimal_gap(inp: BoundInputs) -> float:
    """Predicted continuous optimum of (b_K − b_V) from the corollary."""
    return math.log2(inp.q_norm * inp.diam_v / math.sqrt(inp.head_dim)) + math.log2(
        inp.r_k / inp.r_v
    )


def allocate(inp: BoundInputs, avg_bits: float) -> tuple[int, int]:
    """Return integer (b_K, b_V) whose mean is ~`avg_bits` and gap ~= `optimal_gap`.

    TODO(Week 5): round the continuous (gap, avg) solution to integers under the
    matched-average-budget constraint, then re-optimize the residual against the
    `bounds.predicted_error` surface. Stubbed until Week 4 statistics exist.
    """
    raise NotImplementedError("Week 5: integer allocation at matched average budget")
