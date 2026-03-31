# MedSAM — Segment Anything for Medical Images

**GitHub:** `bowang-lab/MedSAM`

## What It Is
Meta's Segment Anything Model (SAM) fine-tuned on massive medical imaging datasets. Lets you segment anything in CT/MRI/X-ray with a click or bounding box — no training needed for your specific task.

## Two Modes
- **Everything Mode** — auto-generates masks across the whole image (grid sampling)
- **Prompt Mode** — you draw a bounding box or click → model segments that structure

## Architecture
- ViT (Vision Transformer) image encoder — heavy, runs once per image
- Lightweight prompt encoder — real-time
- Mask decoder — fast

## MedSAM2 + nnU-Net Hybrid
Best current approach for difficult tasks:
- Hiera encoder from MedSAM2 + nnU-Net pipeline
- Better boundary localization
- Handles extreme class imbalance (e.g. tiny brain vessels = <5% of volume)
- Reduces HD95 significantly vs standalone models

## SAM-UNet
- Parallel CNN branch alongside frozen ViT
- Local + global features
- SOTA on SA-Med2D-16M (largest 2D medical segmentation dataset)
- `Hhankyangg/sam-unet`

## Use Cases for Your Work
- Interactive segmentation for [[MLC-Sim]] structure delineation
- Quick prototyping without labeled training data
- Combined with [[TotalSegmentator]] for verification

## Connects To
- [[nnU-Net]] (hybrid architectures)
- [[MONAI]]
- [[Medical-Imaging]]
- [[CT]], [[MRI]]

---
*Part of → [[Repos-Index]] > Medical Imaging AI*
