"""Quantizer correctness — Plan Week 1 exit criterion (these must pass)."""

import torch

from kvbits.quantizers import (
    StochasticUniformQuantizer,
    quantize_per_channel,
    quantize_per_token,
)


def test_output_shape_and_dtype_preserved():
    x = torch.randn(2, 8, 16)  # (heads, tokens, channels)
    q = quantize_per_channel(x, bits=4)
    assert q.shape == x.shape
    assert q.dtype == x.dtype


def test_dequantized_values_stay_in_range():
    x = torch.randn(4, 32, 64)
    q = quantize_per_token(x, bits=3)
    # Dequantized values never exceed the per-slice min/max used to build the grid.
    assert q.max() <= x.max() + 1e-5
    assert q.min() >= x.min() - 1e-5


def test_stochastic_rounding_is_unbiased():
    torch.manual_seed(0)
    x = torch.randn(8, 128, 64)
    # Average many independent stochastic quantizations -> should approach x.
    acc = torch.zeros_like(x)
    n = 400
    for _ in range(n):
        acc += quantize_per_channel(x, bits=3, stochastic=True)
    mean = acc / n
    assert torch.allclose(mean, x, atol=2e-2)


def test_more_bits_means_less_error():
    torch.manual_seed(0)
    x = torch.randn(4, 64, 32)
    err = {
        b: (quantize_per_channel(x, bits=b, stochastic=False) - x).abs().mean().item()
        for b in (2, 4, 8)
    }
    assert err[2] > err[4] > err[8]


def test_constant_slice_does_not_nan():
    x = torch.ones(2, 4, 8)
    q = quantize_per_channel(x, bits=4)
    assert torch.isfinite(q).all()
    assert torch.allclose(q, x)


def test_dataclass_dispatch_matches_functions():
    torch.manual_seed(1)
    x = torch.randn(2, 16, 8)
    qc = StochasticUniformQuantizer(bits=4, granularity="per_channel", stochastic=False)
    qt = StochasticUniformQuantizer(bits=4, granularity="per_token", stochastic=False)
    assert torch.equal(qc(x), quantize_per_channel(x, 4, stochastic=False))
    assert torch.equal(qt(x), quantize_per_token(x, 4, stochastic=False))
