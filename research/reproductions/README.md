# Reproductions

A method is not a **baseline** until we've reproduced it and matched its reported numbers. This
folder is where prior work gets re-run before it's allowed onto the benchmark leaderboard. It's
also where we build intuition — reimplementing a lemma or a scheme by hand is the fastest way to
find its load-bearing assumption.

> **Why this is separate from `experiments/`.** `experiments/` holds *our* hypothesis-driven
> runs (does the bound track reality? which allocation wins?). Reproductions here re-derive
> *other people's* results. Keeping them apart keeps our contribution honest and our baselines
> auditable.

## Layout

```
reproductions/
├── README.md              this index
├── TEMPLATE/README.md     copy this for a new reproduction
├── qjl/                   reproduce the QJL main lemma (Plan Week 1)
└── kivi/                  reproduce the KIVI 2-bit asymmetric baseline (Plan Week 4)
```

Each reproduction is self-contained: its own README stating what's being reproduced, the target
number, what we got, and the fidelity verdict. Code reuses `src/kvbits/` where possible; anything
reproduction-specific stays local to the folder.

## The fidelity ladder

State honestly which rung a reproduction reached:

| Rung | Meaning |
|------|---------|
| **Conceptual** | Re-derived the math / re-implemented the idea; no numeric target. |
| **Qualitative** | Same trend/ordering as the paper, different absolute numbers. |
| **Quantitative** | Matches reported numbers within a stated tolerance on the same setup. |
| **Exact** | Bit-for-bit / seed-for-seed match (rare, usually needs their code). |

A baseline used in the paper's comparison table should reach **Quantitative** on at least one
shared metric, or carry an explicit caveat.

## How to add one

1. Copy `TEMPLATE/` to `<slug>/`.
2. Fill in the target (paper, table, exact number) *before* running — pre-register the goal.
3. Run, record raw output under the folder, and write the verdict against the fidelity ladder.
4. If it becomes a paper baseline, promote its numbers to `research/benchmarks/RESULTS.md`.

## Index

| Reproduction | Target | Rung reached | Status |
|--------------|--------|--------------|--------|
| [`qjl`](qjl/README.md) | QJL main lemma (variance bound on sketched scores) | — | 🌱 planned (Week 1) |
| [`kivi`](kivi/README.md) | KIVI 2-bit asymmetric KV, Llama perplexity | — | 🌱 planned (Week 4) |
