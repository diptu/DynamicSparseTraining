# Benchmark

The **frozen evaluation protocol** and the **leaderboard**. Everything that claims a number in
the paper — reproductions, baselines, our derived allocation — is measured here, the same way,
so rows are comparable.

> A benchmark is only useful if it doesn't move. Once the protocol below is frozen (Plan Week 7),
> changes require a version bump and a note, not a silent edit.

## Layout

```
benchmarks/
├── README.md     this file — the protocol
├── protocol.md   the frozen spec: models, data, metrics, budgets, seeds
└── RESULTS.md    the leaderboard — every measured configuration, one row each
```

## What we measure

| Axis | Values |
|------|--------|
| **Models** | Llama 3.2 1B (primary), Qwen 2.5 1.5B (secondary — first allowed scope cut) |
| **Metrics** | WikiText-2 perplexity; LongBench subsets (2, cut to 1 under pressure) |
| **Budgets** | 2, 3, 4 bits average KV |
| **Schemes** | uniform · fixed-asymmetric (KIVI-style) · **derived allocation** (ours) |

The headline comparison is **three schemes × three budgets** at matched average bits. That grid
is non-negotiable (see `CLAUDE.md` "never cut" list).

## Rules

1. **Same protocol for every row.** Model, data slice, sequence length, and seed are fixed in
   `protocol.md`. A row that deviates says so explicitly.
2. **Matched average bits.** Schemes are compared at equal *average* KV bits, so a 2-bit uniform
   row and a derived-allocation row spending the same mean budget sit side by side.
3. **Raw outputs are committed.** Everything lands in the repo's top-level `results/` (so
   `make figures` regenerates plots GPU-free). `RESULTS.md` is the human-readable digest of it.
4. **Reproduced before ranked.** A baseline appears only after `research/reproductions/` clears
   it on the fidelity ladder.

## Relationship to `experiments/`

`experiments/` *runs* the models and writes raw outputs; this folder *defines what to run and how
to score it*, and collects the verdicts. Think: `benchmarks/` is the ruler, `experiments/` is the
measuring.
