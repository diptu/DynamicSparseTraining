# Effective Dimension Predicts the Sparse Double Descent Peak

**Working title:** *One Axis to Rule Them All: Collapsing Sparse Double Descent Curves onto Effective Dimension*

**Goal:** A preprint-quality result + targeted professor outreach → fully funded PhD offer, Fall 2027.

---

## 1. Hypothesis

The sparse double descent (SDD) test-error peak is governed by **effective dimension** (measured from the Hessian eigenspectrum), not nominal sparsity.

**Falsifiable prediction:** A dynamic sparse training (DST) network and a statically pruned network at the *same nominal sparsity* have *different* effective dimensions — so their SDD peaks occur at **different nominal sparsities** but the **same effective dimension**. Plotting test error vs. effective dimension collapses both curves onto one.

**Kill condition:** If curves do not collapse within confidence bands under any standard effective-dimension definition, the hypothesis is falsified. (This is a publishable negative result — it would show effective dimension is *not* the governing quantity, contra the parameter-counting literature.)

---

## 2. Positioning: the "right axis" resolution (lit review complete — novelty confirmed)

**The framing that sells this — the "U-Turn" argument:**
- **Curth et al. (2023)** argue that much of "double descent" in classical methods is an *illusion created by plotting against the wrong complexity axis* — unfolding onto the right axis recovers the classical U-curve. They pose the problem; they don't resolve it for deep sparse networks.
- **This experiment is the deep-learning resolution:** nominal sparsity is the wrong axis for SDD; effective dimension is the right one. The curve-collapse test is the direct empirical demonstration.

**Supporting literature:**
- **He et al. (ICML 2022):** established sparse double descent empirically — the phenomenon to be explained.
- **Maddox et al. (2020), Abbas et al. (2021):** effective dimension from the Hessian eigenspectrum as a generalization metric — but used *descriptively* (correlates with generalization), never *predictively* (dictates peak location).
- **Granziol et al. (2020):** Hessian bulk / flatness as general geometric properties — again analysis, not a predictive tool for the SDD phase transition.

**Confirmed gap (lit review, Jul 2026):** no existing work uses effective dimension to predict the SDD peak location, and no one uses the DST-vs-static gap as a controlled test of what governs the peak. Current work in the space is either algorithmic (new pruning/DST methods, e.g. GlobalPru) or geometric-descriptive.

**What elevates this above "metric collector" papers:** most work reports that effective dimension *correlates* with generalization. This posits a **causal mechanism** — effective dimension *dictates* the peak location — with a pre-registered kill condition. Theory → derived prediction → measurement that can disprove it. Physics-of-AI, not "train sparse nets and report numbers."

---

## 3. Known risks and how the design addresses them

### Risk A — Effective dimension is ill-defined and expensive
Multiple non-equivalent definitions exist (eigenvalue-threshold count, trace-based, `Σ λᵢ/(λᵢ+α)`). Estimation on real nets requires stochastic approximation.

**Mitigation:**
- Pre-register **three definitions** (Maddox-style `N_eff(α) = Σ λᵢ/(λᵢ+α)`, spectral-gap count, Hessian trace via Hutchinson) and report all three. Collapse under ≥1 pre-registered definition with the others reported honestly = credible; cherry-picking after the fact = not.
- Use **PyHessian** (Lanczos + Hutchinson, designed for exactly this) — spectral density on ResNet-scale nets is feasible on a single GPU.
- Quantify estimator noise: repeat estimation with k random probe vectors, report CIs.

### Risk B — SDD needs label noise (artificial regime)
Peaks are most visible with 10–20% symmetric label noise.

**Mitigation:** Run the noise level as a controlled axis {0%, 10%, 20%}. If collapse holds *across* noise levels, that strengthens the claim; if it only holds under noise, say so explicitly. Framing: label noise is the standard magnifying glass for interpolation-threshold phenomena (same as in the original deep double descent work), not a bug.

### Risk C — DST vs. static pruning differ in more than effective dimension
Mask exploration, training dynamics, and implicit regularization are confounded. A failed collapse wouldn't cleanly falsify the theory.

**Mitigation — third and fourth conditions:**
1. **Static random pruning** (no magnitude criterion) — different mask structure, removes magnitude-pruning bias.
2. **DST with frozen final mask retrained from scratch** — isolates the *mask* from the *dynamics*. If effective dimension is the governing quantity, this condition should land on the same collapsed curve as its parent DST run.

