# 20-Week PhD-Readiness Plan — 3h/day (US Fall-2027 application cycle)

**Goal:** by Week 20, [diptu.github.io](https://diptu.github.io/) plus a submitted application package
convince a professor to want you in their group — backed by a **live arXiv preprint**, an **adoptable
open-source artifact (`pip install kvbits`)**, a public multi-pillar repo, demonstrated theory depth
(notes + verifiable coursework), **three secured letters**, and a tailored SOP per program — applied
as a **survivable portfolio** (safety + target + reach), not a wishlist of top-10 labs.

**Stretch goal — put the AMBITIOUS tier within reach:** produce the three things that tier demands
*beyond* the preprint (see "Reading the shortlist" below), so Beidi Chen (CMU) and Tri Dao (Princeton)
become genuine reaches rather than lottery tickets. This is an *upgrade layered on the base plan* — if
research slips, it's the first thing cut, and the safety/target tiers still stand.

**Time budget:** 3h/day × 6 days/week × 20 weeks ≈ **360 focused hours** (1 rest day/week). Each
**Day** is a ~3h block; check it when done.

**This plan absorbs** `todo.md` (the research spine) and `unified.md` (the 3-repo merge) into a daily
cadence, and adds what a US application needs and those don't: math foundations + certificates, the
website overhaul, **application logistics on their real lead times** (letters, tests, transcripts),
SOP/CV, and two outreach waves. Where a day maps to research, the detail lives in `todo.md`.

---

## Calendar anchor (why the dates matter)

| Marker | Date (approx) |
|--------|---------------|
| Week 1 start | **2026-07-13** (today) |
| Week 6 gate — theorem verified | ~2026-08-23 |
| Week 8 — outreach wave 1 | ~2026-09-06 |
| Week 13 — **arXiv v1 live** + Tianlong Chen RA email | ~2026-10-11 |
| Week 16 — **arXiv v2** (differentiated) + `kvbits` released + Beidi/Tri Dao outreach | ~2026-11-01 |
| Week 20 end | **~2026-11-30** |
| US CS PhD deadlines | **Dec 1 – Jan 15** (most cluster Dec 15) |

The plan lands you *at* the deadline window with everything ready. The December batch submits in
Weeks 19–20; any January deadlines submit in the week or two after the plan ends. **Everything with an
external lead time (letters, tests, transcripts) is pulled early on purpose** — see the logistics lane.

## Reading the shortlist (`short-list.md`) — what "within reach" means

The shortlist tiers by **admission probability for this profile**, and it is blunt: 0 safety, 0 target,
2 reach (Tianlong Chen via **RA/visiting side door**, Marculescu direct), 2 ambitious (Beidi Chen, Tri
Dao), 6 closed. Its central warning (Part 4): **applying to ten top-10 labs is not a plan — it's how a
cycle is wasted.** The survivable portfolio is built from tiers this list doesn't yet contain.

Two consequences drive every change below:

**A. Build the real safety + target tiers (this is primary).** Per shortlist Part 3, they exist and
must be created, not relabeled:
- **Safety (3–4):** funded EU / Canada *research-masters* (ETH, EPFL, Max Planck/IMPRS, KTH, TU Delft; Waterloo/UBC/Toronto MSc) — the well-worn route from exactly this profile.
- **Target (4–5):** mid-tier US R1s (ranked ~30–80) with **NSF-funded** efficiency/quantization/serving labs, where your 6 years of production ML/MLOps is a *differentiator*, not an apology.
- **Reach (2):** Tianlong Chen (**RA/visiting — highest-EV action on the list**, H2O co-author, rolling), Marculescu (direct; verify funding first).

**B. Make AMBITIOUS reachable — the differentiator layer.** The tier defines itself: a solid preprint
is *table stakes*, so it can't be the differentiator. What raises the odds (honestly: from ~1–3% toward
the top of reach, not into Target) is producing what the tier actually requires:

| AMBITIOUS demands (shortlist) | In-scope deliverable (respects `CLAUDE.md`) | Weeks |
|---|---|---|
| A result the PI *cares about* | Derived allocation **vs. H2O/SnapKV eviction at equal memory** on the LongBench subsets Beidi uses (comparison, not a combined method); **measured GB saved + tokens/sec** end-to-end for Tri Dao | 13–16 |
| A **widely-adopted OSS artifact** | `pip install kvbits`: auto-derives the allocation on any HF model, one-click Colab demo, clean README (adoptable is in your control; adoption is a lottery — ship it anyway) | 15–17 |
| Direct contact / a **referral** | Two-stage preprint (**v1 W13** → Tianlong Chen RA email → H2O-community bridge; **v2 W16**), then technical outreach to Beidi/Tri Dao with the artifact in hand | 13, 16, 19 |

> Scope guard: `CLAUDE.md` keeps **mixed eviction+quantization out of scope**. Eviction methods appear
> only as *baselines to beat at equal memory*, never as a combined method. The bound, the money plot,
> and the three-way allocation comparison are never cut.

### Target portfolio shape (shortlist Part 4 — apply to this, not a wishlist)

