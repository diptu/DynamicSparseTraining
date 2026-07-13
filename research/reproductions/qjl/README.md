# Reproduction: QJL main lemma

- **Source:** QJL, arXiv 2024 · [`docs/literature/papers/qjl.md`](../../../docs/literature/papers/qjl.md)
- **Cite key:** `qjl2024`
- **Their code:** TODO (check the paper)
- **Why we're reproducing:** intuition + structural template (Plan Week 1). Re-deriving the
  variance bound by hand is the fastest way to internalize the "bound output-relevant error"
  discipline the whole paper rests on.

## Target (pre-registered)

- **What exactly:** the main lemma — the sketched attention score is unbiased and its variance
  is bounded by the stated expression.
- **Reported number:** <the variance bound as stated in the paper — transcribe it here>
- **Fidelity rung we're aiming for:** **Conceptual** (a hand derivation + a small numerical
  check that the empirical variance of the sketch matches the bound).

## Setup

- No model needed — random vectors, the JL sketch, Monte-Carlo variance estimate.
- Reuse `numpy`/`torch` already in core deps; keep any code in this folder.

## Result

_TODO after Week 1._

## Verdict

_TODO._

## Notes

Longer by-hand derivation scratch may also live in `paper/notes/reading/qjl.md`; the distilled
takeaway belongs in the literature note.
