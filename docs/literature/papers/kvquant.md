# KVQuant: Towards 10M Context Length LLM Inference with KV Cache Quantization

- **Authors / venue / year:** Hooper, Kim, Mohammadzadeh, Mahoney, Shao, Keutzer, Gholami · arXiv 2024
- **Links:** https://arxiv.org/abs/2401.18079
- **Cite key:** `kvquant2024`
- **Bucket:** Quantization
- **Read status:** to read (Plan Week 4)

## The claim (in one sentence)

Careful per-channel key quantization, pre-RoPE, plus outlier isolation and non-uniform
datatypes, enables very-low-bit KV caches at extreme context lengths.

## Method

Per-channel keys (pre-RoPE), per-token values, non-uniform (sensitivity-weighted)
quantization, sparse outlier handling.

## Positioning vs. our thesis

Maps the **empirical statistics landscape** — which channels are outliers, which layers are
sensitive — that our first-order analysis operates over. Useful as the reality check on what a
first-order (mean-field) bound can and cannot explain: the residual is exactly the
outlier/heavy-tail structure KVQuant handles explicitly.

## What we borrow

The statistics vocabulary (per-channel ranges, layer sensitivity) feeding `stats.py`.

## What we reject / where it stops

Non-uniform datatypes and outlier isolation are orthogonal to allocation; we stay uniform to
isolate the allocation effect.

## Quotable numbers / results

<TODO>

## Open threads

- How much quantization damage does a first-order analysis explain vs. leave to outliers?
