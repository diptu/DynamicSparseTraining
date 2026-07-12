"""Numerical verification of the perturbation bound — Plan Week 3 GO/NO-GO GATE.

Draw random q, K, V; quantize K and V at various bit widths; measure the actual
attention-output error ‖õ − o‖ and assert it stays under `bounds.predicted_error`.
Correlation/validity across seeds and bit widths is the gate, not tightness.

Marked xfail until the constant C in bounds.predicted_error is pinned by the Week 2-3
proof. Flip `_BOUND_PROVEN = True` (and set the real C) once theory.tex is locked.
"""

import math

import pytest
import torch

from kvbits.bounds import BoundInputs, predicted_error
from kvbits.quantizers import quantize_per_channel, quantize_per_token

_BOUND_PROVEN = False  # set True in Week 3 once C is derived


def _attention(q, K, V):
    """Single-head attention output o = softmax(qᵀK/√d) V."""
    d = q.shape[-1]
    scores = (K @ q) / math.sqrt(d)  # (tokens,)
    a = torch.softmax(scores, dim=0)
    return a @ V  # (d,)


def _measure(seed, b_k, b_v, n_tokens=64, d=64, C=1.0):
    torch.manual_seed(seed)
    q = torch.randn(d)
    K = torch.randn(n_tokens, d)
    V = torch.randn(n_tokens, d)

    Kq = quantize_per_channel(K, bits=b_k, stochastic=True)
    Vq = quantize_per_token(V, bits=b_v, stochastic=True)

    o = _attention(q, K, V)
    o_hat = _attention(q, Kq, Vq)
    measured = (o_hat - o).norm().item()

    inp = BoundInputs(
        q_norm=q.norm().item(),
        head_dim=d,
        diam_v=(V.amax(0) - V.amin(0)).norm().item(),
        r_k=(K.amax() - K.amin()).item(),
        r_v=(V.amax() - V.amin()).item(),
    )
    return measured, predicted_error(inp, b_k, b_v, C=C)


@pytest.mark.skipif(not _BOUND_PROVEN, reason="Week 3 gate: constant C not yet derived")
@pytest.mark.parametrize("b_k", [2, 3, 4])
@pytest.mark.parametrize("b_v", [2, 3, 4])
@pytest.mark.parametrize("seed", range(5))
def test_measured_error_within_bound(seed, b_k, b_v):
    measured, bound = _measure(seed, b_k, b_v)
    assert measured <= bound


def test_error_decreases_with_more_bits():
    """Sanity check available before the proof: more bits -> less measured error."""
    errs = [
        sum(_measure(s, b, b)[0] for s in range(8)) / 8
        for b in (2, 4, 8)
    ]
    assert errs[0] > errs[1] > errs[2]
