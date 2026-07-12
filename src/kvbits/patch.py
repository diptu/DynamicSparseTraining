"""Hugging Face attention patching for on-the-fly KV cache quantization.

Plan Week 4. Wraps a model's attention so that keys and values are quantized (via
`kvbits.quantizers`) as they enter the cache, using per-layer/head bit widths from
`kvbits.allocation`. Enables end-to-end generation with quantized KV (the Week 4
exit criterion: coherent text at 4-bit) and the perplexity / LongBench evaluations
in Week 7.
"""

from __future__ import annotations

from kvbits.quantizers import StochasticUniformQuantizer  # noqa: F401 - used once implemented


def patch_kv_quantization(
    model,  # noqa: ANN001 - HF model, optional dep
    b_k: int = 4,
    b_v: int = 4,
    *,
    key_granularity: str = "per_channel",
    value_granularity: str = "per_token",
):
    """Patch `model`'s attention to quantize KV on the fly. Returns the patched model.

    TODO(Week 4): swap each attention module's cache-update path to route keys and
    values through StochasticUniformQuantizer at the given granularities/bit widths.
    Support both uniform (scalar b_k, b_v) and per-(layer, head) allocation tables.
    """
    raise NotImplementedError("Week 4: HF attention patching for on-the-fly KV quant")
