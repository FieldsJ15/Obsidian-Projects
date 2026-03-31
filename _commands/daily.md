# /daily

> Regenerates the daily dashboard at `Dashboard/daily.md`.
> Run every morning or overnight via a script.

---

## Instructions for Claude

When the user runs `/daily`, do the following:

1. **Read** `_context/goals.md` → extract current focus and active goals
2. **Read** `_context/projects.md` → get project statuses and next actions
3. **Scan** `_sessions/` → find the 5 most recent session recaps, extract open threads
4. **Scan** `Sessions/` → find the 5 most recent briefs
5. **Rewrite** `Dashboard/daily.md` with today's date and all updated info:

```markdown
# Daily Dashboard

> Auto-generated. Run `/daily` to regenerate.
> Last updated: [TODAY]

---

## Today — [DATE]

### Active Projects
| Project | Last Session | Status | Next Action |
|---------|-------------|--------|-------------|
[from _context/projects.md]

### Open Threads
[from recent _sessions/ recaps — things marked as unfinished]

### This Week's Focus
[from _context/goals.md current focus section]

---

## Recent Sessions (last 5)
[filenames + one-line summary from each]

---

## Recent Briefs (last 5)
[filenames + project + topic]

---

## Quick Links
- [[HOME]] — knowledge map
- [[Repos-Index]] — curated repos
- `_context/goals.md` — priorities
- `_context/projects.md` — project statuses
```

6. Confirm: "Dashboard updated → `Dashboard/daily.md`"

---

## Automating It (Optional)
To auto-run overnight on Windows, create a Task Scheduler job that runs:
```
wsl -e bash -c "cd '/mnt/c/Users/joaop/Desktop/AI projects' && claude -p '/daily'"
```
