---
title: "Why Keys Need More Bits Than Values"
date: 2026-07-13
author: Nazmul Alam Diptu
tags: [kv-cache, quantization, transformers, attention]
status: draft
summary: "Value error passes through attention gently; key error amplifies inside the softmax — and you can compute exactly how much more."
---

# Why Keys Need More Bits Than Values

<!-- OUTLINE — flesh out alongside Plan Weeks 1–3. -->

When you quantize a transformer's KV cache, keys and values are not equally fragile. Nearly every
production scheme quietly gives keys more bits than values. This post is about *why* that's not a
heuristic — it falls out of one line of algebra — and how much more, exactly.

## The setup

<KV cache = the memory bottleneck of long-context inference. Quantize it to save memory. But by
how many bits, and split how between keys and values? Today that split is hand-tuned.>

## The idea

<Two mechanisms, one gentle and one violent:>

- **Values are gentle.** The attention output is a weighted average of value vectors, and the
  weights sum to one: `o = a·V`. Perturb the values and the error passes through *at most
  linearly* — averaging can't amplify.
- **Keys are violent.** Keys live *inside* the softmax. Perturb a key and the error is scaled by
  the query norm, bent through the exponential, and then scaled again by how spread out the
  values are. That's amplification.

<Then: the punchline formula, in words — the optimal bit gap is the log of (query norm × value
spread / √d) plus the log of the key/value range ratio. Every term is measurable on a running
model, so the gap is a *prediction*, not a knob.>

## Why it matters

<Same average memory budget, better quality — by spending bits where they're fragile instead of
splitting evenly. And no per-model tuning, because the split is computed from statistics you can
read off the model in one forward pass.>

## Going deeper

- The full derivation and proofs: [technical report](../../reports/main/report.md) · [paper](../../../paper/)
- The bound and allocation rule in code: [`src/kvbits/`](../../../src/kvbits/)
- Where this sits in the field: [literature review](../../literature/)
