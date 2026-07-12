#!/usr/bin/env python
"""Ablations: per-layer / per-head bit-gap breakdown.

Plan Week 7 (first section demotable to an appendix under standing rule #4). Breaks
the derived allocation down by layer and head to show where the K/V gap concentrates.

Usage:
    python experiments/04_ablations.py --config experiments/configs/llama32_1b.yaml
"""

from _common import config_arg_parser, load_config


def main() -> None:
    args = config_arg_parser(__doc__).parse_args()
    _cfg = load_config(args.config)
    # TODO(Week 7): per-layer/head gap breakdown from stats + allocation.
    raise NotImplementedError("Week 7: ablations")


if __name__ == "__main__":
    main()
