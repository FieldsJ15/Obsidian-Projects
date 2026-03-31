# /handover

> **What it does:** Saves a session recap to `_sessions/` before you close the conversation.
> Run this at the end of every session.

---

## Instructions for Claude

When the user runs `/handover`, do the following:

1. **Create a session recap file** at `_sessions/YYYY-MM-DD_HH-MM.md` with today's date and time.

2. **Populate it with this structure:**

```markdown
# Session Recap — [DATE]

## What We Worked On
- [bullet list of main topics/tasks]

## Decisions Made
- [any important decisions, trade-offs, or direction choices]

## Changes to the System
- [files created, modified, deleted/archived]

## Open Threads
- [things left unfinished or to pick up next session]

## Next Steps
- [concrete actions for the next session]

## Key Context for Next Claude
> [2-3 sentences that give the next Claude instance the fastest possible onboarding to continue this work]
```

3. **Check if any architectural changes happened** this session. If yes, append a changelog entry to `_context/architecture.md` with today's date.

4. **Check if any goals changed.** If yes, update `_context/goals.md`.

5. **Confirm** to the user: "Handover saved to `_sessions/[filename]`. Ready to close."

---

## Example Output

> Handover saved to `_sessions/2026-03-31_14-30.md`. Ready to close.