| Tier | Count | Source |
|---|---|---|
| 🟢 Safety | **3–4** | Funded EU / Canada research-masters |
| 🔵 Target | **4–5** | Mid-tier US R1s (rank ~30–80) with funded efficiency labs |
| 🟡 Reach | **2** | Tianlong Chen (RA route), Marculescu |
| 🟠 Ambitious | **1–2** | Beidi Chen and/or Tri Dao — with the differentiator layer |
| 🔴 Closed | **0** | Skip; the fee + hours build the safety tier instead |

## The six gaps this closes (from the profile assessment)

| Profile gap | Closed by | Weeks |
|-------------|-----------|-------|
| No recent output; pubs predate current direction (2018–20) | The arXiv preprint (theorem + benchmark) | 4–16, 19 |
| Thin theoretical depth; no formal math coursework listed | Public math notes **+ 2 verifiable certificates** (linear algebra, convex/info theory) | 1–14 |
| Shallow paper engagement | Literature notes (attention-papers Stages 1–6) + reproductions | 3, 7 |
| No advisor / collaborators / mentorship | Two outreach waves; engaged faculty → possible mentor/letter | 8, 17, 19–20 |
| **Limited letter-of-recommendation prospects** | Deliberate 3-letter campaign (candidates → soft contact → formal ask + brag sheet) | 2, 6, 12, 16, 19 |
| Modest GPA (3.62) for theory-heavy programs | Recent excellence (preprint + notes) + an honest, forward-looking SOP narrative | 17–18 |
| Website doesn't showcase any of it | Full site overhaul | 17 |

## Application logistics lane (parallel track — lead times, not research pace)

These have **external clocks** that don't care about research progress. Start each at "Kick off," hit
"Done by," or applications stall.

| Item | Kick off | Done by | Why the lead time |
|------|----------|---------|-------------------|
| **Letters ×3** — identify candidates | W2 | — | Need 4 candidates to land 3 strong letters |
| Letters — soft re-contact (share `v0.1-lemma`) | W6 | W8 | Writers write better when they've followed the work |
| Letters — **formal ask + brag sheet** | W12 | W13 | Recommenders want 4–6 weeks; asking late = weak/late letters |
| Letters — confirm submitted | W19 | W20 | Follow up; portals show received/not |
| **TOEFL/IELTS** — decide if required per program | W2 | W3 | NSU is English-medium; some programs waive, many don't — check each |
| TOEFL/IELTS — register + take (if needed) | W6 | W11 | Scores take ~10 days to send; must arrive before deadlines |
| **GRE** — decide (target GRE-optional programs) | W2 | W3 | Only prep if a must-have program requires it — protect research time |
| **Transcripts / WES credential eval** (NSU) | W4 | W12 | International transcript + evaluation is slow (4–6 wks) |
| **arXiv v1** (theory + money plot) | W12 | W13 | Needed to attach to the Tianlong Chen RA email |
| **RA / visiting-researcher email — Tianlong Chen** | W13 | W13 | Rolling channel; highest-EV action on the shortlist |
| **Funding search** — mid-tier R1 (30–80) + EU/Canada masters | W10 | W13 | Builds the safety+target tiers the shortlist lacks |
| **arXiv v2** (differentiated) + `kvbits` release | W16 | W17 | The AMBITIOUS-tier artifact; goes in the apps |
| **Program list** — long-list → final portfolio (10–13) | W2 | W13 | Portfolio shape above: 3–4 safety, 4–5 target, 2 reach, 1–2 ambitious |
| **SOP** — master draft → per-program tailoring | W14 | W19 | One master, then per-program versions |
| **CV** — updated with preprint + `kvbits` + repos | W18 | W18 | Export via `/make-pdf` |
| Fee waivers / application fees | W18 | W19 | Some need pre-approval |
| **Submit December batch** | W19 | W20 | Dec 1 / Dec 15 deadlines |

## Definition of done (Week 20)

- [ ] arXiv preprint live (**v1 by W13, v2 by W16**), linked from the site
- [ ] **`kvbits` released** — `pip install`-able, one-click Colab demo, clean README (the adoptable artifact)
- [ ] **Differentiator result**: derived allocation vs. eviction at equal memory (Beidi) + measured GB/tokens-sec (Tri Dao), in v2
- [ ] One public unified repo (Literature · Foundations · Research) that installs + regenerates figures cold
- [ ] Public math notes **+ 2 completed course certificates** demonstrating theory engagement
- [ ] Overhauled website: research result front-and-center, preprint, `kvbits`, repos, notes, clear narrative
- [ ] **3 letter writers secured**, formally asked, briefed, ≥2 confirmed submitted
- [ ] CV + 1-page research statement + SOP master + per-program tailored SOPs
- [ ] **Survivable portfolio finalized** (3–4 safety, 4–5 target, 2 reach, 1–2 ambitious, 0 closed); tests + transcripts en route or received
- [ ] **Tianlong Chen RA/visiting email sent** (W13); Beidi/Tri Dao technical outreach (W16+)
- [ ] **December-deadline batch submitted**; January batch queued; two outreach waves sent; ≥1 substantive faculty conversation opened

