# MLC-Sim (Project)

> Active project. Full notes in `Multi-Leaf Colimator/CLAUDE.md`.

## What It Is
3D/4D Multi-Leaf Collimator simulator for radiotherapy treatment planning.

## Knowledge Connections
- Uses [[CT]] data for patient geometry (HU → tissue density)
- Integrates [[PET]] for tumor metabolic activity
- Implements [[DICOM]] RT Plan standard (RT Plan, RT Dose, RT Structure)
- IEC 61217 coordinate system (see [[Biomedical-Engineering]])
- Dose calculation connects to physics in [[Signal-Processing]]

## Stack
- FastAPI backend + React frontend
- Cornerstone3D for [[Medical-Imaging]] rendering
- [[Python-Biomedical]] (pydicom, numpy)

## Links
- Code: `Multi-Leaf Colimator/` (own GitHub repo: FieldsJ15/MLC-Sim)
- Context: `_context/projects.md`

---
*Part of → [[HOME]] > Projects*
