# MONAI — Medical Open Network for AI

**GitHub:** `Project-MONAI/MONAI` | 6K+ stars | NVIDIA + King's College London

## What It Is
PyTorch medical imaging framework. Where nnU-Net is a fixed pipeline optimized for performance, MONAI is a modular toolkit for building custom pipelines. Use both: nnU-Net for baseline, MONAI for custom architectures.

## Key Components
- **Transforms** — 3D spatial augmentations (rotation, zoom, elastic deformation, intensity)
- **Networks** — UNet, SegResNet, DynUNet, SwinUNETR (Transformer-based)
- **Losses** — Dice, Focal, DiceCE (handles class imbalance)
- **Metrics** — Dice, HD95, surface distance
- **Auto3DSeg** — AutoML for 3D medical segmentation

## When to Use vs nnU-Net
| Task | Use |
|------|-----|
| Best baseline, standard dataset | [[nnU-Net]] |
| Custom architecture research | MONAI |
| Production ML pipeline | MONAI |
| Multi-task (seg + classification) | MONAI |

## Install
```bash
pip install monai
```

## Quickstart
```python
from monai.networks.nets import UNet
model = UNet(spatial_dims=3, in_channels=1, out_channels=2,
             channels=(16,32,64,128,256), strides=(2,2,2,2))
```

## Connects To
- [[nnU-Net]]
- [[TotalSegmentator]]
- [[Medical-Imaging]]
- [[CT]], [[MRI]]
- [[Python-Biomedical]]

---
*Part of → [[Repos-Index]] > Medical Imaging AI*
