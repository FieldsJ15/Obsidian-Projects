# /index

> Generates a file index of the vault so Claude can see everything without reading every file.
> Saves to `Dashboard/vault-index.md`
> Run before any session where Claude needs vault-wide context.

---

## Instructions for Claude

When the user runs `/index`, do the following:

1. **Scan the entire vault** (skip `_archive/`, `node_modules/`, `.obsidian/`, `.git/`)
2. **Generate** `Dashboard/vault-index.md`:

```markdown
# Vault Index
*Generated: [DATE] — [total file count] files*

## _context/
- architecture.md — system map + changelog
- goals.md — active priorities
- projects.md — project registry

## _commands/
- brief.md, guide.md, daily.md, index.md, handover.md, weekly-update.md

## Sessions/
### MLC-Sim/
- [list of session files with dates]
### Biomedical/
- [list]

## Guides/
- [list by project]

## Knowledge/
### Biomedical/
- [list]
### Medical-Imaging/
- [list]
[etc.]

## Writing/
### Essays/
- [list]
### Articles/
- [list]

## Dashboard/
- daily.md, vault-index.md
```

3. Confirm: "Index saved to `Dashboard/vault-index.md` — [N] files indexed."

---

## Why This Exists
Feeding the entire vault to Claude burns tokens and hits context limits.
The index gives Claude a map to navigate selectively — it reads only what's relevant.
