# 🗺️ How Everything Connects — Master Process Map
**Nate's Business AI Ecosystem | Last Updated: April 2026**

---

## 🧠 THE FULL ECOSYSTEM AT A GLANCE

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         NATE'S AI BUSINESS STACK                           │
│                                                                             │
│  ORCHESTRATION LAYER                                                        │
│  ┌──────────────────────────────────┐                                       │
│  │  MasterClaw (OpenClaw)           │  ← Nate talks here via WhatsApp       │
│  │  AI brain, strategist, director  │  ← Reads/writes server files          │
│  └──────────────┬───────────────────┘                                       │
│                 │                                                           │
│     ┌───────────┴──────────┐                                                │
│     ▼                      ▼                                                │
│  BUILDING LAYER         AUTOMATION LAYER                                    │
│  Claude Code            Make.com                                            │
│  (terminal agent)       (no-code workflows)                                 │
│     │                      │                                                │
│     ▼                      ▼                                                │
│  OUTPUT LAYER           DISTRIBUTION LAYER                                  │
│  Remotion (video)       Blotato → TikTok, IG,                               │
│  ElevenLabs (voice)     YouTube, LinkedIn, X                                │
│  HeyGen (avatar)                                                            │
│                                                                             │
│  KNOWLEDGE LAYER         SALES & MONETIZATION                               │
│  Custom AI Brain (RAG)   GHL (leads + CRM)                                  │
│  NotebookLM              Gumroad (products)                                 │
│  Groq Whisper            Skool (community)                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 TOOL DIRECTORY

| Tool | Role | Category |
|------|------|----------|
| MasterClaw (OpenClaw) | AI orchestrator, strategist, WhatsApp interface | Brain |
| Claude Code | Custom software builder, terminal coding agent | Builder |
| Remotion | Renders videos from React/TypeScript code | Video |
| Go Viral Bro | Viral content discovery plugin for Claude Code | Research |
| Groq Whisper | Speech-to-text transcription (fast, cheap) | Audio |
| yt-dlp | Downloads YouTube audio/video | Downloader |
| ElevenLabs | Text → realistic voiceover audio | Audio |
| Pexels API | Free stock footage for video production | Media |
| Seedance | AI video generation | Video Gen |
| Nana Banana | AI face/body generation for influencer content | AI Avatar |
| HeyGen | AI talking head avatar videos | AI Avatar |
| Blotato | Multi-platform video publishing automation | Distribution |
| Make.com | No-code workflow automation | Automation |
| GHL (GoHighLevel) | CRM, lead gen, AI follow-up | Sales |
| Custom AI Brain (RAG) | Department knowledge bases with cited answers | Knowledge |
| NotebookLM | Research summarization and synthesis | Research |
| Gumroad | Digital product sales | Monetization |
| Skool | Community platform and course hosting | Community |

---

## FLOW 1: CONTENT PIPELINE FLOW
**"From idea to published video — automated"**

```
TOPIC / IDEA
     │
     ▼
┌────────────────────┐
│  Nate tells        │  ← WhatsApp message
│  MasterClaw        │
└────────┬───────────┘
         │  writes script + scene breakdown
         ▼
┌────────────────────┐
│   MasterClaw       │  ← Writes: voiceover script, scene list,
│   (Strategist)     │     caption, hashtags, CTA
└────────┬───────────┘
         │  pastes spec to Claude Code
         ▼
┌────────────────────┐
│   Claude Code      │  ← Reads CLAUDE.md / AGENTS.md for stack context
│   (Builder)        │  ← Uses Go Viral Bro for hook research
└──┬─────────────────┘
   │                │
   ▼                ▼
┌──────────┐   ┌──────────────┐
│ Remotion │   │  ElevenLabs  │
│ Renders  │   │  Generates   │
│ visuals  │   │  voiceover   │
│ + text   │   │  audio       │
└──┬───────┘   └──────┬───────┘
   │                  │
   │  ┌───────────────┘
   ▼  ▼
┌────────────────────┐
│   Assemble video   │  ← Claude Code combines video + audio
│   (ffmpeg / code)  │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│     Blotato        │  ← Auto-publishes with captions/hashtags
└────────┬───────────┘
         │
         ▼
   ┌─────┴──────────────────────────────┐
   │  TikTok · Instagram · YouTube      │
   │  LinkedIn · X (Twitter) · Facebook │
   └────────────────────────────────────┘

STOCK FOOTAGE: Pexels API → feeds into Remotion scenes
AVATAR OPTION: HeyGen → talking head overlay on video
```

