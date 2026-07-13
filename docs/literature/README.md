# Literature review

A **standing, indexed map** of the KV-cache compression field. This is the durable home for
everything we've read and how it relates to the thesis. It outlives any single paper draft.

> **Relationship to the paper.** `paper/sections/related.tex` is a *curated subset* of this
> review — the handful of works the paper must position against. This folder is the full
> picture, including tangents and works we ultimately don't cite. Add a paper's note here
> **once**; the paper cites it from here. (This supersedes the old convention in
> `paper/notes/reading/` of writing reading notes straight into `related.tex`.)

## Layout

```
literature/
├── README.md          this index
├── bibliography.bib   central BibTeX — every cited work, one entry
├── papers/            one note file per paper (see TEMPLATE.md)
└── reviews/           thematic survey writeups spanning many papers
```

## How to add a paper

1. Copy `papers/TEMPLATE.md` to `papers/<slug>.md` (e.g. `papers/kivi.md`).
2. Fill in the summary, the one-line positioning vs. our thesis, and what we borrow or reject.
3. Add its BibTeX to `bibliography.bib` with a matching cite key.
4. Add a row to the index table below.

## The field, in one taxonomy

KV-cache memory-reduction methods, by the knob they turn:

- **Quantization** — fewer bits per stored key/value. *Our lane.* (KIVI, KVQuant, QJL)
- **Rotation / transform** — decorrelate before quantizing (QuaRot, PolarQuant, transform coding). *Composes with allocation; out of scope for the paper, tracked as future work.*
- **Eviction / sparsity** — drop tokens (H2O, StreamingLLM). *Orthogonal.*
- **Low-rank / sharing** — factor or share the cache (MLA, GQA). *Architectural; orthogonal.*

Our specific contribution sits inside **quantization**: the *allocation* of a fixed bit
budget between keys and values, derived rather than tuned.

## Index

| Paper | Slug | Bucket | One-line positioning vs. our thesis | Note |
|-------|------|--------|-------------------------------------|------|
| QJL | [`qjl`](papers/qjl.md) | Quantization | Theorem-first KV quant via quantized JL sketch; closest in spirit, structural template. | 🌱 |
| KIVI | [`kivi`](papers/kivi.md) | Quantization | Established K/V asymmetry empirically; we *derive* it and predict its magnitude. | 🌱 |
| KVQuant | [`kvquant`](papers/kvquant.md) | Quantization | The empirical statistics landscape (outliers, layer sensitivity) our first-order analysis does/doesn't capture. | 🌱 |
| PolarQuant | [`polarquant`](papers/polarquant.md) | Rotation | Rotation + residual near the info-theoretic limit; orthogonal knob to allocation. | 🌱 |
| KV Cache Transform Coding | [`kv-transform-coding`](papers/kv-transform-coding.md) | Transform | Transform-coding view; our allocation step is reverse water-filling in output-distortion space. | 🌱 |

## Thematic reviews

| Review | Scope | Status |
|--------|-------|--------|
| [KV-cache compression landscape](reviews/kv-cache-compression-landscape.md) | The four buckets above, and where derived allocation fits. | 🌱 outline |