With four conditions, either the curves collapse (strong positive) or the *pattern of failure* localizes what else matters (still a finding).

---

## 4. Experimental design

**Scale (deliberately small — this must run on free/cheap compute):**

| Axis | Values |
|---|---|
| Dataset | CIFAR-10 (CIFAR-100 as robustness check if time permits) |
| Architecture | ResNet-18 (standard for SDD replication) |
| Sparsity levels | ~10 points, log-spaced, 50%→99.5% (dense around the expected peak) |
| Methods | Static magnitude prune, static random prune, DST (RigL or SET), DST-mask-retrain |
| Label noise | 0%, 10%, 20% |
| Seeds | 3 per cell |

**Measurements per trained model:** test error, train error (confirm interpolation), Hessian eigenspectrum via PyHessian (top-k eigenvalues + trace + spectral density), all three effective-dimension definitions.

**Analysis:** For each method, locate peak in (nominal sparsity, test error) space. Then re-plot all methods in (effective dimension, test error) space. Success metric: peak locations align in effective-dimension coordinates within seed-level confidence intervals. Quantify with peak-location distance ratio (spread in eff-dim coords ÷ spread in nominal-sparsity coords) — a number reviewers can grab.

**Compute budget:** ~360 training runs of ResNet-18/CIFAR-10 (~1 GPU-hr each on a T4/A10). Phased: Phase 1 (core 2 methods × 1 noise level × 10 sparsities × 3 seeds = 60 runs) is a Colab Pro / Kaggle / GSU-cluster-sized job. Phase 2 expands only if Phase 1 shows signal.

---

## 5. Timeline (today → Fall 2027 offer)

| When | What |
|---|---|
| **Jul 2026** | **Pre-register the experimental plan** (§7): hypotheses, all four conditions, three effective-dim definitions, kill condition — on OSF (or a timestamped public GitHub repo/wiki). Do this *before* the first training run. |
| **Jul–Aug 2026** | Replicate He et al. SDD baseline. Get PyHessian pipeline working. Phase 1 runs. |
| **Sep 2026** | Analysis, first collapse plot. Write 4–6 page workshop-style writeup + arXiv preprint (even preliminary). |
| **Oct 2026** | **Cold outreach to the 5 professors below** — this is the peak window: after summer, before their inboxes flood with generic Dec applicants. Attach the preprint + one killer figure. |
| **Nov 2026** | Follow-ups, Zoom calls with responders. Incorporate their feedback into Phase 2 runs — instant advisor-fit signal. |
| **Dec 2026** | Applications due (UNC ~Dec 10, MSU/UMN/Rice typically Dec 1–15 — verify each). Named professor in SOP, ideally after having spoken with them. |
| **Jan–Mar 2027** | Interviews. Phase 2 / CIFAR-100 results as fresh material to discuss. |
| **Spring 2027** | Offers. Funded PhD = RA/TA/fellowship; a professor who wants you *is* the funding at these schools. |

The critical path is **preliminary results by end of September**. Everything downstream depends on the outreach email containing a figure, not a promise.

---

## 6. Target professors and per-professor framing

The proposal core stays identical; the *emphasis paragraph* in each email changes.

### 1. Tianlong Chen — UNC Chapel Hill (QS #140) — **Priority 1**
- **Why him:** Sparsity/lottery-ticket work is his core identity; heavily funded (Meta ×3, Amazon ×2, Cisco ×4, IBM, NIH); actively recruiting PhD students.
- **Angle:** Frame as extending the lottery-ticket/sparsity research program with a *theory-first* falsifiable experiment — the effective-dimension lens as a unifying explanation for when sparse subnetworks match dense performance. Cite his sparsity papers specifically.
- **Hook line:** "Your work established *that* sparse subnetworks generalize; this experiment tests *what quantity governs when* they stop."

### 2. Sijia Liu — Michigan State (QS #161) — **Priority 1**
- **Why him:** Directly works on the *theory* of pruning and LTH (bi-level optimization for pruning); NSF CAREER 2024, ARO, Cisco, MIT-IBM Watson affiliate.
- **Angle:** Lead with the theoretical claim and the falsification structure — he's the most theory-oriented of the five. The bi-level-optimization connection: effective dimension as the quantity a principled pruning objective should target. Cite Curth et al. explicitly — the "wrong axis" critique is exactly the kind of foundational question theory people care about.
- **Hook line:** the pre-registered kill condition (§1) — and state explicitly that you'll **publish the negative result if the hypothesis fails**. Willingness to be wrong in public signals scientific maturity over number-chasing; this lands hardest with him.