## Standing rules

1. **3h is the unit; the day's outcome is the point** — if the block finishes early, pull tomorrow forward.
2. **Week 6 is the only hard research gate** (theorem proven + verified). If the math fails twice, ship the loose bound and proceed — never re-enter.
3. **Logistics beat research when a clock is running.** A letter ask or test registration on its due week *outranks* a research day. Move research, never the logistics deadline.
4. **Ship a public signal early** so outreach wave 1 (W8) and letter re-contact (W6) point at something real. Don't wait for the preprint to start talking to people.
5. **Write while you read.** Math + literature notes go straight to the public site/repo — the notes *are* the theory-depth evidence.
6. **Friday ritual** (Day 6 each week): push; update site/README status; one line in `paper/notes/log.md`; **tick the logistics lane**.
7. **Scope only shrinks** (per `Plan.md`): Qwen → LongBench subsets → per-head → ablations. Never cut the bound, the money plot, or the three-way comparison.
8. **The differentiator layer is the first cut, not the safety net.** The AMBITIOUS upgrade (differentiator experiment, `kvbits` polish, Beidi/Tri Dao outreach) is a *stretch on top of a complete base plan*. If research slips, drop it in this order — extra experiment → OSS polish → v2 timing — and the v1 preprint + RA route + safety/target tiers still deliver a survivable cycle. **Never sacrifice the portfolio (safety+target) for a 1–3% lab.**
9. **Apply to the portfolio, not the wishlist** (shortlist Part 4). Zero closed-tier applications; every top-10 lab you add must be matched by ≥2 safety/target applications already in hand.

## Phase map

| Phase | Weeks | Focus | Milestone |
|-------|-------|-------|-----------|
| 1 · Setup, unify & logistics kickoff | 1–3 | merge repos, instrument, first reproduction, math on-ramp, **letters/tests/programs seeded** | first public signal; logistics started |
| 2 · Theory core | 4–8 | the bound + allocation + literature depth + **outreach wave 1** + soft letter contact + tests booked | `v0.1-lemma`, emails sent |
| 3 · Measure, benchmark & ship v1 | 9–13 | structure, oracle frontier, full comparison + **arXiv v1, Tianlong Chen RA email, funding search, formal letter asks, tests taken** | `v0.2-stats`, `v0.3-results`, **v1 live**, letters in flight |
| 4 · Differentiate & ship v2 | 14–16 | paper + **differentiator experiment** + **`kvbits` release** + **arXiv v2** + Beidi/Tri Dao outreach + SOP master | `v0.4-draft`, **v2 live**, artifact out |
| 5 · Profile & materials | 17–18 | website overhaul + SOP/CV/research statement + per-program tailoring | site + materials ready |
| 6 · Submit & convert | 19–20 | **submit December batch** + outreach wave 2 + letter/score confirmation + follow-through | applications submitted, conversations open |

---

## Five-week achievement checkpoints

Stop at the end of Weeks 5, 10, 15, and 20 and score yourself. Each checkpoint has **one hard line**
(must be true, or fix it before continuing) and a set of verifiable criteria. Rate each:
**🟢 Green** = all criteria met, on track · **🟡 Amber** = hard line met but ≥1 criterion slipped —
apply the recovery move · **🔴 Red** = the hard line failed — stop and recover before the next phase.

| CP | Week | Headline | The one hard line |
|----|------|----------|-------------------|
| 1 | 5 | Foundations laid · theory drafted · logistics seeded | The **allocation corollary exists end-to-end on paper** (`b_K − b_V` derived), even if unverified |
| 2 | 10 | Theorem shipped · outreach live · structure measured | **`v0.1-lemma` tagged** — bound proven *and* numerically verified (or loose bound shipped w/ limitations) |
| 3 | 15 | v1 public · RA door knocked · differentiator done | **arXiv v1 live AND the Tianlong Chen RA email sent** with it |
| 4 | 20 | Shipped & submitted | **December batch submitted** (safety + target first), letters received, ≥1 faculty conversation open |

### 🏁 Checkpoint 1 — Week 5: foundations + theory draft + logistics seeded
> **Hard line:** the allocation corollary `b_K − b_V ≈ log₂(‖q‖·diam(V)/√d) + log₂(r_K/r_V)` is derived on paper. Everything else can be Amber; this cannot.
- [ ] 3 repos merged; fresh clone installs + `pytest` green; KV-cache dump works per layer/head
- [ ] **First public signal:** one reproduction (H2O/SnapKV) shipped with a matching plot (W3)
- [ ] Value-side bound proven (Lemma 1); softmax-Lipschitz chain + amplification factors written; **corollary derived**
- [ ] Logistics seeded: 4 letter candidates listed, program long-list (~20), TOEFL/GRE decided, transcripts/WES ordered
- [ ] Math notes public (Trefethen & Bau, Boyd ch.1–2/5); certificate #1 in progress
- **Recovery if behind:** theory is priority — if instrumentation lags, derive on synthetic q/K/V; if the reproduction stalls, ship the simpler heuristic. **Never touch the logistics clock** (transcripts/tests have external lead times).
- **Evidence a professor sees:** a public repo, a faithful reproduction, and real math notes — proof you've started.

