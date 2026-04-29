# 🦞 Training Guide: How to Use MasterClaw with Claude Code
**For Nate & Team | Written by MasterClaw | April 2026**

---

## PART 1: THE TWO AI TOOLS YOU NEED TO KNOW

### What is MasterClaw?

MasterClaw is your AI business partner, running on **OpenClaw** and living on **WhatsApp**. Think of MasterClaw as your always-on strategist — the one who:

- Knows your whole business stack
- Remembers your goals and context across sessions (via MEMORY.md)
- Writes scripts, briefs, strategies, and specs
- Manages your server files and content pipeline
- Directs other tools on *what* to build

**How you talk to MasterClaw:** WhatsApp, anytime. Text naturally. MasterClaw reads your project files, knows your tools, and responds like a knowledgeable teammate — not a generic chatbot.

**What MasterClaw can't do directly:** Write and execute complex multi-file software in real-time. For that, you need Claude Code.

---

### What is Claude Code?

Claude Code is **Anthropic's coding agent that lives in your terminal**. It's designed to:

- Read, write, and edit entire codebases
- Execute commands, run scripts, install packages
- Navigate complex project structures
- Build full applications from a spec

**How you use Claude Code:** Open your terminal, navigate to a project folder, and run `claude`. Then you give it a brief — and it builds.

**What Claude Code can't do:** It doesn't know your WhatsApp conversations, your personal business context, or what tools you've already set up — *unless you tell it*. That's where the handoff comes in.

---

## PART 2: HOW THEY WORK TOGETHER

MasterClaw and Claude Code are complementary. Neither replaces the other.

```
MasterClaw                   Claude Code
(Architect / Strategist)     (Builder / Engineer)

- Knows the big picture      - Knows how to write the code
- Writes the spec/brief      - Executes the spec
- Understands your goals     - Understands the codebase
- Lives on WhatsApp          - Lives in the terminal
- Remembers your context     - Reads your project files
```

**The Mental Model:**
- MasterClaw is the architect who designs the building
- Claude Code is the contractor who constructs it
- Nate is the owner who says what he needs

---

## PART 3: THE HANDOFF WORKFLOW

This is the core workflow. Master this and you can build almost anything.

```
STEP 1: Tell MasterClaw what you want
        (WhatsApp)
        "I want to build an automated YouTube transcription system
         that saves transcripts to my server"
             │
             ▼
STEP 2: MasterClaw writes the spec
        (Detailed brief with file paths, tools, logic, structure)
             │
             ▼
STEP 3: Copy the spec → paste into Claude Code
        (Terminal: cd /your/project && claude)
        Paste the full spec as your first message
             │
             ▼
STEP 4: Claude Code builds it
        (Reads files, writes code, installs packages, tests)
             │
             ▼
STEP 5: Paste Claude Code's summary back to MasterClaw
        (WhatsApp: "Claude Code did X, Y, Z — here's what it said")
             │
             ▼
STEP 6: MasterClaw reviews, adjusts, and writes the next brief
        (Iterate until done)
```

**Pro tip:** You don't need to understand every line of code. You're the bridge between the strategist (MasterClaw) and the builder (Claude Code). Your job is the handoff.

---

## PART 4: REAL EXAMPLES FROM NATE'S BUILD

### Example 1: Setting Up Remotion

**What we needed:** A video renderer that takes a script + scenes and produces an MP4 — programmatically.

**The brief MasterClaw wrote for Claude Code:**
> "Set up a Remotion project in `/root/.openclaw/workspace/content-pipeline/remotion/`. 
> Create a composition called `ContentVideo` that accepts: title (string), scenes (array of {text, duration}), voiceover audio file path, and background color. 
> Use Tailwind-style inline styles. 
> The output should be a 1080x1920 (vertical) video at 30fps.
> Install dependencies and test with a sample render."

**What happened:** Claude Code scaffolded the entire Remotion project, wrote the React components, set up the config, and produced a test render. MasterClaw then reviewed the output and wrote a follow-up brief to add the ElevenLabs audio sync.

**Lesson learned:** Give Claude Code a clear file path, clear input/output shapes, and the tech stack to use. It handles the rest.

---

### Example 2: Building the Content Pipeline

**What we needed:** An end-to-end system where MasterClaw passes a script → the pipeline renders a video → saves it ready for Blotato upload.

**How we broke it into steps:**
1. Brief 1: Build the script formatter (MasterClaw spec → structured JSON)
2. Brief 2: Wire JSON → Remotion render
3. Brief 3: Add ElevenLabs voice generation step
4. Brief 4: Add ffmpeg merge step (video + audio)
5. Brief 5: Output to `/content-pipeline/output/` with metadata file

