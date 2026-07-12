#!/usr/bin/env python
"""Collect per-layer/head statistics (‖q‖, r_K, r_V, diam(V)) on a model.

Plan Week 4-5. Loads a model + calibration corpus per the config, attaches
`kvbits.stats.StatsCollector`, and writes the dump to `output.stats_path`.

Usage:
    python experiments/01_collect_stats.py --config experiments/configs/llama32_1b.yaml
"""

from _common import config_arg_parser, ensure_parent, load_config


def main() -> None:
    args = config_arg_parser(__doc__).parse_args()
    cfg = load_config(args.config)
    ensure_parent(cfg["output"]["stats_path"])

    # TODO(Week 4): load model+data, StatsCollector().attach(model), iterate corpus,
    # .dump(cfg["output"]["stats_path"]).
    raise NotImplementedError("Week 4: statistics collection")


if __name__ == "__main__":
    main()