**Human touchpoints:** Nate provides the topic/idea | Nate reviews before publish (optional)
**Automation opportunities:** MasterClaw could auto-generate topics from trending data → fully hands-free pipeline

---

## FLOW 2: TRANSCRIPTION FLOW
**"YouTube knowledge → your AI Brain"**

```
YOUTUBE URL
     │
     │  Nate sends link to MasterClaw
     ▼
┌────────────────────┐
│    yt-dlp          │  ← Downloads audio-only (.mp3)
│  (downloader)      │
└────────┬───────────┘
         │  audio file → server
         ▼
┌────────────────────┐
│   Groq Whisper     │  ← Fast, cheap transcription API
│  (transcription)   │  ← Returns timestamped text
└────────┬───────────┘
         │  .txt / .md transcript
         ▼
┌────────────────────────────────────┐
│   Server Storage                   │
│   /content-pipeline/transcripts/   │
└──────────┬─────────────────────────┘
           │
     ┌─────┴──────┐
     ▼            ▼
┌──────────┐  ┌──────────────────┐
│NotebookLM│  │ Custom AI Brain  │
│Research  │  │ RAG Knowledge    │
│synthesis │  │ Base (ingested)  │
└──────────┘  └──────────────────┘

Human touchpoints: Nate sends the YouTube URL
Automation: Make.com could auto-trigger on saved bookmarks
```

---

## FLOW 3: AI INFLUENCER FLOW
**"Generate an AI persona posting content at scale"**

```
TOPIC / NICHE
     │
     ▼
┌────────────────────┐
│   MasterClaw       │  ← Writes character brief + script
│   writes script    │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│   Nana Banana      │  ← Generates AI face/body
│   (face gen)       │  ← Consistent look per character
└────────┬───────────┘
         │  character images
         ▼
┌────────────────────┐
│    Seedance        │  ← Animates character into video
│  (AI video gen)    │  ← Script → motion
└────────┬───────────┘
         │  video clip
         ▼
┌────────────────────┐
│   ElevenLabs       │  ← Cloned or generated voice
│  (voice layer)     │  ← Matches character persona
└────────┬───────────┘
         │  audio
         ▼
┌────────────────────┐
│  Assemble + Edit   │  ← Claude Code / ffmpeg merges
│  (Claude Code)     │  ← Adds captions, music, B-roll
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│     Blotato        │  ← Publishes to all platforms
└────────────────────┘

Human touchpoints: Initial character design approval | Topic direction
Automation: Full pipeline can run on schedule with topic feed
```

---

## FLOW 4: AI BRAIN FLOW
**"Your business knowledge, always available, always cited"**

```
RAW KNOWLEDGE SOURCES
┌──────────────────────────────────────────┐
│  PDFs   Transcripts   SOPs   Emails      │
│  Training docs   Meeting notes           │
└──────────────────────┬───────────────────┘
                       │  ingestion
                       ▼
┌────────────────────────────────────────────┐
│         Custom AI Brain (RAG System)       │
│                                            │
│  ┌─────────────┐  ┌──────────────────────┐ │
│  │ Ask Grandeur│  │ Ask Sales            │ │
│  │ (Company KB)│  │ (Sales playbook)     │ │
│  └─────────────┘  └──────────────────────┘ │
│  ┌─────────────┐                           │
│  │ Ask Ops     │                           │
│  │ (Operations)│                           │
│  └─────────────┘                           │
└──────────────────────┬─────────────────────┘
                       │  vector search
                       ▼
┌────────────────────────────────────────────┐
│        Custom Chat Interface               │
│  (web app or WhatsApp or Slack bot)        │
└──────────────────────┬─────────────────────┘
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   Customers ask               Team asks
   "How do I...?"              "What's our SOP for...?"
          │                         │
          ▼                         ▼
   Cited answers              Cited answers
   (with source docs)         (with source docs)

Feeds into AI Brain:
  NotebookLM summaries → refined knowledge chunks
  Groq transcripts → video tutorial knowledge
  Nate's notes → proprietary methodology
```

