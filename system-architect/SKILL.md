---
name: system-architect
description: Create process maps, system architecture diagrams, training guides, and connection maps showing how tools and workflows integrate. Use when Nate asks how things connect, wants a process map, needs a training document, asks to document a workflow, or wants to understand how tools work together. Also use after completing any new integration or setup to automatically document it.
---

# System Architect Skill

This skill governs how MasterClaw documents systems, tools, and workflows. Every time two or more tools are connected — document it. Every time a new integration is built — map it. Keep the knowledge base current.

---

## WHEN TO TRIGGER THIS SKILL

Trigger automatically when:
- Nate asks "how does X connect to Y?"
- Nate says "show me how everything works"
- Nate asks for a process map, workflow diagram, or system overview
- A new tool is added to the stack
- A new integration or automation is completed
- Nate asks for a training guide or tutorial on a workflow

---

## CORE RULES

### Rule 1: Always Create a Process Map When Connecting Two or More Tools

Any time two tools are wired together, document the connection before moving on. A map takes 5 minutes to write and saves hours of future confusion.

Minimum viable map format:
```
Tool A → [data type being passed] → Tool B → [what happens next]
```

Example:
```
yt-dlp → [.mp3 audio file] → Groq Whisper → [.md transcript] → /content-pipeline/transcripts/
```

---

### Rule 2: Show Data Flow with Clear Arrows

Every diagram must show:
- **What goes in** (the input data/trigger)
- **What comes out** (the output/result)
- **Where it goes** (file path, API, or next tool)

Format: `Tool A → data type → Tool B`

Example formats:
```
[Input] → Tool → [Output format] → [Destination]

YouTube URL → yt-dlp → MP3 file → /tmp/audio/
MP3 file → Groq Whisper API → transcript text → /content-pipeline/transcripts/YYYY-MM-DD-title.md
```

For complex flows, use ASCII box diagrams:
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Tool A     │────▶│   Tool B     │────▶│  Destination │
│  (input)     │     │  (process)   │     │  (output)    │
└──────────────┘     └──────────────┘     └──────────────┘
```

---

### Rule 3: Identify Human Touchpoints

In every flow map, label where a human (Nate or team) needs to take action. Mark these clearly:

```
👤 HUMAN STEP: Nate sends YouTube URL via WhatsApp
🤖 AUTO: yt-dlp downloads audio
🤖 AUTO: Groq transcribes
👤 HUMAN STEP: (optional) Nate reviews transcript before ingesting to AI Brain
🤖 AUTO: Transcript saved to /content-pipeline/transcripts/
```

Use emoji markers:
- `👤 HUMAN:` — manual action required
- `🤖 AUTO:` — fully automated, no human needed
- `⚠️ REVIEW:` — human should check before proceeding

---

### Rule 4: Identify Automation Opportunities

For every human touchpoint, note whether it could be automated and what it would take:

```
AUTOMATION OPPORTUNITY:
Current: Nate manually sends YouTube URL to trigger transcription
Could be: Make.com watches a YouTube playlist → auto-triggers on new video
Requires: Make.com webhook + YouTube watch module + existing transcription script
Effort: LOW
```

Rate automation opportunities:
- **LOW** — plug-and-play, can be done in < 1 hour
- **MEDIUM** — requires some custom code or configuration
- **HIGH** — significant build required

---

### Rule 5: Save Maps to the Tutorials Directory

All process maps and architecture docs save to:
```
/root/.openclaw/workspace/content-pipeline/tutorials/
```

Naming convention:
```
[topic]-process-map.md          ← for flow/process maps
[topic]-training-guide.md       ← for training docs
[topic]-integration-notes.md    ← for quick integration notes
how-everything-connects-master-map.md  ← the master overview (always update this)
```

---

### Rule 6: Create a Tutorial for Each New Connection

Every time a new tool connection is documented, create two things:

**1. Written Tutorial** — Covers:
- What each tool does
- Why they're connected
- Step-by-step setup instructions
- The exact brief to give Claude Code (if code was involved)
- Troubleshooting tips

**2. Video Script** — For the content pipeline. Format:
```json
{
  "title": "How [Tool A] connects to [Tool B]",
  "duration_seconds": 60,
  "voiceover_text": "...",
  "scenes": [
    { "text": "...", "duration": 5, "visual": "..." }
  ],
  "hashtags": [...],
  "platforms": ["TikTok", "Instagram Reels", "YouTube Shorts"]
}
```

Save video scripts to:
```
/root/.openclaw/workspace/content-pipeline/scripts/
```

---

### Rule 7: Update the Master Map When New Tools Are Added

After documenting any new tool or integration, update:
```
/root/.openclaw/workspace/content-pipeline/tutorials/how-everything-connects-master-map.md
```

Add the new tool to:
1. The Tool Directory table
2. The relevant flow diagram(s)
3. The "Quick Reference — Where Each Tool Lives" table at the bottom
4. Create a new flow section if the tool introduces a new workflow

Note the date of update at the top of the file.

---

## PROCESS MAP TEMPLATE

Use this template when creating any new process map:

```markdown
# [System/Integration Name] — Process Map
**Created:** [Date] | **Last Updated:** [Date]

## Overview
[One paragraph: what this system does and why it exists]

## Tools Involved
| Tool | Role | Category |
|------|------|----------|
| Tool A | Does X | Category |
| Tool B | Does Y | Category |

## Flow Diagram

[input trigger]
     │
     ▼
┌────────────────────┐
│   Tool A           │  ← [what it receives]
│   [what it does]   │  ← [how it processes]
└────────┬───────────┘
         │  [what it outputs]
         ▼
┌────────────────────┐
│   Tool B           │
│   [what it does]   │
└────────┬───────────┘
         │
         ▼
[final output / destination]

## Human Touchpoints
👤 HUMAN: [step 1]
🤖 AUTO: [step 2]
👤 HUMAN: [step 3]

## Automation Opportunities
- [Step X] could be automated by [method] | Effort: LOW/MEDIUM/HIGH

## Setup Instructions
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Troubleshooting
- [Common issue] → [Fix]
```

---

## TRAINING GUIDE TEMPLATE

```markdown
# Training Guide: [Topic]
**Audience:** [Nate / Team / Clients]
**Created:** [Date]

## What This Is
[Plain English explanation]

## Why It Matters
[Business value / time saved / capability unlocked]

## How It Works (Overview)
[Simple diagram or flow]

## Step-by-Step
### Step 1: [Name]
[Instructions]

### Step 2: [Name]
[Instructions]

## Real Examples
### Example 1: [Name]
[What was built, what brief was used, what the result was]

## Common Mistakes
- ❌ [Mistake] → ✅ [Correct approach]

## Video Script
[JSON script for Remotion pipeline]
```

---

## REFERENCE: KEY FILE LOCATIONS

```
/root/.openclaw/workspace/
├── content-pipeline/
│   ├── tutorials/          ← Process maps + training guides
│   ├── scripts/            ← Remotion video scripts (JSON)
│   ├── transcripts/        ← Groq transcriptions
│   ├── audio/              ← ElevenLabs output
│   ├── renders/            ← Remotion video output
│   └── output/             ← Final assembled videos
├── skills/
│   └── system-architect/   ← This skill
├── MEMORY.md               ← MasterClaw long-term memory
└── TOOLS.md                ← Stack-specific notes
```

---

*Skill maintained by MasterClaw 🦞*
*When in doubt: map it, document it, save it.*