### 🏁 Checkpoint 2 — Week 10: theorem shipped · outreach live · structure measured
> **Hard line (the only hard gate in the plan):** `v0.1-lemma` is tagged — `tests/test_bound.py` passes, or the loose bound is shipped with a limitations note. If the tight bound failed twice, ship loose **now** and never re-enter.
- [ ] `v0.1-lemma` tagged (W6); theorem written up in the report
- [ ] Literature depth: attention-papers Stages 1–4 deep notes public (W7)
- [ ] **Outreach wave 1 sent** (4–6 faculty, W8); letter candidates soft-contacted with the tagged result
- [ ] `stats.py` collecting `‖q‖, r_K, r_V, diam(V)`; K/V spectra stored; `v0.2-stats` tagged (W9)
- [ ] **Predictions pre-registered** — timestamped `b_K − b_V` heatmap committed to README (W9)
- [ ] Oracle frontier + R–D curve; funding search done → candidate portfolio assembled to the target shape
- [ ] TOEFL/GRE taken or firmly scheduled; transcripts/WES in flight
- **Recovery if behind:** the gate outranks everything — if the proof is stuck, adopt the loose bound and move. If outreach slipped, send it this week regardless of research state.
- **Evidence a professor sees:** a *verified* theorem, pre-registered predictions, and a first specific email — signals of a real researcher, not a hobbyist.

### 🏁 Checkpoint 3 — Week 15: v1 public · RA door knocked · differentiator done
> **Hard line:** arXiv v1 is live (or the PDF is posted to the site) **and** the Tianlong Chen RA/visiting email is sent with it — the highest-EV funding action on the shortlist.
- [ ] **arXiv v1 live** (theory + money plot + comparison), linked from the site (W13)
- [ ] Money plot tracks reality; `v0.3-results` frozen (W13)
- [ ] **Portfolio finalized** (10–13 programs, deadlines locked); **formal letter asks sent** with brag sheet (W12); 3 writers accepted
- [ ] **Tianlong Chen RA/visiting email sent** (W13)
- [ ] Differentiator experiment done (W14): equal-memory eviction-vs-allocation comparison + measured GB/tokens-sec
- [ ] `kvbits` built (pip-installable + Colab); `v0.4-draft` tagged (W15); blogs #1–5 published; SOP master v1 drafted
- [ ] Certificate #2 nearly complete
- **Recovery if behind:** the differentiator (W14) is the **first cut** — v1 + the benchmark still carry December. Never let it delay v1 or the letter asks.
- **Evidence a professor sees:** a live preprint, a possibly-open RA conversation, and a usable artifact — you're now above "table stakes."

### 🏁 Checkpoint 4 — Week 20: shipped & submitted
> **Hard line:** the December-deadline batch is submitted (safety + target **first**), letters confirmed received in portals, and ≥1 substantive faculty conversation is open.
- [ ] arXiv v2 live + `kvbits` released publicly; Beidi/Tri Dao technical outreach sent (W16)
- [ ] Website overhauled — result + preprint + `kvbits` front-and-center (W17)
- [ ] CV + 1-page research statement + per-program SOPs done; fee waivers sorted (W18)
- [ ] **December batch submitted**; letters received; scores + transcripts landed (W19–20)
- [ ] Wave-2 outreach sent; **January-deadline programs queued**
- [ ] 2 certificates published; self-audit against all six profile gaps passed
- **Recovery if behind:** submit **safety + target first** (the survivable core); reach/ambitious can slip into January. Never miss a target-tier deadline to polish an ambitious-tier app.
- **Evidence a professor sees:** a complete submitted portfolio, a public body of work, and live conversations — a fundable candidate.

> **Through-line:** every checkpoint converts effort into something *externally visible* — a repo, a
> verified theorem, a live preprint, a submitted portfolio. Funding decisions turn on visible evidence
> of consistent research output, and these four dates are where you prove it exists.

---

## Phase 1 — Setup, unify & logistics kickoff

### Week 1 — Unified public repo + transition narrative
> **Outcome:** three repos merged on a `unify` branch; "why theory now" drafted; website gaps listed.
- [ ] **Day 1** — `unified.md` Phase 0–1: backup branch; subtree-add `attention-papers` + `transformer-from-scratch`; verify histories
- [ ] **Day 2** — `unified.md` Phase 2: reconcile literature — merge bibliographies, migrate KV notes into the taxonomy
- [ ] **Day 3** — `unified.md` Phase 3: `uv` workspace; one `ruff`/`pytest`; both test suites green
- [ ] **Day 4** — Rewrite root README as a 3-pillar portal (1.5h); extend `JOURNEY.md` + draft `ROADMAP.md` (1.5h)
- [ ] **Day 5** — Write the 1-page "why theory now" transition narrative → `docs/applications/` (2h); list every website gap vs. the profile assessment (1h)
- [ ] **Day 6** — Math on-ramp: Trefethen & Bau Lec 1–2, public notes → `docs/literature/notes/math/`; Friday ritual