### 3. Caiwen Ding — Minnesota (QS ~150s)
- **Why him:** Algorithm–hardware co-design of sparse ML; explicitly recruiting with full financial support; NSF CAREER 2024, 24+ grants.
- **Angle:** Systems/efficiency framing — if effective dimension predicts the safe sparsity ceiling, it becomes a *design rule* for hardware-aware sparsity budgets rather than trial-and-error. Lead with execution credibility: a theory-only pitch from a student is risky, but a theory-driven pitch backed by a production-grade evaluation pipeline (PyHessian + your CI/CD, AWS, LLM-eval infrastructure track record) is exactly what co-design labs need — students who can get things to work.
- **Hook line:** "A predictive rule for how sparse you can go before the accuracy cliff — measured, not guessed."

### 4. Anshumali Shrivastava — Rice (QS ~140s)
- **Why him:** SLIDE, contextual sparsity for LLMs, dynamic sparse attention; large-scale ML focus.
- **Caveat first:** Meta Superintelligence Labs affiliation — **verify advising bandwidth before investing** (check his page for "recruiting" language, or ask directly in email #1; a fast no is fine).
- **Angle:** Scale trajectory — CIFAR/ResNet is the controlled testbed, but the question "what governs the sparsity ceiling" is exactly the contextual-sparsity-for-LLMs question. Position the experiment as the rigorous small-scale version of what his group bets on at scale.

### 5. Flex pick — outside the QS 100–200 band
Since the band constraint is soft, add **one** of the pure-DST cluster as a fifth email:
- **Xiaolong Ma (U Arizona)** — core DST publications, NSF panelist, recently +$640K funding → likely has open funded slots. **Best default choice:** funding recency + core-DST fit.
- Alternatives: Yanzhi Wang (Northeastern), Geng Yuan (UGA); Zhangyang "Atlas" Wang (UT Austin, ~top 70) is the reach — worth one email since the marginal cost is near zero and he's *the* lottery-ticket figure.

**Outreach mechanics:** ≤150-word email, one attached figure (the collapse plot), preprint link, **link to the pre-registered plan** ("pre-registered on OSF before the first run" is a one-clause credibility bomb), one sentence of specific engagement with *their* paper, one clear ask ("are you taking funded PhD students for Fall 2027?"). No CV wall-of-text — link it.

---

## 7. Pre-registration (do this before the first training run)

**Status of novelty check: ✅ complete (Jul 2026).** Gap confirmed — no existing work uses effective dimension predictively for SDD peak location, or the DST-vs-static gap as a controlled test (see §2). One residual watch item: recheck OpenReview around ICLR 2027 submission time and monitor the target labs' arXiv output monthly; if something appears, the mask-retrain ablation (§3 Risk C) is the fallback novelty.

**Pre-registration protocol (OSF, or a timestamped public GitHub repo):**
1. **Hypotheses:** primary (curves collapse in effective-dim coordinates) and the explicit kill condition.
2. **All four conditions:** static magnitude, static random, DST (RigL/SET), DST-mask-retrain.
3. **All three effective-dim definitions**, named in advance, with the commitment to report all three regardless of outcome.
4. **Success metric:** peak-location distance ratio, defined before seeing data.
5. **Noise levels, sparsity grid, seeds** — the full §4 table, frozen.

This costs half a day and converts "student with an idea" into "researcher running a pre-registered study." It also inoculates against the cherry-picking critique in §3 Risk A — the definitions were fixed before the data existed, provably.

---

## 8. Deliverables checklist

- [x] Novelty check complete — gap confirmed (Jul 2026)
- [ ] Pre-registered plan live on OSF/GitHub (before first run)
- [ ] SDD baseline replicated (He et al. setup)
- [ ] PyHessian pipeline validated (CI-quantified effective-dim estimates)
- [ ] Phase 1 runs done (60 runs)
- [ ] The Figure: test error vs. nominal sparsity (messy) side-by-side with test error vs. effective dimension (collapsed)
- [ ] arXiv preprint (4–6 pages + appendix)
- [ ] 5 personalized outreach emails drafted
- [ ] Applications submitted by early Dec 2026 with professor named in each SOP
