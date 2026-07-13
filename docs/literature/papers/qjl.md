# QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead

- **Authors / venue / year:** Zandieh, Daliri, Han · arXiv 2024
- **Links:** https://arxiv.org/abs/2406.03482
- **Cite key:** `qjl2024`
- **Bucket:** Quantization
- **Read status:** to read carefully (Plan Week 1 — structural template for our paper)

## The claim (in one sentence)

A quantized Johnson–Lindenstrauss sketch of keys preserves attention scores in expectation
with bounded variance, enabling ~1-bit key storage with no dequantization overhead.

## Method

<TODO — reproduce the main lemma by hand (Plan Week 1). Longer derivation scratch may live in
`paper/notes/reading/qjl.md`; the distilled version goes here.>

## Positioning vs. our thesis

Closest in spirit: theorem-first, bounds attention-relevant error rather than per-vector
reconstruction error. QJL is a *representation* result (JL sketch); ours is an *allocation*
result (how to split a budget). They are compatible — the framing of "bound the thing that
reaches the output" is exactly what we push on.

## What we borrow

The structural template of the paper (lemma → bound → practical scheme), and the discipline
of bounding output-relevant error.

## What we reject / where it stops

QJL fixes a scheme; it doesn't ask how to *allocate* bits between keys and values under a joint
budget. That question is ours.

## Quotable numbers / results

<TODO — reported bit widths and accuracy retention.>

## Open threads

- Does the JL-sketch error interact with the K/V allocation gap? (future work)
