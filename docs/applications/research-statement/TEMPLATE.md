<!-- Research statement (1–2 pages). One core version, lightly adapted per program.
     This is the intellectual spine of the application — write it first. -->

# Research Statement — Nazmul Alam Diptu

## Opening: the question I work on

<Two or three sentences. The problem that motivates you, stated so a non-specialist committee
member gets it. For this repo: memory is the bottleneck of long-context LLMs, and we don't yet
understand — theoretically — where the bits should go when we compress the KV cache.>

## What I've done

<Your strongest evidence, concretely. Lead with the result.>

- **A derived, not tuned, bit allocation.** Prior KV-quantization schemes give keys more bits
  than values by hand. I showed the asymmetry follows from a first-order perturbation bound on
  the attention output, and derived a closed-form optimal gap measurable per layer and head.
- **Validated end to end.** <Bound-vs-measured plot; three-way comparison; the numbers.>
- **Done in the open.** A public, reproducible repository documenting the full journey — literature
  review, reproductions, a benchmark, the paper, and this narrative — sustained over <N> weeks.

## How I think about research

<What this project reveals about your taste: narrow scope held deliberately, pre-registered
predictions, a real loose bound over a stuck elegant one, reproducibility as a hard requirement.
Committees read for judgment, not just results.>

## What I want to do next

<The natural sequels — composition with rotations, outlier-aware bounds, information-theoretic
lower bounds under output distortion. Show the current work opens a program, not a dead end.>

## Why this program / advisor

<Adapt per program. Name faculty and tie to their actual work — the same specificity as a good
cold email. Keep a per-program note in `../programs/<school>.md`.>
