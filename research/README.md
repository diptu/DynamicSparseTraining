# research/ — the code-bearing scaffolding around the experiments

Reproductions of prior work and the frozen benchmark protocol. The paper's own runs live in
[`../experiments/`](../experiments/); the shared code they all use is [`../src/kvbits/`](../src/kvbits/).
Start with [`../JOURNEY.md`](../JOURNEY.md) for the full map.

| Folder | Artifact | Start here |
|--------|----------|------------|
| [`reproductions/`](reproductions/) | Prior methods re-run and matched to reported numbers | [reproductions/README.md](reproductions/README.md) |
| [`benchmarks/`](benchmarks/) | Frozen evaluation protocol + leaderboard | [benchmarks/README.md](benchmarks/README.md) |

## How the pieces relate

```
src/kvbits/  ── the shared package (quantizers, bounds, allocation, hooks)
     │
     ├── research/reproductions/  re-run OTHERS' methods  ─┐
     ├── experiments/             run OUR hypotheses       ─┤─▶ raw outputs in results/
     └── research/benchmarks/     the ruler: what to run, how to score, the leaderboard
```