**Key insight:** Don't ask Claude Code to build everything at once. MasterClaw wrote a separate brief for each component, Claude Code built each one, and Nate assembled them via handoffs. Modular > monolith.

---

### Example 3: The AI Transcription System

**What we needed:** Nate sends a YouTube URL → system downloads audio → transcribes → saves to server.

**The brief MasterClaw wrote:**
> "Create a shell script at `/root/.openclaw/workspace/content-pipeline/transcribe.sh`.
> It should:
> 1. Accept a YouTube URL as an argument
> 2. Use yt-dlp to download audio only as MP3 to /tmp/
> 3. Send the MP3 to Groq Whisper API (key in .env) 
> 4. Save the transcript as a .md file to /content-pipeline/transcripts/ with filename derived from the video title and date
> 5. Print the saved path when done
> Include error handling for failed downloads."

**Result:** A single command. `./transcribe.sh https://youtube.com/...` → transcript saved. MasterClaw can then read those transcripts directly.

---

## PART 5: HOW TO WRITE A GOOD CLAUDE CODE BRIEF

Claude Code is powerful but context-blind. A good brief gives it everything it needs.

### ✅ The Good Brief Template

```
GOAL: [What you're building in one sentence]

CONTEXT: [What already exists, what tools are installed, what the stack is]

TASK:
1. [Specific step 1]
2. [Specific step 2]
3. [Specific step 3]

FILE PATHS: [Where to read from, where to write to]

INPUTS: [What data comes in — format, source]
OUTPUTS: [What should come out — format, destination]

TECH STACK: [Languages, libraries, APIs to use]

ENV VARS: [Variable names it should use — never paste actual keys]

CONSTRAINTS:
- [What NOT to do]
- [Edge cases to handle]
- [Style/format requirements]

SUCCESS LOOKS LIKE: [How you know it worked]
```

### ❌ The Bad Brief

> "Build me a video system"

That's it. Claude Code will ask 20 clarifying questions or build something completely wrong. **MasterClaw's job is to never write a vague brief.**

---

## PART 6: COMMON MISTAKES

### Mistake 1: Telling Claude Code to do manual things

❌ "Download some B-roll footage from YouTube manually"
✅ "Use yt-dlp with these flags to download from this URL and save to this path"

Claude Code can only do things a computer can do. It can't open a browser manually, click buttons, or film things.

---

### Mistake 2: Not giving Claude Code tool context

❌ Starting Claude Code with "build the transcription system"

Claude Code doesn't know you have yt-dlp installed, that Groq is your transcription API, or where your server files live. 

✅ Always include: what tools are available, what's already installed, what the file structure looks like.

---

### Mistake 3: Pasting partial specs

If MasterClaw wrote a 3-part spec and you only paste Part 1, Claude Code builds Part 1 in a way that may not connect to Parts 2 and 3. Always paste the full brief, or be explicit: "This is Part 1 of 3 — here's the full context for all parts."

---

### Mistake 4: Not reviewing what Claude Code built

Claude Code is excellent but not infallible. After each build:
- Ask MasterClaw to review the code Claude Code wrote (paste key files)
- Run a test before integrating into your pipeline
- Don't assume it worked — verify

---

## PART 7: THE AGENTS.MD / CLAUDE.MD TRICK 🧠

This is one of the most powerful patterns for working with Claude Code.

### The Problem

Every time you start a new Claude Code session, it starts fresh. It doesn't know:
- What tech stack you're using
- What APIs are available
- What the folder structure means
- What standards you follow

### The Solution: CLAUDE.md (or AGENTS.md)

Put a file called `CLAUDE.md` in your project root. Claude Code automatically reads it at the start of every session.

**What to put in CLAUDE.md:**

```markdown
# Project Context for Claude Code

## Stack
- Runtime: Node.js 18+
- Video: Remotion 4.x
- Audio: ElevenLabs API (key in .env as ELEVENLABS_API_KEY)
- Transcription: Groq Whisper (key in .env as GROQ_API_KEY)
- Media: Pexels API (key in .env as PEXELS_API_KEY)
- Publishing: Blotato (key in .env as BLOTATO_API_KEY)

## File Structure
/content-pipeline/
  /scripts/        ← raw video scripts (JSON)
  /audio/          ← ElevenLabs output (MP3)
  /renders/        ← Remotion output (MP4)
  /transcripts/    ← Groq transcripts (MD)
  /output/         ← Final assembled videos

## Standards
- All videos: 1080x1920 vertical, 30fps
- Transcripts: Markdown format, include title + date header
- Scripts: JSON with fields: title, scenes[], voiceover_text, hashtags[]

## DO NOT
- Hardcode API keys (use process.env)
- Overwrite files in /output/ without date-stamping
- Use synchronous file operations
```

