# Fabric

**GitHub:** `danielmiessler/fabric` | 30K+ stars

## What It Is
AI pattern framework for the terminal. Turn any text/URL into structured AI output and pipe it directly into your Obsidian vault. No GUI, no plugin — pure terminal automation.

## Core Concept: Patterns
Patterns are reusable LLM prompts. Run them on any input:
```bash
# Summarize a webpage → save to vault
fabric -u https://arxiv.org/abs/1234 -p summarize > "AI projects/Knowledge/paper-summary.md"

# Extract key insights from text
echo "paste your text" | fabric -p extract_wisdom

# Analyze a YouTube video
fabric -y "https://youtube.com/watch?v=xxx" -p summarize
```

## Setup (Windows WSL or PowerShell)
```bash
# Install (Linux/WSL)
curl -fsSL https://raw.githubusercontent.com/danielmiessler/fabric/main/install.sh | bash

# Or via Go
go install github.com/danielmiessler/fabric@latest

# Initialize (add API keys)
fabric --setup
# → paste Anthropic API key when prompted
```

## Shell Aliases → Vault Auto-routing
Add to `.bashrc` / `.zshrc`:
```bash
export OBSIDIAN_VAULT="/mnt/c/Users/joaop/Desktop/AI projects"

# Auto-save fabric output to vault
fabric_save() {
    fabric -p "$1" | tee "$OBSIDIAN_VAULT/Knowledge/$2.md"
}
# Usage: fabric_save summarize "my-paper-notes"
```

## Best Patterns for Biomedical Work
| Pattern | Use |
|---------|-----|
| `summarize` | Condense papers/articles |
| `extract_wisdom` | Key insights from long content |
| `analyze_claims` | Critical review of a paper |
| `create_keynote` | Turn notes into presentation |
| `explain_code` | Understand Python scripts |

## Connects To
- [[claude-code-terminal]]
- [[obsidian-agent-client]]
- [[Python-Biomedical]]

---
*Part of → [[Repos-Index]] > Obsidian Tools*
