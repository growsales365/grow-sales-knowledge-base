# How to Set Up Remotion with Claude Code

## Written Guide

### What You'll Build
A working Remotion project on your Mac, configured with TailwindCSS and Agent Skills, with Claude Code ready to generate your first video automatically.

---

### Prerequisites
- Node.js installed (see `how-to-install-nodejs-on-mac.md` if you haven't done this)
- Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- A terminal (Terminal.app or iTerm2)

---

### Step 1: Create Your Remotion Project

Open your terminal and run:

```bash
npx create-video@latest
```

You'll be prompted to choose a template. Select:
- **Template:** Blank
- **Extras:** TailwindCSS ✓ and Agent Skills ✓ (use spacebar to toggle)
- **Project name:** anything you like (e.g., `my-videos`)

Hit Enter and let it install.

---

### Step 2: Start the Dev Server

Navigate into your project folder:

```bash
cd my-videos
npm run dev
```

Your browser will open at `http://localhost:3000`. You'll see the Remotion Studio — a preview player where your video renders live as you edit code.

Keep this terminal running.

---

### Step 3: Open Claude Code in the Same Directory

Open a **second terminal tab**, navigate to the same project folder:

```bash
cd my-videos
claude
```

Claude Code will start up inside your project. It can now read and write all your Remotion source files.

---

### Step 4: Prompt Claude Code to Build Your First Video

Try this prompt:

```
Build me a 30-second vertical video (9:16) that introduces my brand. 
Use TailwindCSS classes. Include:
- Scene 1 (0-10s): Big bold headline text fades in on a dark background
- Scene 2 (10-20s): Three bullet points animate in one by one
- Scene 3 (20-30s): Call to action with my website URL
Brand name: [YOUR BRAND]
Website: [YOUR URL]
Color scheme: dark background, white text, purple accents
```

Claude Code will create/edit your `src/` files. Watch the Remotion Studio live-update as it builds.

---

### Step 5: Render Your Video

Once you're happy with the preview:

```bash
npx remotion render
```

Your video exports to the `out/` folder as an `.mp4` file ready for posting.

---

### Tips
- **Iterate fast:** Tell Claude Code "make the headline bigger" or "change the background to navy blue" and it updates instantly.
- **Agent Skills** let Claude understand Remotion's API natively — it won't hallucinate wrong APIs.
- **TailwindCSS** means you describe styles in plain English and Claude translates them correctly.

---

## Video Script (9:16 Vertical, ~60 seconds)

**Format:** Remotion motion graphics, dark background, code terminal aesthetic  
**Aspect Ratio:** 1080x1920  
**Duration:** 60 seconds  

---

### Scene 1 — Hook (0:00–0:05)
**Visual:** Black screen, single line of white text types in like a terminal  
**Text:** `"What if AI built your videos for you?"`  
**Subtext:** None  
**Animation:** Typewriter effect, cursor blinks  
**Audio cue:** Subtle keyboard click SFX  

---

### Scene 2 — Problem (0:05–0:12)
**Visual:** Split — terminal on left showing `npx` error, confused emoji on right  
**Text:** `"Making videos manually = 4 hours per post"`  
**Subtext:** Small text below: "There's a better way 👇"  
**Animation:** Text slides up from bottom  

---

### Scene 3 — Solution Intro (0:12–0:18)
**Visual:** Remotion + Claude Code logos appear side by side  
**Text:** `"Remotion + Claude Code"`  
**Subtext:** `"AI-powered video generation in minutes"`  
**Animation:** Logos drop in with bounce, then text fades up  

---

### Scene 4 — Step 1 (0:18–0:27)
**Visual:** Terminal window, command types itself out  
**Code shown:** `npx create-video@latest`  
**Text overlay:** `"Step 1: Create your project"`  
**Subtext:** `"Choose: Blank + TailwindCSS + Agent Skills"`  
**Animation:** Terminal lines appear one by one  

---

### Scene 5 — Step 2 (0:27–0:38)
**Visual:** Screen recording-style mockup of Remotion Studio preview  
**Text:** `"Step 2: Start dev server → npm run dev"`  
**Subtext:** `"Live preview updates as AI edits your code"`  
**Animation:** Mockup scales in, preview "plays"  

---

### Scene 6 — Step 3 (0:38–0:50)
**Visual:** Claude Code terminal with a prompt being typed  
**Text:** `"Step 3: Tell Claude what to build"`  
**Code shown:** `"Build me a 30-second intro video..."`  
**Subtext:** `"Watch it generate your video in real time"`  
**Animation:** Text streams in like AI output  

---

### Scene 7 — Payoff (0:50–0:57)
**Visual:** Final rendered video frame glows, then export command runs  
**Text:** `"npx remotion render → done ✅"`  
**Subtext:** `"From idea to .mp4 in under 5 minutes"`  
**Animation:** Checkmark pulses, screen brightens  

---

### Scene 8 — CTA (0:57–1:00)
**Visual:** Clean card, avatar/logo  
**Text:** `"Follow for daily AI automation tips"`  
**Subtext:** `"Link in bio for the full setup guide"`  
**Animation:** Card slides up, subtle pulse on follow text  

---

## Publishing Notes

**Caption:**
> What if AI could build your videos for you? 🤖✨ Here's how I set up Remotion + Claude Code to generate motion graphics automatically — from a single prompt. Step-by-step in the comments 👇 #AIVideo #ClaudeCode #Remotion #ContentAutomation #VideoEditing

**Hashtags:**
`#AIVideo #ClaudeCode #Remotion #ContentAutomation #VideoEditing #TechTutorial #AITools #CreatorTools #NoCodeVideo #AutomateEverything`

**Platform Recommendations:**
- **TikTok** — Primary (tech audience loves automation content)
- **Instagram Reels** — Strong secondary
- **YouTube Shorts** — Good for SEO longevity
- **LinkedIn** — Works well for "productivity/AI tools" angle

**Best Post Time:** Tuesday–Thursday, 9–11am or 7–9pm local audience timezone