### Week 2 — Instrument the model + logistics kickoff
> **Outcome:** KV-cache dumping works; fresh clone installs; **letter candidates + program long-list + test decisions made.**
- [ ] **Day 1** — Fresh clone → `uv sync` → `pytest` (both suites); fix any breakage
- [ ] **Day 2** — Pick target model (Llama-3.2-1B); load + generate to confirm GPU/Colab (1.5h); write config yaml + read `quantizers.py` (1.5h)
- [ ] **Day 3** — Forward hook: dump K/V per layer/head to `results/`
- [ ] **Day 4** — Trefethen & Bau Lec 3–5 (SVD, low-rank, Eckart–Young); public notes
- [ ] **Day 5** — **Logistics kickoff (research pauses):** list **4 letter candidates** (NSU faculty you worked under/alongside, a manager, a possible outreach-earned researcher) with why each is credible → `docs/applications/letters.md`; seed a **program long-list of ~20** → `docs/applications/programs/tracker.md`
- [ ] **Day 6** — **Test decisions:** for the long-list, note per-program **TOEFL waiver** eligibility and **GRE** requirement; decide to target **GRE-optional** programs unless a must-have needs it; book nothing yet, just decide; Friday ritual + tick logistics lane

### Week 3 — First public signal: reproduce a heuristic
> **Outcome:** faithful H2O/SnapKV reproduction with a matching plot; blog #1 drafted; test path locked.
- [ ] **Day 1** — Read H2O + SnapKV method sections; pick the simpler; pre-register the target in `research/reproductions/`
- [ ] **Day 2** — Implement attention-score accumulation + the eviction step
- [ ] **Day 3** — Wire it into the generation loop behind a flag; run on one task
- [ ] **Day 4** — Reproduce the paper's headline plot; document match/gap + fidelity rung
- [ ] **Day 5** — Draft blog #1 "instrumenting the KV cache" (2h); **finalize test path**: confirm whether any target needs TOEFL/GRE and, if yes, reserve a test date in the W6–W11 window (1h)
- [ ] **Day 6** — Polish the reproduction README; buffer/catch-up; commit; Friday ritual

## Phase 2 — Theory core

### Week 4 — Value-side bound + QJL + transcript order
> **Outcome:** value-side bound proven; QJL lemma reproduced; **NSU transcripts / WES evaluation ordered.**
- [ ] **Day 1** — Read QJL §1–3 carefully
- [ ] **Day 2** — Reproduce QJL main lemma by hand → `reproductions/qjl/` (2h); numerical variance check (1h)
- [ ] **Day 3** — State + prove the value-side bound (`o = a·V` convex combination) → `theory.tex` Lemma 1
- [ ] **Day 4** — Fill `docs/literature/papers/qjl.md`; stub `paper/main.tex` sections
- [ ] **Day 5** — Math: Boyd *Convex Optimization* ch.1–2 (sets, functions); notes
- [ ] **Day 6** — **Logistics:** order official NSU transcripts; start WES/credential eval if any target requires it (slow — start now); Friday ritual + tick lane

### Week 5 — Key-side bound attempt
> **Outcome:** candidate key-side bound + allocation corollary exist end-to-end.
- [ ] **Day 1** — Softmax-Lipschitz lemma statement; key-perturbation → output-error chain (scratch)
- [ ] **Day 2** — Identify amplification factors (`‖q‖`, `diam(V)`, `1/√d`); write into `theory.tex`
- [ ] **Day 3** — Set up the Lagrangian; derive the closed-form `b_K − b_V` corollary
- [ ] **Day 4** — Implement `bounds.py` (predicted-error formula) + a smoke test
- [ ] **Day 5** — Math: Boyd ch.5 (duality) — the ground under the allocation derivation; notes
- [ ] **Day 6** — Fallback prep (triangle-inequality loose bound); finish blog #2 "why keys need more bits"; Friday ritual

### Week 6 — GATE: theorem proven + verified · `v0.1-lemma` + soft letter contact
> **Outcome (GO/NO-GO):** `tests/test_bound.py` passes and the proof is complete; **letter writers re-contacted.**
- [ ] **Day 1** — Close the proof (tight or loose); finalize the corollary; lock `theory.tex`
- [ ] **Day 2** — `tests/test_bound.py`: random q/K/V generator + quantize (2/3/4-bit) + measured error
- [ ] **Day 3** — Assert measured ≤ bound across widths and many seeds; run `pytest` — **the gate**
- [ ] **Day 4** — If it failed twice: adopt the loose bound + limitations note; else tighten
- [ ] **Day 5** — Tag `v0.1-lemma`; publish blog #1; **soft-contact the 3–4 letter candidates**: a warm note sharing what you're building + the tagged result (no ask yet — just get them following)
- [ ] **Day 6** — Register/confirm TOEFL or GRE date if required; write the theorem up in `docs/reports/main/report.md`; Friday ritual

