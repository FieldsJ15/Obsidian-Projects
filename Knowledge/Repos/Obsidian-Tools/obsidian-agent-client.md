# obsidian-agent-client

**GitHub:** `RAIT-09/obsidian-agent-client`

## What It Is
Chat panel inside Obsidian that bridges Claude Code, Gemini CLI, and Codex simultaneously. Uses Agent Client Protocol (ACP) — no terminal emulation, just a chat interface connected to CLI binaries.

## Key Feature: @notename
Type `@notename` in chat → plugin injects that note's content directly into the AI context. Zero token cost compared to uploading entire vault.

## Setup

### Step 1 — Install CLI tools
```powershell
# Claude Code (already done)
npm install -g @anthropic-ai/claude-code

# ACP adapter
npm install -g @agentclientprotocol/claude-agent-acp

# Authenticate
claude   # triggers OAuth login
```

### Step 2 — Get binary paths
```powershell
# Windows
where.exe node
where.exe claude-agent-acp
# Copy these paths — you'll need them in Step 4
```

### Step 3 — Install plugin via BRAT
1. In Obsidian: install **BRAT** plugin (Community Plugins)
2. BRAT → Add Beta Plugin → `RAIT-09/obsidian-agent-client`

### Step 4 — Configure
Settings → Agent Client → paste the paths from Step 2

## vs claude-code-terminal
| | claude-code-terminal | obsidian-agent-client |
|--|--|--|
| Interface | Real terminal | Chat panel |
| Multi-agent | No | Yes (Claude + Gemini + Codex) |
| Setup complexity | Higher (Electron rebuild) | Lower |
| @notename injection | No | Yes |
| Shell commands | Yes | No |

## Connects To
- [[claude-code-terminal]]
- [[Fabric]]

---
*Part of → [[Repos-Index]] > Obsidian Tools*
