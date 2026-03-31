# claude-code-terminal

**GitHub:** `dternyak/claude-code-terminal`

## What It Is
Embedded floating terminal inside Obsidian that runs Claude Code. Toggle with hotkey — Claude has direct access to your vault files without leaving Obsidian.

## Setup (Windows — run in PowerShell)

### Prerequisites
```powershell
# Check Node.js is installed
node --version   # needs 18+
npm --version

# Install Claude Code CLI if not done
npm install -g @anthropic-ai/claude-code
```

### Install Plugin
```powershell
# Navigate to vault plugins folder
cd "C:\Users\joaop\Desktop\AI projects\.obsidian\plugins"

# Clone the repo
git clone https://github.com/dternyak/claude-code-terminal.git

# Enter folder and install deps
cd claude-code-terminal
npm install

# CRITICAL: recompile for Obsidian's Electron version
npm run rebuild:electron

# Build the plugin
npm run build

# Copy permissions config
mkdir -Force "..\..\..\.claude"
copy examples\settings.local.json "..\..\..\.claude\"
```

### Enable in Obsidian
1. Restart Obsidian
2. Settings → Community Plugins → enable **claude-code-terminal**
3. Toggle terminal: `Ctrl+Shift+\`` or Command Palette

## What It Gives You
- Claude Code running inside Obsidian
- Full file system access to vault
- Can read, write, search any note
- Runs commands without switching windows

## Status
- Check GitHub issues if `rebuild:electron` fails (Electron version mismatch is the main issue)
- Obsidian 1.9.x → Electron 37.3.1

## Connects To
- [[obsidian-agent-client]] (alternative approach)
- [[Fabric]] (CLI alternative, no plugin needed)
- [[HOME]]

---
*Part of → [[Repos-Index]] > Obsidian Tools*