### Week 7 — Literature depth: the field's whole arc
> **Outcome:** substantive public notes across attention-papers Stages 1–4 (closes the shallow-engagement gap).
- [ ] **Day 1** — Stage 1 Neural Attention (2014–16): Bahdanau + Luong deep notes
- [ ] **Day 2** — Stage 2 Foundations (2017): *Attention Is All You Need* deep note
- [ ] **Day 3** — Stage 3 Efficient Transformers: Linformer / Performer / Reformer / Longformer summaries
- [ ] **Day 4** — Stage 4 Efficient Inference: FlashAttention / PagedAttention notes
- [ ] **Day 5** — Cross-link the taxonomy to `foundations/` implementations; publish the literature site
- [ ] **Day 6** — Math: Cover & Thomas ch.2 (entropy, mutual information); notes; Friday ritual

### Week 8 — Outreach wave 1 + statistics hooks
> **Outcome:** faculty tiered per the shortlist, 4–6 emailed; `stats.py` collecting.
- [ ] **Day 1** — Build the target list **tiered to the portfolio shape** → `tracker.md`: mark the 2 reach (Tianlong Chen — flag as **RA/visiting route**, Marculescu), 1–2 ambitious (Beidi Chen, Tri Dao), and begin scouting **mid-tier R1 (rank 30–80) funded efficiency labs** for the target tier; note each one's relevant recent paper
- [ ] **Day 2** — Shortlist 4–6 for wave 1 (bias toward target-tier PIs who reply — they become letters/advisors); draft personalized emails (one specific sentence each; link repo + blog + `v0.1-lemma`)
- [ ] **Day 3** — Send wave-1 emails; set follow-up reminders; log them (1h); implement `stats.py` hooks (2h)
- [ ] **Day 4** — Run statistics collection; dump to `results/stats/`
- [ ] **Day 5** — SVD of K/V per layer/head; store spectra
- [ ] **Day 6** — Math: Cover & Thomas ch.10 intro (rate–distortion); notes; Friday ritual

## Phase 3 — Measure, benchmark & lock logistics

### Week 9 — Structure + pre-registered predictions · `v0.2-stats`
> **Outcome:** "How compressible is the KV cache?" writeup; predictions committed before validation.
- [ ] **Day 1** — Attention entropy + token-importance concentration metrics
- [ ] **Day 2** — Plot K/V spectra + entropy across depth (`scripts/`)
- [ ] **Day 3** — Write "How compressible is the KV cache, really?" → report
- [ ] **Day 4** — Compute derived allocations (`allocation.py`); predicted `b_K − b_V` heatmap
- [ ] **Day 5** — Sanity-check the story; commit the heatmap to README (timestamped pre-registration) (2h); narrate into `experiments.tex` (1h)
- [ ] **Day 6** — Tag `v0.2-stats`; draft blog #3; Friday ritual

### Week 10 — Oracle frontier + **funding search for safety/target tiers**
> **Outcome:** an oracle compressor + empirical rate–distortion curve; **the safety + target tiers the shortlist lacks now exist as a candidate list.**
- [ ] **Day 1** — Define the oracle objective (min cache s.t. output error ≤ ε)
- [ ] **Day 2** — Implement the token-eviction oracle (greedy, full future knowledge)
- [ ] **Day 3** — Implement the bit-quantization oracle (per-layer budget search)
- [ ] **Day 4** — Validate (recover full output as ε→0); sweep ε; store frontier data + plot the R–D curve
- [ ] **Day 5** — **Logistics — build the missing tiers (shortlist Part 3):** run the funding search on **mid-tier R1s ranked ~30–80** with NSF-funded efficiency/quantization/serving labs (target tier) and on **funded EU/Canada research-masters** (ETH, EPFL, IMPRS, KTH, TU Delft; Waterloo/UBC/Toronto — safety tier) → `tracker.md`
- [ ] **Day 6** — Assemble the **candidate portfolio** to the target shape (3–4 safety, 4–5 target, 2 reach, 1–2 ambitious, 0 closed); for each: deadline, fee, required docs, TOEFL/GRE status, funding model; Friday ritual + tick lane

### Week 11 — KIVI + quantized generation
> **Outcome:** KIVI baseline on the frontier; model generates coherent text at 4-bit KV. (**TOEFL/GRE taken by now if required.**)
- [ ] **Day 1** — Implement KIVI-style quant (per-channel K, per-token V)
- [ ] **Day 2** — Reproduce KIVI baseline PPL → `reproductions/kivi/`; add the point to the R–D plot
- [ ] **Day 3** — Implement `patch.py` (HF attention patching)
- [ ] **Day 4** — Run the model end-to-end at 4-bit KV; confirm coherent text
- [ ] **Day 5** — Update `benchmarks/protocol.md`; draft blog #4 "an oracle lower bound for the KV cache"
- [ ] **Day 6** — **arXiv endorsement — start now** (cs.LG endorsement can take days; v1 posts next week): request/confirm the path; confirm test scores sent; Friday ritual