---

## FLOW 5: LEAD GEN FLOW
**"Content drives leads, AI closes the loop"**

```
CONTENT (social media posts / videos)
     │
     │  viewer takes action
     ▼
┌────────────────────┐
│   GHL Landing Page │  ← Opt-in form / link in bio
│   (GoHighLevel)    │
└────────┬───────────┘
         │  lead captured
         ▼
┌────────────────────┐
│   GHL CRM          │  ← Lead tagged, scored, segmented
│   + AI Follow-up   │  ← Automated SMS/email sequence
└────────┬───────────┘
         │  interested lead
         ▼
┌────────────────────┐
│  Booking System    │  ← Calendar link / auto-schedule
│  (in GHL)          │
└────────┬───────────┘
         │  call booked
         ▼
┌────────────────────┐
│   Discovery Call   │  ← Human (Nate / sales team)
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│   Proposal Sent    │  ← GHL tracks proposal stage
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│   CLOSED ✅        │  ← Revenue logged
└────────────────────┘

Parallel monetization paths:
  Content viewers → Gumroad (buy digital products)
  Content viewers → Skool (join community/course)
```

---

## FLOW 6: LEARNING FLOW
**"YouTube tutorials → business intelligence"**

```
YOUTUBE TUTORIALS / COURSES
     │
     │  Nate or MasterClaw identifies valuable content
     ▼
┌────────────────────┐
│  yt-dlp downloads  │  ← Audio extracted
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│  Groq Whisper      │  ← Full transcript generated
│  transcribes       │
└────────┬───────────┘
         │  raw transcript
         ▼
┌────────────────────┐
│   NotebookLM       │  ← Upload transcript for deep analysis
│   (summarization)  │  ← Generate key insights, frameworks
└────────┬───────────┘
         │  structured insights
         ▼
┌────────────────────────────────────┐
│   Two outputs:                     │
│                                    │
│  ① → Custom AI Brain               │  ← New knowledge chunk ingested
│      (RAG update)                  │
│                                    │
│  ② → MasterClaw                    │  ← Informs content strategy
│      (content ideas)               │  ← "We should make a video on X"
└────────────────────────────────────┘

Human touchpoints: Selecting which videos to process
Automation: Could auto-process bookmarked YouTube playlists
```

---

## 🔄 HOW THE WHOLE SYSTEM FEEDS ITSELF

```
                    ┌─────────────────┐
                    │   NATE's IDEAS  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
              ┌────▶│  MasterClaw     │◀────┐
              │     │  (orchestrator) │     │
              │     └────────┬────────┘     │
              │              │              │
         Insights         Builds        Lead data
              │              │              │
              │     ┌────────┴────────┐     │
              │     │  Claude Code    │     │
              │     │  (builder)      │     │
              │     └────────┬────────┘     │
              │              │              │
         Learning         Content         Sales
              │              │              │
    ┌─────────┴──┐   ┌───────┴──────┐  ┌───┴────────┐
    │NotebookLM  │   │  Blotato     │  │    GHL     │
    │AI Brain    │   │  (publish)   │  │  (leads)   │
    └────────────┘   └──────────────┘  └────────────┘
                              │
                    ┌─────────┴──────────┐
                    │  All Platforms     │
                    │  → Audience grows  │
                    │  → More leads      │
                    │  → More learning   │
                    └────────────────────┘
```

---

## 📋 QUICK REFERENCE — WHERE EACH TOOL LIVES

| Layer | Tools |
|-------|-------|
| **Talk to Nate** | MasterClaw via WhatsApp |
| **Build things** | Claude Code (terminal), Make.com (no-code) |
| **Create video** | Remotion, Seedance, HeyGen |
| **Create audio** | ElevenLabs |
| **Create AI faces** | Nana Banana |
| **Find media** | Pexels API |
| **Research hooks** | Go Viral Bro (in Claude Code) |
| **Transcribe** | yt-dlp → Groq Whisper |
| **Research/summarize** | NotebookLM |
| **Store knowledge** | Custom AI Brain (RAG) |
| **Publish everywhere** | Blotato |
| **Capture leads** | GHL |
| **Sell products** | Gumroad |
| **Host community** | Skool |

---

*Update this file whenever a new tool is added to the stack.*
*Maintained by MasterClaw 🦞*
