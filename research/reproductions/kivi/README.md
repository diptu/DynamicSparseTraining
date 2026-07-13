# Reproduction: KIVI 2-bit asymmetric KV

- **Source:** KIVI, arXiv 2024 · [`docs/literature/papers/kivi.md`](../../../docs/literature/papers/kivi.md)
- **Cite key:** `kivi2024`
- **Their code:** TODO (check the paper)
- **Why we're reproducing:** KIVI is the **fixed-asymmetric baseline** in the paper's three-way
  allocation comparison (uniform vs. fixed-asymmetric/KIVI-style vs. derived). Its numbers must
  be ours, measured under our benchmark protocol, not quoted.

## Target (pre-registered)

- **What exactly:** per-channel 2-bit keys + per-token 2-bit values on Llama 3.2 1B, WikiText-2
  perplexity (and, budget permitting, a LongBench subset).
- **Reported number:** <transcribe KIVI's closest comparable — note their model differs; the
  point is trend + relative degradation, measured on *our* setup>
- **Fidelity rung we're aiming for:** **Quantitative** on WikiText-2 PPL under our protocol.

## Setup

- Model: Llama 3.2 1B · Data: WikiText-2 · via `experiments/` config + `src/kvbits` quantizers.
- The KIVI scheme = `quantizers.py` per-channel (K) + per-token (V) at a fixed 2/2 split.
- Deviations from the paper: different base model (they use larger Llamas) — so we compare the
  *scheme*, not their absolute number.

## Result

_TODO after Week 4._

## Verdict

_TODO. Promote to `research/benchmarks/RESULTS.md` once measured._

## Notes

Keep this reproduction's KIVI config in lockstep with the benchmark protocol so its row on the
leaderboard is apples-to-apples with our derived allocation.
