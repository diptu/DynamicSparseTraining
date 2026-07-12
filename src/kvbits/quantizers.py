"""Stochastic uniform quantization for KV cache tensors.

Plan Week 1 deliverable. Two granularities matching the KV cache literature:

- **per-channel** (per feature-dimension): each coordinate of the head dimension
  gets its own scale/zero-point. This is how KIVI quantizes *keys* — outlier
  channels otherwise dominate the range.
- **per-token** (per sequence position): each cached token vector gets its own
  scale/zero-point. Typical for *values*.

Quantization is *stochastic* (unbiased): a real value is rounded up or down with
probability proportional to its distance to the two nearest grid points, so
E[quant(x)] = x. Unbiasedness is what makes the first-order perturbation bound in
`bounds.py` hold in expectation.
"""

from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import Tensor


def _quantize(x: Tensor, bits: int, dim: int, stochastic: bool) -> Tensor:
    """Affine uniform quantize/dequantize `x` along `dim` with `2**bits` levels.

    Scale and zero-point are computed from the min/max over every dim except
    `dim`, i.e. one (scale, zero) pair per index along `dim`. Returns a tensor of
    the same shape and dtype holding the dequantized values.
    """
    if bits < 1:
        raise ValueError(f"bits must be >= 1, got {bits}")
    levels = (1 << bits) - 1  # e.g. 4-bit -> 15 steps, 16 grid points

    reduce_dims = [d for d in range(x.ndim) if d != dim]
    x_min = x.amin(dim=reduce_dims, keepdim=True)
    x_max = x.amax(dim=reduce_dims, keepdim=True)

    scale = (x_max - x_min) / levels
    scale = torch.where(scale > 0, scale, torch.ones_like(scale))  # guard constant slices

    q = (x - x_min) / scale  # now in [0, levels]
    if stochastic:
        floor = torch.floor(q)
        prob = q - floor  # P(round up)
        q = floor + torch.bernoulli(prob)
    else:
        q = torch.round(q)
    q = q.clamp_(0, levels)

    return q * scale + x_min


def quantize_per_channel(x: Tensor, bits: int, *, stochastic: bool = True) -> Tensor:
    """Quantize `x` with one scale per channel (last dim, the head dimension)."""
    return _quantize(x, bits, dim=x.ndim - 1, stochastic=stochastic)


def quantize_per_token(x: Tensor, bits: int, *, stochastic: bool = True) -> Tensor:
    """Quantize `x` with one scale per token (dim -2, the sequence dimension)."""
    return _quantize(x, bits, dim=x.ndim - 2, stochastic=stochastic)


@dataclass
class StochasticUniformQuantizer:
    """Configurable stochastic uniform quantizer.

    Args:
        bits: number of bits per element (>= 1).
        granularity: "per_channel" or "per_token".
        stochastic: if True, use unbiased stochastic rounding; else round-to-nearest.
    """

    bits: int
    granularity: str = "per_channel"
    stochastic: bool = True

    def __call__(self, x: Tensor) -> Tensor:
        if self.granularity == "per_channel":
            return quantize_per_channel(x, self.bits, stochastic=self.stochastic)
        if self.granularity == "per_token":
            return quantize_per_token(x, self.bits, stochastic=self.stochastic)
        raise ValueError(
            f"granularity must be 'per_channel' or 'per_token', got {self.granularity!r}"
        )
