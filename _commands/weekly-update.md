# /weekly-update

> **What it does:** End-of-week maintenance command. Runs review, archives old files, updates context, and preps next week.
> Run every Friday or start of new week.

---

## Instructions for Claude

When the user runs `/weekly-update`, execute these steps in order:

### Step 1 — Weekly Review
- Read all `_sessions/` recaps from the past 7 days
- Summarize: what got done, what's still open, any patterns

### Step 2 — Archive Old Files
- Check `_sessions/` for recaps older than 30 days → move to `_archive/_sessions/`
- Check `Projects/` for any inactive project folders → ask user before archiving
- Remove obvious temp files (`.tmp`, draft files marked as old)

### Step 3 — Update Context Files
- Review `_context/goals.md` — are current goals still accurate? Flag if outdated
- Review `_context/projects.md` — update statuses based on session recaps
- Review `_context/architecture.md` — verify the folder map is still accurate

### Step 4 — Update Skill Inventory
- Check `_skills/` for any new skills added this week
- Update `_skills/skill-inventory.md` if needed

### Step 5 — Generate Next Week Preview
Output a brief list:
```
## Next Week — [DATE RANGE]

### Priority Actions
1. ...
2. ...

### Open Threads to Pick Up
- ...

### System Maintenance Notes
- ...
```

### Step 6 — GitHub Reminder
Remind the user: "Run obsidian-git sync (or push via terminal) to back up to GitHub."

---

## Notes
- Don't auto-delete anything. Always ask before archiving project folders.
- Keep the output scannable — use lists, not paragraphs.
