# MARLIN-X Model Card: Look-Alike-Aware SAR Oil Slick Segmentation Model
## Model Details & Scientific Provenance Audit

> **Model Architecture:** Dual-Pol SAR U-Net + Look-Alike Classification Head  
> **Version:** 1.0.0-PROTOTYPE (SIH 2026 / NTRO SIH26143)  
> **Model Audit Status:** `UNVALIDATED BASELINE / DEMO CHECKPOINT`  
> **Primary Sensor Inputs:** Sentinel-1 C-band SAR (IW GRD, VV + VH dual polarization backscatter in dB)

---

### 1. Model Summary & Core Philosophy

The MARLIN-X SAR Oil Slick Model is a modular segmentation and classification engine designed to detect marine oil spills from satellite Synthetic Aperture Radar (SAR) imagery while accounting for environmental look-alikes.

Unlike binary classifiers that label every dark SAR patch as oil, this model architecture outputs a multi-class probability distribution:
1. **Probable Oil Slick**
2. **Environmental Look-alike (Low Wind Zone)**
3. **Environmental Look-alike (Biogenic Film / Algal Bloom)**
4. **Uncertain / Human Review Required**

> [!IMPORTANT]
> **Scientific Guardrail:**  
> **SAR dark features may have non-oil causes.** A dark region in a SAR scene indicates microwave backscatter damping (reduced ocean surface roughness) but does NOT automatically prove chemical oil contamination.

---

### 2. Model Audit & Validation Status

| Audit Checklist Item | Verification Status | Explanation |
| :--- | :---: | :--- |
| **Trained Checkpoint Exists** | **DEMO BASELINE ONLY** | Checkpoint `ml/models/weights/sar_unet_v1.pt` is a random initialization baseline saved after a 1-step synthetic execution test. |
| **Real Training Dataset Used** | **NO** | No real satellite SAR scenes (e.g. Sentinel-1 GRD TIFFs) are stored in `ml/datasets/` yet. |
| **Held-Out Test Evaluation** | **NOT YET VALIDATED** | Quantitative metrics (IoU, Dice, Precision, Recall) are **N/A** until evaluation on real ground-truth callsets is performed. |
| **Inference Provenance** | **SIMULATED** | Pipeline outputs are generated using synthetic arrays for demonstration (`MARLIN-X-DEMO-001`). |

---

### 3. Neural Architecture Specifications

- **Encoder-Decoder Backbone**: 4-level U-Net with batch normalization and ReLU activations.
- **Input Channels**: 2 channels ($\text{VV}_{\text{dB}}$ and $\text{VH}_{\text{dB}}$ backscatter).
- **Classification Head**: Global Average Pooling over bottleneck feature maps ($128 \rightarrow 64 \rightarrow 4$) with Softmax activation.
- **Output Mask**: Single-channel Sigmoid probability map ($H \times W$) for spatial segmentation.

---

### 4. Corrected Evaluation Metrics

> [!WARNING]  
> **MODEL NOT YET VALIDATED ON REAL SATELLITE DATASET.**  
> Previous placeholder metrics (e.g. $\text{IoU}=0.842, \text{Dice}=0.914$) were illustrative placeholders and have been **REMOVED** in accordance with scientific integrity guidelines.

| Metric | Measured Value | Validation Status |
| :--- | :---: | :--- |
| **IoU (Intersection over Union)** | **N/A** | Model Not Yet Validated |
| **Dice Coefficient / F1** | **N/A** | Model Not Yet Validated |
| **Precision** | **N/A** | Model Not Yet Validated |
| **Recall** | **N/A** | Model Not Yet Validated |

---

### 5. Ethical & Legal Disclaimer

- The MARLIN-X model outputs **investigative leads and probabilistic physical compatibility**, NOT legal proof of pollution source or criminal liability.
- All high-priority detections require multi-evidence verification (Lagrangian hindcasting, AIS integrity analysis, and human expert review).
