# System Architecture

> This is the living map of João's AI file system. Claude reads this at the start of every session.
> **After any structural change, add a dated entry to the Changelog section below.**

---

## Current Architecture (as of 2026-03-31)

### Folder Map

```
AI projects/                        ← Root vault (Obsidian + Claude Code)
│
├── CLAUDE.md                       ← System instructions for Claude
├── .gitignore                      ← Git ignore rules
│
├── _context/                       ← Context files (read-first zone)
│   ├── architecture.md             ← THIS FILE — system map + change log
│   ├── goals.md                    ← Active goals and priorities
│   └── projects.md                 ← Project registry with statuses
│
├── _commands/                      ← Slash commands (simple, automated)
│   ├── handover.md                 ← /handover — end-of-session recap
│   └── weekly-update.md            ← /weekly-update — weekly maintenance
│
├── _skills/                        ← Reusable multi-step workflows
│   └── skill-inventory.md          ← Index of all skills
│
├── _sessions/                      ← Saved session recaps (auto-generated)
│
├── _archive/                       ← Archived files (never deleted, just moved)
│
├── Projects/                       ← Active project folders
│   ├── Agents-Tribunal/            ← MCP agent for legal/medical docs
│   ├── Multi-Leaf-Colimator/       ← Radiotherapy MLC project
│   └── ...
│
└── First Vault/                    ← Original Obsidian vault
    └── .obsidian/                  ← Obsidian config (synced via obsidian-git)
```

### Core Stack

| Layer | Tool | Role |
|-------|------|------|
| AI Engine | Claude Sonnet 4.6 | Reads, writes, executes, reasons |
| Editor | Obsidian | View and edit all markdown files |
| Version Control | GitHub + obsidian-git | Backup, sync, history |
| File System | Windows `C:\Users\joaop\Desktop\AI projects` | Single source of truth |

### Key Principles

- **Context-first:** Always read `_context/` before acting
- **Archive, never delete:** Unused files go to `_archive/`
- **Log changes here:** Every structural decision goes in the Changelog below
- **Lean CLAUDE.md:** System orientation only; depth lives in `_context/`

---

## Changelog

### 2026-03-31 — Initial System Setup
- Created full folder scaffold: `_context/`, `_commands/`, `_skills/`, `_sessions/`, `_archive/`, `Projects/`
- Created `CLAUDE.md` with system instructions
- Created `_context/architecture.md` (this file)
- Created `_context/goals.md` and `_context/projects.md`
- Created `/handover` and `/weekly-update` commands
- Created `_skills/skill-inventory.md`
- Created `.gitignore` for obsidian-git compatibility
- Stack: Claude Sonnet 4.6 + Obsidian + obsidian-git → GitHub (`FieldsJ15/Obsidian-Projects`)

---

<!-- Add new entries above this line, newest first -->
