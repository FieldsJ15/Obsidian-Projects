# /brief

> Run at the end of any planning/brainstorming session.
> Saves a structured brief to `Sessions/[project]/YYYY-MM-DD_[topic].md`

---

## Instructions for Claude

When the user runs `/brief`, do the following:

1. **Ask** (if not obvious): "What project is this for? And a 2-4 word topic slug for the filename?"

2. **Generate the brief** and save to `Sessions/[project]/YYYY-MM-DD_[topic-slug].md`:

```markdown
# Brief: [Topic] — [DATE]

**Project:** [project name]
**Session type:** Planning / Brainstorming / Design
**Status:** [what decision/direction was reached]

---

## Context
[1-2 sentences: what problem or question this session addressed]

## What We Decided
[bullet list of concrete decisions made]

## Key Ideas Explored
[bullet list — include ideas that were rejected and why, not just what was chosen]

## Open Questions
[things still unresolved that need a future session]

## Next Actions
- [ ] [concrete next step]
- [ ] ...

## Notes for Future Claude
> [2-3 sentences giving the fastest possible onboarding to this topic/decision]
```

3. **Update** `_context/projects.md` if any new project direction was decided.

4. Confirm: "Brief saved to `Sessions/[project]/[filename]`."

---

## Naming Convention
`Sessions/[Project]/2026-03-31_mlc-coordinate-system.md`
