#!/usr/bin/env python
"""Three-way allocation comparison at matched average bits.

Plan Week 7 (never-cut deliverable). Compares, at 2/3/4-bit average budgets:
    - uniform            (b_K = b_V)
    - fixed-asymmetric   (KIVI-style hand-tuned gap)
    - derived            (kvbits.allocation, the closed-form rule)
on perplexity (WikiText-2) + LongBench subsets. Writes the results table consumed by
the README and scripts/plot_allocation_compare.py.

Usage:
    python experiments/03_allocation_compare.py --config experiments/configs/llama32_1b.yaml
"""

from _common import config_arg_parser, load_config


def main() -> None:
    args = config_arg_parser(__doc__).parse_args()
    _cfg = load_config(args.config)
    # TODO(Week 7): for each budget x scheme, patch KV, eval ppl + LongBench, save.
    raise NotImplementedError("Week 7: three-way allocation comparison")


if __name__ == "__main__":
    main()