### Week 12 — The money plot + **formal letter asks** + assemble v1
> **Outcome:** predicted-vs-measured plot that tracks reality; **3 letter writers formally asked**; lean v1 preprint assembling.
- [ ] **Day 1** — `02_bound_vs_measured.py`: predicted vs. measured output error; run across 2/3/4-bit, per layer; commit raw outputs
- [ ] **Day 2** — Plot predicted vs. measured; check the bound tracks (correlation is the bar)
- [ ] **Day 3** — **Assemble v1** (a lean note: lemma + allocation corollary + the money plot + reproduction context) from the report — "write as you go" means this is editing, not drafting
- [ ] **Day 4** — **Logistics (research pauses):** formally ask your **3 confirmed letter writers**. Brag sheet: CV, `v0.1-lemma`/draft link, 3–5 specific bullets, portfolio + deadlines, submission instructions → `docs/applications/letters.md`
- [ ] **Day 5** — Wave-1 follow-ups + refine targets from replies (1.5h); polish v1 abstract/intro (1.5h)
- [ ] **Day 6** — Buffer + Friday ritual

### Week 13 — arXiv v1 live + Tianlong Chen RA email · `v0.3-results`
> **Outcome:** **v1 preprint on arXiv**, three-way comparison frozen, **RA/visiting email sent to Tianlong Chen**, portfolio finalized.
- [ ] **Day 1** — Allocation comparison frozen: WikiText-2 PPL × 3 budgets × 3 schemes + 2 LongBench subsets; add H2O/SnapKV/StreamingLLM/KIVI/derived to the leaderboard vs. the oracle frontier
- [ ] **Day 2** — Fill `RESULTS.md`; commit all raw outputs; fold the comparison into v1; `make figures`; tag `v0.3-results`
- [ ] **Day 3** — **Submit v1 to arXiv** (or post the PDF to the site now if endorsement stalls — don't wait); link from the site
- [ ] **Day 4** — **Email Tianlong Chen re: RA / visiting / externship** (H2O co-author, rolling — the highest-EV action on the shortlist): one specific sentence on how the derived allocation relates to H2O, v1 attached, offer to present it
- [ ] **Day 5** — **Finalize the portfolio (10–13 programs)** to the target shape; lock deadlines; confirm letters accepted
- [ ] **Day 6** — Draft blog #5; Friday ritual

## Phase 4 — Differentiate & ship v2 (the AMBITIOUS layer)

### Week 14 — Differentiator experiment (the result Beidi & Tri Dao care about)
> **Outcome:** two results that make the artifact *unignorable* to the ambitious-tier PIs — in scope (comparison + measurement, no combined method).
- [ ] **Day 1** — **Beidi lever:** design the equal-memory comparison — derived-allocation quantization vs. H2O/SnapKV eviction at matched KV memory on 2 LongBench subsets she uses
- [ ] **Day 2** — Run it; commit raw outputs; the claim to test: allocation-optimal *quantization* is competitive with / beats *eviction* at equal memory
- [ ] **Day 3** — **Tri Dao lever:** instrument end-to-end memory (GB) + throughput (tokens/s) at the derived allocation vs. FP16 KV on a real model + long context
- [ ] **Day 4** — Run the system measurement; commit numbers; note kernel-feasibility honestly (what would need a custom kernel)
- [ ] **Day 5** — Write both results into the paper + report; update `RESULTS.md`
- [ ] **Day 6** — Sanity-check the story; `make figures`; Friday ritual

### Week 15 — `kvbits` OSS release + paper revision + SOP master · `v0.4-draft`
> **Outcome:** an adoptable open-source artifact; submission-ready v2 draft; SOP master; blogs published.
- [ ] **Day 1** — Package `kvbits`: `pip install`-able, `apply_kvbits(model)` auto-derives the allocation on any HF model from measured `‖q‖, r_K, r_V, diam(V)`
- [ ] **Day 2** — One-click **Colab demo** (load model → apply → show GB saved + quality retained) + a clean, honest README (what it does, limits, one figure)
- [ ] **Day 3** — Revision pass on the paper: tighten the argument, fix proof gaps; sharpen title/abstract; publish blog #1–#5 → `docs/blog/published/`
- [ ] **Day 4** — Repo hygiene: docstrings, dead code, verify quickstart + `kvbits` install from a fresh clone
- [ ] **Day 5** — **SOP master v1**: hook · trajectory (industry → theory, "why now") · contribution (the result + artifact) · fit · goals → `docs/applications/sop/`
- [ ] **Day 6** — Cold-reader pass; tag `v0.4-draft`; Friday ritual

### Week 16 — arXiv v2 + release + Beidi/Tri Dao outreach + coursework signal
> **Outcome:** **v2 (differentiated) live**, `kvbits` public, ambitious-tier PIs contacted with the artifact, 2nd certificate done.
- [ ] **Day 1** — Final formatting; **submit arXiv v2** (adds the differentiator results); update the site's preprint link
- [ ] **Day 2** — **Release `kvbits` publicly**: PyPI + repo + a short, non-hyped launch post; submit to relevant lists — adoptable is in your control, adoption is a lottery, ship it anyway
- [ ] **Day 3** — **Technical outreach to Beidi Chen & Tri Dao**: not a cold ask — a specific result. Beidi: the equal-memory eviction-vs-allocation finding + `kvbits`. Tri Dao: the measured memory/throughput + kernel-feasibility note. Reference the open RA conversation with Tianlong Chen if it's live
- [ ] **Day 4** — Finish the **2nd course certificate** (convex opt / info theory); publish both certs + notes on the site
- [ ] **Day 5** — Letter follow-up with the v2 link; confirm test scores + transcripts are en route to each program; resolve gaps
- [ ] **Day 6** — Buffer + Friday ritual

## Phase 5 — Profile & materials

### Week 17 — Website overhaul + outreach wave 2 prep
> **Outcome:** the site showcases result, repos, notes, narrative; wave-2 list ready.
- [ ] **Day 1** — Rebuild the homepage: research vision + the KV-cache result + preprint link front and center
- [ ] **Day 2** — Publications page: add the live v2 preprint; link repo + report; **feature `kvbits`** (install one-liner + Colab badge) as the headline artifact
- [ ] **Day 3** — Research page: the 3 formalized questions + derived-allocation result + the money-plot figure + the equal-memory comparison
- [ ] **Day 4** — Notes page: publish math + literature (Stages 1–6) notes **and the 2 certificates** as theory-depth evidence
- [ ] **Day 5** — Projects page: the unified repo (3 pillars), `kvbits`, foundations, benchmark — each with a crisp pitch; "why theory now" on About; meta/SEO; mobile check
- [ ] **Day 6** — Draft the **wave-2 target list** (target-tier PIs + ambitious-tier follow-ups); Friday ritual

### Week 18 — Application materials + per-program tailoring
> **Outcome:** CV, 1-page research statement, and per-program SOPs drafted; fees/waivers sorted.
- [ ] **Day 1** — Draft the 1-page research statement grounded in the result → `docs/applications/research-statement/`
- [ ] **Day 2** — Update the **CV** (preprint, repos, certificates, skills, transition story); export PDF via `/make-pdf`
- [ ] **Day 3** — Tailor the SOP per program (safety + target first — these carry the cycle; then reach). For the industry→theory bridge, lean on the shortlist's honest framing: 6 yrs production ML/MLOps as a *differentiator* at target-tier labs
- [ ] **Day 4** — Finish SOP tailoring; draft the **RA/visiting cover notes** for the reach tier (Tianlong Chen, and any target PI who invited it)
- [ ] **Day 5** — Apply for fee waivers; confirm each portal's required docs are uploaded/ready
- [ ] **Day 6** — Final voice pass: align SOPs ↔ website ↔ research statement; Friday ritual

## Phase 6 — Submit & convert

### Week 19 — Submit December batch + outreach wave 2
> **Outcome:** Dec-deadline applications submitted; 6–8 more faculty emailed with the preprint.
- [ ] **Day 1** — Submit the earliest-deadline apps **safety + target first** (these are the survivable core); verify each portal shows complete
- [ ] **Day 2** — Confirm **letters received** in each portal; nudge any writer not yet submitted
- [ ] **Day 3** — Submit the reach + 1–2 ambitious apps; double-check test scores + transcripts landed
- [ ] **Day 4** — Wave-2 emails (target-tier PIs + Beidi/Tri Dao follow-up; one specific sentence each; v2 + `kvbits` attached); log them
- [ ] **Day 5** — Follow up the Tianlong Chen RA thread + wave-1; respond substantively to any replies
- [ ] **Day 6** — Buffer + Friday ritual

### Week 20 — Convert, consolidate & queue January
> **Outcome:** December batch fully in; January deadlines queued; conversations open; next cycle planned.
- [ ] **Day 1** — Final submission sweep: every December-deadline app complete, letters in, scores received
- [ ] **Day 2** — Queue the **January-deadline programs**: portals prepped, SOPs tailored, letters routed
- [ ] **Day 3** — For interested faculty: a 1-page "how I'd contribute to your group" proposal
- [ ] **Day 4** — Record a 5-minute walkthrough of the result + repo for outreach
- [ ] **Day 5** — Full self-audit against the six original profile gaps + the logistics lane; fix any remaining
- [ ] **Day 6** — Retro + draft the next cycle (finish January apps, deepen theory, second result); final log entry

---

## After Week 20

The December batch is in and January is queued — but the cycle isn't over. Through December–January:
finish the January-deadline applications, keep faculty correspondence warm (a reply from a professor
is worth more than any single application), and prepare for interviews. **The RA/visiting route with
Tianlong Chen runs on its own clock — keep it alive regardless of the December outcome; it is the
shortlist's highest-EV path and can convert independently of any admissions committee.** A second
result, or `kvbits` gaining real users, strengthens later-deadline apps and interview conversations.

**Hold the realism from the shortlist:** the AMBITIOUS pair (Beidi, Tri Dao) stay ~1–3% even with the
differentiator — they are lottery tickets you can now afford, not the plan. The plan is the safety +
target portfolio plus the RA side door. The repo's log (~20+ Friday entries) and the public journey
are themselves the evidence that you do research consistently — which is what funding and admission
decisions actually turn on.
