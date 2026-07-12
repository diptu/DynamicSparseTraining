#!/usr/bin/env python
"""Predicted vs. measured attention-output error across 2/3/4-bit, per layer.

Plan Week 6 — "the money plot". Reads collected stats, evaluates
`kvbits.bounds.predicted_error`, measures true error from patched runs, and writes a
per-layer comparison table to results/ for scripts/plot_bound_vs_measured.py.

Usage:
    python experiments/02_bound_vs_measured.py --config experiments/configs/llama32_1b.yaml
"""

from _common import config_arg_parser, load_config


def main() -> None:
    args = config_arg_parser(__doc__).parse_args()
    _cfg = load_config(args.config)
    # TODO(Week 6): sweep bit widths, compare predicted_error vs measured, save table.
    raise NotImplementedError("Week 6: bound-vs-measured comparison")


if __name__ == "__main__":
    main()
