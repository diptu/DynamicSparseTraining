# Pre-registration — Sparse On-Device Adaptation for Crop Screening Under Drift

*Frozen before the first adaptation run. Amendments are logged with date + reason at the bottom; the original hypotheses are never edited in place.*

## 1. Question

In a low-connectivity deployment, can a compressed crop-disease classifier recover accuracy lost to distribution drift by adapting **on-device**, **without labels**, and by updating only a **sparse subset** of its parameters within a fixed edge budget?

## 2. Primary hypothesis (H1)

Label-free sparse on-device adaptation recovers a **recovery ratio ≥ 0.30** — i.e. closes at least 30% of the `frozen → cloud-oracle` accuracy gap — averaged across the pre-registered drift types, while its per-update memory footprint stays within the target tier's budget.

## 3. Secondary hypotheses

- **H2 (stability):** Under the streaming protocol, the sparse-update method never drops below the frozen baseline accuracy at any checkpoint (no net-harmful adaptation).
- **H3 (sparsity efficiency):** Updating a selected sparse subset (k ≤ 25% of adaptable params) reaches ≥ 90% of the recovery achieved by full-parameter adaptation, at a fraction of the memory cost.
- **H4 (safety):** An entropy/energy-based abstention gate improves selective accuracy (accuracy on non-abstained samples) versus no gate, under drift.

## 4. Kill condition (falsification)

H1 is falsified if **either** of the following holds after Phase 1 + Phase 2:

1. Mean recovery ratio across all drift types is **< 0.30**, **or**
2. The sparse-update method drops **below** the frozen baseline at **any** checkpoint of the streaming protocol.

A falsified H1 is written up and released as a negative result. No re-specification of H1 after seeing results.

## 5. Fixed experimental variables

| Variable        | Setting                                                                                              |
| --------------- | --------------------------------------------------------------------------------------------------- |
| Source dataset  | PlantVillage (lab), fixed train/val split (seed-fixed)                                               |
| Drift datasets  | (a) PlantDoc, (b) Cassava Leaf Disease, (c) synthetic-corruption suite over PlantVillage test set   |
| Backbones       | MobileNetV2-0.35, MCUNet — both int8                                                                 |
| Edge tiers      | MCU (≤ 256 KB train mem) · cheap-device (Pi Zero 2 W / low-end Android)                              |
| Seeds           | {0, 1, 2}                                                                                            |
| Class mapping   | Restricted to disease classes shared across source and each drift target (documented in `configs/`) |

## 6. Conditions (adaptation methods)

1. **Frozen** — no adaptation (lower bound).
2. **BN-recal** — recompute BatchNorm running statistics on unlabeled target stream.
3. **TENT** — entropy minimisation, BatchNorm affine params only.
4. **Sparse on-device update (core)** — self-supervised objective; update only a selected sparse parameter subset (selection rule pre-registered in `configs/sparse_select.yaml`).
5. **Pseudo-label self-training** — confidence-thresholded self-labels.
6. **Cloud oracle** — full supervised retrain on labelled target (upper bound; not deployable).

Selection rule for condition 4 is fixed in advance (e.g. gradient-magnitude top-k on a held-out warmup batch) and not tuned on the drift test sets.

## 7. Metrics (pre-specified)

- **Primary:** recovery ratio `(adapted − frozen) / (oracle − frozen)`.
- Accuracy under drift (top-1).
- Per-update: peak RAM, FLOPs, latency, estimated energy — measured on the target tier.
- Streaming trajectory: accuracy at fixed checkpoints; min accuracy over the stream.
- Calibration (ECE); selective accuracy vs. coverage for the abstention gate.

## 8. Analysis plan

- Report mean ± CI over 3 seeds for every cell.
- H1 decided on the mean recovery ratio across the three drift types.
- H3 tested by sweeping k ∈ {5, 10, 25, 50, 100}% and comparing recovery vs. memory.
- No dataset, class set, budget, or metric is added after unblinding.

## 9. Compute & scope

Phase 1 (batch, all conditions × backbones × drift types × 3 seeds) is the minimum publishable unit. Phase 2 (streaming stability) extends the core condition only. Hardware profiling done on one physical device per tier.

---

### Amendment log

*(date — what changed — why. Original section text above is never edited.)*
