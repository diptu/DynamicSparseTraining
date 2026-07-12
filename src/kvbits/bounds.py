"""Predicted attention-output error under KV quantization (the perturbation bound).

Plan Weeks 2-3. Implements the right-hand side of the main result:

    ‖õ − o‖ ≤ C · (‖q‖/√d) · diam(V) · r_K · 2^(−b_K)  +  r_V · 2^(−b_V)

where
    ‖q‖      query norm,
    d        head dimension,
    diam(V)  spread (diameter) of the value vectors,
    r_K, r_V coordinate ranges of keys / values,
    b_K, b_V bit widths for keys / values,
    C        a constant from the softmax-Lipschitz step (see paper/sections/theory.tex).

`predicted_error` is validated against measured error in tests/test_bound.py — that
numerical check is the Week 3 GO/NO-GO gate. The value-side term (second summand) is
the "easy half" proven in Week 1; the key-side term is the Week 2-3 result.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class BoundInputs:
    """Statistics needed to evaluate the bound, all measurable on a running model."""

    q_norm: float  # ‖q‖
    head_dim: int  # d
    diam_v: float  # diam(V)
    r_k: float  # coordinate range of keys
    r_v: float  # coordinate range of values


def key_term(inp: BoundInputs, b_k: int, *, C: float = 1.0) -> float:
    """Key-side contribution to the output-error bound (amplified through softmax)."""
    return C * (inp.q_norm / math.sqrt(inp.head_dim)) * inp.diam_v * inp.r_k * 2.0 ** (-b_k)


def value_term(inp: BoundInputs, b_v: int) -> float:
    """Value-side contribution (passes through at most linearly; the easy half)."""
    return inp.r_v * 2.0 ** (-b_v)


def predicted_error(inp: BoundInputs, b_k: int, b_v: int, *, C: float = 1.0) -> float:
    """Predicted upper bound on ‖õ − o‖ for key/value bit widths `b_k`, `b_v`."""
    return key_term(inp, b_k, C=C) + value_term(inp, b_v)
