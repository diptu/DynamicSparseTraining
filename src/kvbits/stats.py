"""Per-layer / per-head statistics hooks.

Plan Week 4. Registers forward hooks on a Hugging Face model's attention modules and
collects the four quantities the bound and allocation rule depend on:

    ‖q‖       query norm (per head, aggregated over tokens)
    r_K       coordinate range of keys
    r_V       coordinate range of values
    diam(V)   diameter (spread) of the value vectors

Output is a dump keyed by (layer, head) suitable for `allocation.optimal_gap`, written
under results/stats/ and committed so downstream figures regenerate without a GPU.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LayerHeadStats:
    """Collected statistics for a single (layer, head)."""

    q_norm: float = 0.0
    r_k: float = 0.0
    r_v: float = 0.0
    diam_v: float = 0.0
    n_tokens: int = 0


@dataclass
class StatsCollector:
    """Attaches to a model, accumulates per-(layer, head) statistics over a corpus.

    TODO(Week 4): implement `attach(model)` to register attention forward hooks,
    `.update()` accumulation, and `.dump(path)` to write results/stats/<model>.json.
    """

    stats: dict[tuple[int, int], LayerHeadStats] = field(default_factory=dict)

    def attach(self, model) -> "StatsCollector":  # noqa: ANN001 - HF model, optional dep
        raise NotImplementedError("Week 4: register attention hooks on the HF model")

    def dump(self, path: str) -> None:
        raise NotImplementedError("Week 4: serialize stats to results/stats/")
