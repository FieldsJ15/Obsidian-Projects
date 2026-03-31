# Multi-Leaf Colimator (MLC-Sim) — Project Instructions

> Inherits global rules from root `CLAUDE.md`. This file adds project-specific context.

---

## What This Project Is

**MLC-Sim** — a full 3D/4D simulation and visualization system for radiotherapy treatment planning. Implements IEC 61217 coordinate standard, DICOM RT Plan parsing, and multi-viewport clinical interface.

**Current state:** Core features implemented. Several features in development (see below).

---

## Architecture

```
Multi-Leaf Colimator/
├── run.bat                    ← Windows quick start (double-click)
├── mlc_schema.yaml            ← Data schema
├── mlc_sim/                   ← Python backend package
│   ├── physics/               ← IEC 61217, 4D dose, ray-casting
│   ├── io/                    ← DICOM RT Plan parser
│   ├── data/                  ← Data pipeline, DICOM loader
│   └── api/                   ← FastAPI backend (port 8000)
├── web/                       ← React frontend (port 5173)
│   └── src/
│       ├── components/        ← UI components
│       ├── pages/             ← App pages
│       ├── store/             ← Zustand state management
│       └── core/              ← IEC 61217, volume loaders
├── scripts/
│   ├── start_full_app.py      ← Full app launcher
│   └── start_server.py        ← Backend only
└── docs/
    ├── FOLHA_TECNICA_CODIGO.md← Architecture, modules, data contracts
    └── STUDY_LOADING_GUIDE.md ← How to load DICOM studies
```

---

## Stack

| Layer | Tech |
|-------|------|
| Backend | Python + FastAPI (port 8000) |
| Frontend | React + Zustand + Cornerstone3D (port 5173) |
| 3D Rendering | Cornerstone3D, vtk.js |
| Standards | IEC 61217, DICOM RT Plan |
| Start | `run.bat` (Windows) |

---

## Key Pages

| URL | Page |
|-----|------|
| `localhost:5173` | Dashboard |
| `localhost:5173/viewer` | 3D/4D viewer (MPR: Axial, Sagittal, Coronal) |
| `localhost:5173/cockpit` | Full treatment cockpit (3x3 grid, BEV, timeline) |
| `localhost:8000/docs` | FastAPI auto-docs |

---

## Implemented vs In Development

**Done:**
- IEC 61217 coordinate system (gantry CW positive, collimator CCW positive)
- DICOM RT Plan parser with monotonicity validation
- 3D visualization (CT, Dose, PET) with Cornerstone3D
- 4D visualization (accumulated dose, treatment timeline)
- BEV (Beam's Eye View) synced with 3D view
- MLC projection with SAD/SCD magnification factor
- SLERP interpolation for rotations, LERP for positions
- REST API for study loading (ResearchTPS schema)

**In development:**
- Multi-FrameOfReference registration
- Automated UI regression tests
- GPU optimization for ray-casting
- WCAG 2.1 AA compliance

---

## Key Rules for This Project

1. **Coordinate system is sacred** — IEC 61217 conventions must never be changed without updating `docs/FOLHA_TECNICA_CODIGO.md`.
2. **Design system:** Use the defined color palette (neutral whites/grays, `#2563EB` accent only for primary actions). No emojis in UI.
3. **State management** lives in `web/src/store/` via Zustand — don't add local state to components for shared data.
4. **API contracts** are documented in `docs/FOLHA_TECNICA_CODIGO.md` — update there if endpoints change.

---

## Running the App

```bash
# Windows — double-click or:
run.bat

# Backend only:
python scripts/start_server.py

# If port conflict:
python scripts/start_server.py --port 8001
```

---

## Changelog

### 2026-03-31
- Added `CLAUDE.md` to project (Claude Code integration)
