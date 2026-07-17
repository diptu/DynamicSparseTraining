# Readings

Papers ordered by importance to this experiment. Tiers = how deeply to read, not chronology.
**Depth key:** 🔴 master (defend under questioning) · 🟡 working knowledge (implement/discuss) · 🟢 skim (know the claim)

## Tier 1 — The experiment stands on these

| # | Paper | Role here | Depth |
|---|---|---|---|
| 1 | He et al., **Sparse Double Descent** (ICML 2022) | The phenomenon being explained; §2 replicates its exact setup | 🔴 |
| 2 | Curth et al., **A U-Turn on Double Descent** (NeurIPS 2023) | The framing: "wrong axis" critique; this work is its deep-sparse resolution — know precisely where they stop and this starts | 🔴 |
| 3 | Maddox et al., **Rethinking Parameter Counting in Deep Models** (2020) | Primary d_eff definition (D1); source of the α parameter | 🔴 |
| 4 | Evci et al., **Rigging the Lottery: Making All Tickets Winners** (ICML 2020) | The DST method (condition c); reproduction target for the correctness gate | 🔴 |

## Tier 2 — The instrument and its defense

| # | Paper | Role here | Depth |
|---|---|---|---|
| 5 | Yao et al., **PyHessian** (2020) | The measurement tool; must defend Lanczos/Hutchinson estimate reliability | 🔴 |
| 6 | Granziol et al., **Hessian spectrum of deep networks** (2020) | Bulk-vs-outlier structure; explains why D1/D2/D3 can disagree (Risk A defense) | 🟡 |
| 7 | Abbas et al., **effective dimension** (2021) | Alternative d_eff lineage; the descriptive-vs-predictive contrast in §2 of the proposal | 🟡 |

## Tier 3 — Context every conversation assumes

| # | Paper | Role here | Depth |
|---|---|---|---|
| 8 | Belkin et al., **Reconciling modern ML and the bias-variance trade-off** (PNAS 2019) | Origin of double descent; guaranteed interview question | 🟡 |
| 9 | Nakkiran et al., **Deep Double Descent** (ICLR 2020) | Deep-nets DD; source of the label-noise-as-magnifier convention (Risk B defense) | 🟡 |
| 10 | Frankle & Carbin, **The Lottery Ticket Hypothesis** (ICLR 2019) | Shared language of Chen's and Liu's entire programs | 🟡 |
| 11 | Mocanu et al., **SET** (Nature Comm. 2018) | First DST method; justifies choosing RigL over SET | 🟢 |

## Tier 4 — Per-professor slot (read the week of each email)

One recent (2025–26) paper per target, chosen from their newest output — check their pages/arXiv the week of sending, not from memory. Placeholder picks to verify:

| Professor | Start from | Why |
|---|---|---|
| Sijia Liu (MSU) | **BiP: bi-level optimization for pruning** (NeurIPS 2022) + newest 2025–26 pruning-theory paper | d_eff as the quantity a principled pruning objective targets |
| Tianlong Chen (UNC) | Newest sparsity/efficiency paper from his UNC group (2025–26) | Cite current work, not his citation-classics |
| Caiwen Ding (UMN) | Recent algorithm–hardware co-design paper | Frame: d_eff as a design rule for sparsity budgets |
| Anshumali Shrivastava (Rice) | Contextual sparsity / dynamic sparse attention line | Frame: this is the controlled small-scale version of his scale bet |
| Xiaolong Ma (Arizona) | Recent core-DST paper | Purest topical overlap; engage on method details |

## Reading order (calendar)

1. **Weeks 1–2 (with pilot):** #1, #4, #5 — these block implementation
2. **Weeks 3–4 (during Phase 1 runs):** #2, #3, #6 — these block the writeup
3. **Weeks 5–6:** #7–#11 — context layer, notes in `paper_notes/`
4. **October, rolling:** Tier 4, one per outreach email

## Notes discipline

Per paper in `paper_notes/`: (1) core claim in one sentence, (2) what it assumes, (3) what this experiment takes from it, (4) the one question I'd ask the authors. Item 4 doubles as interview prep.
