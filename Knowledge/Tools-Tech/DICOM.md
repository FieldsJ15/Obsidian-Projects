# DICOM — Digital Imaging and Communications in Medicine

## What It Is
- Universal standard for medical imaging data
- Every clinical scanner outputs DICOM
- Contains both **pixel data** (the image) and **metadata** (patient, scan params)

## File Structure
- `.dcm` files
- Tags: (Group, Element) — e.g. (0008,0060) = Modality
- Series → Study → Patient hierarchy

## Key Tags
| Tag | Name |
|-----|------|
| (0008,0060) | Modality (CT, MR, PT...) |
| (0028,0030) | Pixel Spacing (mm) |
| (0018,0050) | Slice Thickness |
| (3006,0020) | RT Structure Set (for [[MLC-Sim]]) |
| (300A,00B0) | RT Beam Sequence |

## Python Libraries
- **pydicom** — read/write DICOM
- **SimpleITK** — image processing on DICOM
- **pynetdicom** — DICOM networking

## Viewers
- **3D Slicer** — full featured, free
- **ITK-SNAP** — segmentation focused
- **OHIF Viewer** — web-based
- **Horos / OsiriX** — Mac clinical viewer

## Connects To
- [[Medical-Imaging]]
- [[CT]], [[MRI]], [[PET]], [[SPECT]]
- [[MLC-Sim]] (RT Plan, RT Dose, RT Structure)
- [[3D-Printing-Medicine]] (STL export pipeline)
- [[Python-Biomedical]]

---
*Part of → [[HOME]] > Tools*
