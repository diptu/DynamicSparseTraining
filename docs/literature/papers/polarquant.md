# PolarQuant

- **Authors / venue / year:** TODO · AISTATS 2026
- **Links:** TODO
- **Cite key:** `polarquant2026`
- **Bucket:** Rotation / transform
- **Read status:** to read

## The claim (in one sentence)

Rotation plus residual correction pushes KV quantization near the information-theoretic limit.

## Positioning vs. our thesis

**Orthogonal knob.** Rotation equalizes variance *within* vectors; our allocation exploits
asymmetry *between* components (K vs. V, layer vs. layer). The two compose — the natural sequel,
explicitly out of scope for our paper and logged as future work.

## What we borrow / reject

Out of scope; cited as related/future work only. Verify authors, title, and link on publication.

## Open threads

- Allocation *after* variance equalization: is the derived gap smaller post-rotation?
