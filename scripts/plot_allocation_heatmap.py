#!/usr/bin/env python
"""Figure: predicted b_K − b_V heatmap across layers/heads.

Plan Week 5. Reads results/stats/*.json, applies kvbits.allocation.optimal_gap, and
saves results/figures/allocation_heatmap.png. Runs GPU-free from committed stats.
"""

RESULTS = "results/stats"
OUT = "results/figures/allocation_heatmap.png"


def main() -> None:
    # TODO(Week 5): load stats, compute per-(layer,head) gap, imshow, savefig(OUT).
    raise NotImplementedError("Week 5: allocation heatmap figure")


if __name__ == "__main__":
    main()
