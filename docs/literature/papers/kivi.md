# KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache

- **Authors / venue / year:** Liu, Yuan, Jin, Zhong, Xu, Braverman, Chen, Hu · arXiv 2024
- **Links:** https://arxiv.org/abs/2402.02750
- **Cite key:** `kivi2024`
- **Bucket:** Quantization
- **Read status:** to read fully (Plan Week 4)

## The claim (in one sentence)

Keys should be quantized **per-channel** and values **per-token**, because key outliers
concentrate in channels; this asymmetric scheme quantizes the KV cache to 2 bits with little
quality loss and no tuning.

## Method

Per-channel key quantization (to handle channel-wise outliers) + per-token value quantization,
with a small full-precision residual window for recent tokens.

## Positioning vs. our thesis

**The empirical anchor for our whole story.** KIVI *observes and exploits* the K/V asymmetry
but treats the granularity/budget choice as a design decision. We supply the missing *why* and
*how much*: a first-order bound that predicts keys need more bits, and a closed form for the gap.

## What we borrow

Per-channel (K) and per-token (V) quantization granularities — these become the
`quantizers.py` variants. KIVI is our headline "fixed-asymmetric" baseline in the three-way
allocation comparison.

## What we reject / where it stops

KIVI's asymmetry is fixed and hand-motivated; it doesn't vary the gap per layer/head or derive
it. Our allocation rule does both.

## Quotable numbers / results

<TODO — 2-bit KV results on Llama; perplexity + LongBench deltas for the baseline table.>

## Open threads

- KIVI's residual window vs. our allocation — do they stack? (future work)
