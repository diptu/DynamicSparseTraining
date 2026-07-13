# KV Cache Transform Coding

- **Authors / venue / year:** TODO · ICLR 2026
- **Links:** TODO
- **Cite key:** `kvtransformcoding2026`
- **Bucket:** Transform
- **Read status:** to read

## The claim (in one sentence)

Views the KV cache through the lens of transform coding (decorrelate, then allocate bits across
transformed coordinates).

## Positioning vs. our thesis

Nearest framing to ours on the *allocation* side: our key/value split is **reverse
water-filling in output-distortion space**. The distinction we draw: they allocate across
transform coordinates for per-vector reconstruction; we allocate across K/V for *output*
distortion (what actually reaches the attention result). Verify details on publication.

## What we borrow / reject

The transform-coding / rate–distortion vocabulary. We restrict distortion to the attention
output, not vector reconstruction.

## Open threads

- Information-theoretic lower bound for allocation under output distortion (vs. reconstruction).
