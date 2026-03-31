# /guide

> Run at the end of any building session.
> Generates a technical guide for what was built → saved to `Guides/[project]/[feature].md`
> Future Claude instances can read this to understand what exists and how to use it.

---

## Instructions for Claude

When the user runs `/guide`, do the following:

1. **Ask** (if not obvious): "What did we just build? What's the guide for?"

2. **Generate the technical guide** and save to `Guides/[project]/[feature-name].md`:

```markdown
# Guide: [What Was Built]

**Project:** [project]
**Built:** [DATE]
**Status:** Working / Experimental / Deprecated

---

## What This Is
[1 paragraph: what it does, why it exists, what problem it solves]

## How to Use It

### Prerequisites
- [dependency or setup needed]

### Basic Usage
[step-by-step with code blocks]

### Common Patterns
[2-3 examples of typical use cases]

## Architecture
[how it's built — key files, key functions, how pieces connect]

## Known Limitations
[what it doesn't do, edge cases to watch for]

## How to Extend It
[where to add new features if needed]

## Troubleshooting
[common errors and fixes]

---
*Built with Claude Sonnet 4.6 on [DATE]*
```

3. **Link it** — add a reference in the project's `CLAUDE.md` under a "Guides" section.

4. Confirm: "Guide saved to `Guides/[project]/[filename]`."

---

## Naming Convention
`Guides/MLC-Sim/coordinate-system-implementation.md`
`Guides/AI-System/handover-command.md`
