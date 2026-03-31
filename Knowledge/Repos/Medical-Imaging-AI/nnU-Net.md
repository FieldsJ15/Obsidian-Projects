# nnU-Net

**GitHub:** `MIC-DKFZ/nnUNet` | 8,200+ stars | Gold standard

## What It Is
Self-configuring U-Net. Automatically analyzes your dataset and configures the optimal segmentation pipeline — no manual tuning needed. Has beaten almost every manually designed architecture on every medical segmentation benchmark.

## Why It's the Standard
Traditional U-Net requires tuning: patch size, batch size, architecture depth, augmentation. nnU-Net fingerprints your data and sets all of this automatically. Papers claiming to beat it usually compared against a poorly configured baseline, not nnU-Net properly tuned.

## How It Works
1. **Dataset fingerprint** — analyzes voxel spacing, image size, class distribution
2. **Auto-configuration** — picks 2D, 3D, or cascade network
3. **Training** — 5-fold cross-validation by default
4. **Inference** — test-time augmentation ensemble

## V2 Improvements
- Modular framework (easier to extend)
- Residual Encoder UNet presets
- Better GPU memory scaling

## Important: PyTorch Version
AMP bug in PyTorch 2.9.0 breaks 3D convolutions → **use PyTorch ≤ 2.8.0**

## Install
```bash
pip install nnunetv2
```

## Connects To
- [[MONAI]] (complementary — nnU-Net for performance, MONAI for flexibility)
- [[TotalSegmentator]] (built on nnU-Net)
- [[Medical-Imaging]]
- [[CT]], [[MRI]]
- [[DICOM]]
- [[MLC-Sim]] (dose-painting needs segmentation)

---
*Part of → [[Repos-Index]] > Medical Imaging AI*
