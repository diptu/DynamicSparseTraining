# The KV-cache compression landscape

> **Status:** 🌱 outline. Fill in as the literature notes in `../papers/` accumulate.
> A thematic survey spans papers; per-paper detail stays in the paper notes.

## Purpose

Give a reader (and the paper's related-work section) a single map of *how* people shrink the
KV cache, and locate our contribution — **derived key/value bit allocation** — precisely on it.

## The four knobs

1. **Quantization** — fewer bits per stored element.
   - Uniform / per-channel / per-token variants; outlier handling.
   - Key works: KIVI, KVQuant, QJL. → *our lane.*
2. **Rotation / transform** — decorrelate coordinates before quantizing so bits are spent evenly.
   - QuaRot, PolarQuant, transform coding. → *composes with allocation; paper's future work.*
3. **Eviction / sparsity** — store fewer tokens.
   - H2O, StreamingLLM, SnapKV. → *orthogonal.*
4. **Low-rank / sharing** — factor or share the cache across heads/layers.
   - MLA, GQA/MQA. → *architectural; orthogonal.*

## Where we sit

Within quantization, existing methods **assume or tune** the key-vs-value asymmetry (keys get
more bits). We ask a narrower, sharper question: *given a fixed average budget, what is the
optimal split, and can it be predicted per layer and head from measurable statistics?* The
answer is a closed-form allocation from a first-order perturbation bound — a prediction, not a
hyperparameter.

## To write

- [ ] One paragraph per knob, with the 2–3 canonical citations each.
- [ ] A figure/table: methods × (bucket, granularity, tuned-or-derived, reported bits).
- [ ] The gap statement: no prior work *derives* the allocation from output distortion.
- [ ] Explicit composition claim: rotation equalizes *within* vectors; allocation exploits
      asymmetry *between* components — the two multiply, they don't overlap.
