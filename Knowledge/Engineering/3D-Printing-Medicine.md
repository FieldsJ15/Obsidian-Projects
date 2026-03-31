# 3D Printing in Medicine

## Technologies
- **FDM** — Fused Deposition Modeling (cheap, basic)
- **SLA/DLP** — Resin (high resolution, surgical models)
- **SLS** — Selective Laser Sintering (functional parts)
- **Bioprinting** — living cells + scaffold (research)

## Clinical Applications
- **Surgical planning models** — 3D print from [[CT]]/[[MRI]] DICOM data
- **Custom implants** — cranial plates, orthopedic
- **Prosthetics** — affordable custom limbs
- **Medical education** — anatomical models
- **Drug delivery** — custom pill geometries
- **Radiotherapy** — custom bolus, phantoms → [[MLC-Sim]]

## Workflow: Imaging → Print
1. Acquire [[CT]] or [[MRI]] scan ([[DICOM]])
2. Segment anatomy (3D Slicer, ITK-SNAP) → [[Medical-Imaging-Software]]
3. Export STL
4. Slice (PrusaSlicer, Chitubox)
5. Print → post-process

## Materials
- PLA, PETG — anatomical models
- Resin — high-detail surgical guides
- TPU — flexible implants
- PEEK — implants (biocompatible, strong)

## Connects To
- [[Medical-Imaging]] (source data)
- [[DICOM]] (input format)
- [[Biomedical-Engineering]]
- [[MLC-Sim]] (custom phantoms)

---
*Part of → [[HOME]] > [[Biomedical-Engineering]]*
