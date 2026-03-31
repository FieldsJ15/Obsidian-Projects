# Agents-Tribunal — Project Instructions

> Inherits global rules from root `CLAUDE.md`. This file adds project-specific context.

---

## What This Project Is

An MCP (Model Context Protocol) server called **Biomed-Slide-Agent** that powers a multi-agent tribunal for processing biomedical PDFs (radioterapia slides, medical documents).

**Current state:** Fully configured and working. The server is ready to process PDFs.

---

## Architecture

```
Agents-Tribunal/
├── server.py                  ← MCP server entry point (Biomed-Slide-Agent)
├── mcp.json                   ← MCP config
├── requirements.txt           ← Python deps
├── .venv/                     ← Virtual environment
└── docs/
    ├── COMECE_AQUI.md         ← Quick start guide
    ├── GUIA_USO_MCPs.md       ← How to use all MCPs
    ├── INSTRUCOES_COMPLETAS.md← Full setup instructions
    └── RESOLUCAO_PROBLEMAS.md ← Troubleshooting
```

## Agent Tribunal Flow

```
PDF input
  → inspect_pdf_metadata       (validate)
  → process_slide_for_vision   (convert pages to images)
  → Observer Agent             (describes: text, charts, equations)
  → Clínico Agent              (medical context interpretation)
  → Engenheiro Agent           (physics/math explanation)
  → Meta-Tribunal              (final synthesis)
  → append_to_notebook         (saves to .ipynb)
```

---

## Stack

| Layer | Tech |
|-------|------|
| Language | Python |
| MCP server | `server.py` (stdio transport) |
| PDF processing | pdf2image + poppler |
| Target PDFs | Radioterapia slides from Física Médica |
| Output | Jupyter notebook (`Radioterapia_Completo.ipynb`) |
| Originally built for | Cursor IDE → now accessible via Claude Code |

---

## Key Rules for This Project

1. **Entry point is `server.py`** — don't rename or restructure it; MCP config depends on the exact path.
2. **Virtual env at `.venv/`** — always activate before running Python commands.
3. **Don't add new agents** without updating the tribunal flow diagram above.
4. **PDF paths are hardcoded** in `COMECE_AQUI.md` — update them if the source folder changes.

---

## Running the Server

```bash
# From this folder:
.venv\Scripts\python.exe server.py
```

MCP config for Cursor/Claude:
- **Name:** `Biomed-Slide-Agent`
- **Type:** `command (stdio)`
- **Command:** `.venv\Scripts\python.exe`
- **Args:** `server.py`
- **Working dir:** `C:\Users\joaop\Desktop\AI projects\Agents-Tribunal`

---

## Changelog

### 2026-03-31
- Added `CLAUDE.md` to project (Claude Code integration)