**Now every Claude Code session starts already knowing your entire stack.** You don't have to re-explain it. MasterClaw helps you keep CLAUDE.md up to date as the stack evolves.

### Why AGENTS.md too?

OpenClaw / MasterClaw looks for `AGENTS.md` in workspace folders for its own context. When both exist in a project folder, both MasterClaw and Claude Code can orient themselves to the same project without you explaining anything.

**The result:** You spend your time directing, not explaining. That's leverage.

---

## PART 8: VIDEO SCRIPT — "MasterClaw + Claude Code"
*Remotion-ready script for content pipeline*

```json
{
  "title": "MasterClaw + Claude Code: The AI Team Doing My Work",
  "duration_seconds": 75,
  "voiceover_text": "I use two AI tools to run my entire content business. And they work as a team. First, there's MasterClaw — my AI business partner on WhatsApp. I tell it what I want to build. It thinks strategically, writes the plan, and knows my entire tech stack. Then there's Claude Code — the coder in my terminal. It takes MasterClaw's plan and actually builds it. Real code. Real systems. The handoff is simple: MasterClaw writes the brief. I paste it into Claude Code. Claude Code builds it. I paste the result back to MasterClaw. We iterate until it's done. This is how I built my entire content pipeline. The transcription system. The video renderer. All of it. Neither AI can do the other's job. But together? They're unstoppable. And I'm just the bridge between them.",
  "scenes": [
    {
      "text": "Two AIs. One unstoppable team.",
      "duration": 3,
      "visual": "Split screen: WhatsApp on left, Terminal on right"
    },
    {
      "text": "MasterClaw = The Strategist",
      "duration": 5,
      "visual": "WhatsApp chat with MasterClaw writing a brief"
    },
    {
      "text": "Claude Code = The Builder",
      "duration": 5,
      "visual": "Terminal showing Claude Code writing code"
    },
    {
      "text": "The Workflow",
      "duration": 10,
      "visual": "Flowchart: Brief → Build → Review → Ship"
    },
    {
      "text": "We built this entire pipeline together",
      "duration": 8,
      "visual": "Screen recording of content pipeline running"
    },
    {
      "text": "The CLAUDE.md trick: give it context once, use it forever",
      "duration": 8,
      "visual": "Code editor showing CLAUDE.md file"
    },
    {
      "text": "You're the bridge. They do the work.",
      "duration": 5,
      "visual": "Diagram showing Nate as connector between MasterClaw and Claude Code"
    },
    {
      "text": "Start with one brief. See what gets built.",
      "duration": 6,
      "visual": "Call to action screen"
    }
  ],
  "hashtags": ["#AItools", "#ClaudeCode", "#AIautomation", "#buildinpublic", "#contentcreator", "#AIbusiness"],
  "platforms": ["TikTok", "Instagram Reels", "YouTube Shorts"]
}
```

---

## QUICK REFERENCE CARD

```
┌───────────────────────────────────────────────────────┐
│           MASTERCLAW + CLAUDE CODE CHEAT SHEET        │
├───────────────────────────────────────────────────────┤
│  MASTERCLAW        │  CLAUDE CODE                     │
│  WhatsApp          │  Terminal                         │
│  Strategist        │  Builder                          │
│  Writes briefs     │  Executes briefs                  │
│  Knows context     │  Reads CLAUDE.md                  │
├───────────────────────────────────────────────────────┤
│  THE HANDOFF:                                         │
│  1. Tell MasterClaw what you want                     │
│  2. Get the brief                                     │
│  3. Paste into Claude Code                            │
│  4. Claude Code builds                                │
│  5. Paste results back to MasterClaw                  │
│  6. Iterate                                           │
├───────────────────────────────────────────────────────┤
│  ALWAYS INCLUDE IN YOUR BRIEF:                        │
│  ✓ Goal (1 sentence)                                  │
│  ✓ File paths                                         │
│  ✓ Input/output format                                │
│  ✓ Tech stack                                         │
│  ✓ Env var names                                      │
│  ✓ What success looks like                            │
├───────────────────────────────────────────────────────┤
│  THE TRICK: Put CLAUDE.md in every project folder     │
│  Claude Code reads it automatically. Zero re-explain. │
└───────────────────────────────────────────────────────┘
```

---

*Written by MasterClaw 🦞 | April 2026*
*Update this guide when new workflows are established*
