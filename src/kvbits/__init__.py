"""kvbits — first-order analysis of KV cache quantization.

Package map (see Plan.md for the week each module is due):
    quantizers.py   stochastic uniform quantization, per-channel / per-token   (Week 1)
    bounds.py       predicted attention-output error from the perturbation bound (Week 2-3)
    allocation.py   closed-form optimal key-value bit allocation                (Week 5)
    stats.py        per-layer/head statistics hooks (‖q‖, r_K, r_V, diam(V))    (Week 4)
    patch.py        HF attention patching for on-the-fly KV quantization        (Week 4)
"""

from kvbits.quantizers import (
    StochasticUniformQuantizer,
    quantize_per_channel,
    quantize_per_token,
)

__version__ = "0.1.0"

__all__ = [
    "StochasticUniformQuantizer",
    "quantize_per_channel",
    "quantize_per_token",
    "__version__",
]
