# TotalSegmentator

**GitHub:** `wasserth/TotalSegmentator`

## What It Is
Pre-trained nnU-Net that segments 117+ anatomical structures from CT/MRI in one command. No training needed — runs out of the box on any clinical CT.

## Structures It Segments
- All major organs (liver, spleen, kidneys, lungs, heart...)
- Bones (vertebrae, ribs, pelvis...)
- Vessels (aorta, pulmonary arteries, coronary arteries in V2)
- Brain structures (V2)
- Muscles

## Trained on
- 1228 CT subjects + 616 MRI subjects
- Multi-institutional → robust to scanner variation

## V2 Additions
- More anatomical classes
- Pulmonary vessels, cerebrovascular, coronary arteries
- Better MRI support

## TotalSegmentator 2D (TS2D)
For fast inference without GPU:
- Projects 3D CT → 2D coronal plane (max/avg intensity projection)
- Sub-second inference
- `risc-mi/totalsegmentator2D`

## Install & Run
```bash
pip install TotalSegmentator
TotalSegmentator -i ct.nii.gz -o segmentations/
```

## Use Cases for Your Work
- Auto-contour for [[MLC-Sim]] radiotherapy planning
- Anatomy atlas for [[3D-Printing-Medicine]]
- Teaching dataset for segmentation models

## Connects To
- [[nnU-Net]] (built on it)
- [[CT]], [[MRI]]
- [[DICOM]]
- [[Medical-Imaging-Software]] (3D Slicer can display output)
- [[MLC-Sim]]

---
*Part of → [[Repos-Index]] > Medical Imaging AI*
