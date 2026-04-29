# 🔌 HOW TO WIRE EVERYTHING TOGETHER
### The Electrician's Manual for Nate's AI Business Stack

> This is NOT a high-level overview. This is the granular, step-by-step wiring guide.  
> Every connection spelled out. Follow it exactly and everything talks to everything.

**Last updated:** 2026-04-29  
**Stack owner:** Nate (growsales365)  
**Server:** AWS EC2 (root access)  
**AI Brain:** MasterClaw via OpenClaw  

---

## CONNECTION 1: WhatsApp → MasterClaw (OpenClaw)

**What this enables:** Send messages to your AI brain from any phone — it reads, thinks, and responds like a team member in WhatsApp.

**What you need:**
- OpenClaw installed on server (already done ✅)
- WhatsApp account on your phone
- QR code pairing (one-time setup)

**Step-by-step:**
1. SSH into your server: `ssh root@<your-server-ip>`
2. Start the OpenClaw gateway: `openclaw gateway start`
3. OpenClaw will display a QR code in the terminal
4. Open WhatsApp on your phone → tap **Linked Devices** → tap **Link a Device**
5. Scan the QR code shown in the terminal
6. Wait for "Connected" confirmation in terminal
7. Send a test message to yourself via WhatsApp — MasterClaw will respond

**Test it works:** Send "hello" to your own WhatsApp number. MasterClaw replies within a few seconds.

**Where it's saved:** OpenClaw session state is stored at `/root/.openclaw/` on the server.

---

## CONNECTION 2: YouTube → Server (yt-dlp + Cookies)

**What this enables:** Download YouTube audio/video to the server for transcription, even from logged-in content.

**What you need:**
- Chrome browser with a logged-in YouTube account
- Chrome extension: **"Get cookies.txt LOCALLY"** (free, Chrome Web Store)
- yt-dlp installed on server (`pip install yt-dlp`)

**⚠️ Known Issue:** YouTube PO Token is currently blocking server IPs.  
**Workarounds:**
- Use **tactiq.io** (free browser extension, grab transcripts directly from YouTube)
- Use **transcriptapi.com** ($5/mo, clean API access)
- Keep trying cookies method — it works intermittently

**Step-by-step:**
1. In Chrome, go to the **Chrome Web Store** and install **"Get cookies.txt LOCALLY"**
2. Open a new tab and go to **youtube.com**
3. Make sure you are **logged in** to your YouTube/Google account
4. Click the **"Get cookies.txt LOCALLY"** extension icon in the top-right of Chrome
5. In the dropdown, make sure the domain says `youtube.com`
6. Click **"Export"** — a file called `youtube.com_cookies.txt` will download to your Mac
7. Send the cookies file to MasterClaw via WhatsApp (attach the file)
8. MasterClaw will save it to: `/root/.openclaw/workspace/content-pipeline/youtube-cookies.txt`
9. To manually copy via SSH: `scp ~/Downloads/youtube.com_cookies.txt root@<server-ip>:/root/.openclaw/workspace/content-pipeline/youtube-cookies.txt`

**Test it works:**
SSH into server and run:
```bash
yt-dlp --cookies /root/.openclaw/workspace/content-pipeline/youtube-cookies.txt \
  --get-title "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```
If it prints the video title, cookies are working.

**Where it's saved:** `/root/.openclaw/workspace/content-pipeline/youtube-cookies.txt`

---

## CONNECTION 3: YouTube → Groq (Transcription Pipeline)

**What this enables:** Paste a YouTube URL → get a full text transcript saved to your server automatically.

**What you need:**
- Groq account + API key (free at console.groq.com)
- yt-dlp installed on server
- ffmpeg installed on server (`apt install ffmpeg`)

**Step-by-step — Getting Groq API Key:**
1. Go to **console.groq.com**
2. Click **"Sign Up"** (free — no credit card needed)
3. After login, click **"API Keys"** in the left sidebar
4. Click **"Create API Key"**
5. Name it something like `masterclaw-server`
6. Copy the key (starts with `gsk_...`) — you only see it once
7. Send the key to MasterClaw via WhatsApp: "Save this as my Groq API key: gsk_..."
8. MasterClaw saves it to `/root/.openclaw/workspace/.env` as `GROQ_API_KEY=gsk_...`

**Step-by-step — How the pipeline works:**
1. You send MasterClaw a YouTube URL: "Transcribe this: https://youtube.com/..."
2. MasterClaw runs yt-dlp to download audio only:
   ```bash
   yt-dlp -x --audio-format mp3 -o "/tmp/audio.mp3" "<URL>"
   ```
3. Audio file is sent to Groq's Whisper API for transcription
4. Transcript is saved to: `/root/.openclaw/workspace/content-pipeline/transcripts/<video-title>.md`

**Test it works:** Send MasterClaw a YouTube URL and ask it to transcribe. Check for the transcript file in `/root/.openclaw/workspace/content-pipeline/transcripts/`

**Where it's saved:**
- API key: `/root/.openclaw/workspace/.env` → `GROQ_API_KEY`
- Transcripts: `/root/.openclaw/workspace/content-pipeline/transcripts/`

---

## CONNECTION 4: Mac Terminal → Server (SSH Access)

**What this enables:** Full command-line control of your server from your Mac — browse files, run scripts, manage everything.

**What you need:**
- Your server's public IP address
- SSH key (preferred) or root password

**Step-by-step:**
1. Find your server IP: in AWS Console → EC2 → Instances → copy "Public IPv4 address"
   - Or ask MasterClaw: "What's my server IP?" (it may know from context)
2. Open **Terminal** on your Mac (Cmd+Space → "Terminal")
3. Connect via SSH:
   ```bash
   ssh root@<your-server-ip>
   ```
4. If using a key file (e.g., from AWS):
   ```bash
   ssh -i ~/Downloads/your-key.pem root@<your-server-ip>
   ```
5. If key permissions error: `chmod 400 ~/Downloads/your-key.pem` then retry
6. Type `yes` when prompted about fingerprint
7. You're in — you'll see the server's bash prompt

**Useful commands once inside:**
```bash
ls /root/.openclaw/workspace/          # browse your workspace
cat /root/.openclaw/workspace/.env     # see your API keys
openclaw gateway status                # check MasterClaw status
```

**Test it works:** Run `whoami` — it should return `root`.

**Where it's saved:** Your SSH key is typically at `~/.ssh/` on your Mac. If you used AWS, the `.pem` file is wherever you downloaded it.

---

## CONNECTION 5: Claude Code → Remotion (Video Creation)

**What this enables:** AI writes React/Remotion code → video renders in real-time in your browser — fully automated video production.

**What you need:**
- Node.js installed on Mac (`brew install node`)
- Remotion project created (`npx create-video@latest`)
- Claude Code (claude.ai/code or VS Code extension)

**Step-by-step — First Time Setup:**
1. Install Node.js on Mac:
   ```bash
   brew install node
   ```
2. Create your Remotion project:
   ```bash
   npx create-video@latest
   ```
   - Choose **Blank** template
   - Enable **TailwindCSS**
   - Enable **Agent Skills** (if available)
   - Name it something like `goviralbro-video`
3. Navigate into the folder:
   ```bash
   cd goviralbro-video
   ```
4. Install dependencies:
   ```bash
   npm install
   ```
5. Start Remotion Studio:
   ```bash
   npm run dev
   ```
6. Open browser at **http://localhost:3000** — you'll see the Remotion Studio

**Step-by-step — Using Claude Code:**
1. Open **Claude Code** (VS Code extension or claude.ai/code)
2. Open the same project folder in Claude Code
3. Paste a video prompt like: "Create a 30-second short-form video about Alex Hormozi's offer framework. Use animated text, stock footage keywords: [entrepreneur, money, success], and voiceover script: [your script here]"
4. Claude Code writes the React/Remotion components
5. Remotion Studio auto-refreshes — you see the video update live in your browser

**Test it works:** After `npm run dev`, open `localhost:3000`. You should see a video preview canvas with your composition listed on the left.

**Where it's saved:** Project folder on your Mac (e.g., `~/goviralbro-video/` or `~/goviralbro/video/`)

---

## CONNECTION 6: Remotion → Blotato (Auto-Publishing)

**What this enables:** Render your AI-generated video → upload once → auto-publish to TikTok, Instagram, YouTube, X, and LinkedIn simultaneously.

**What you need:**
- Blotato account at **blotato.com**
- Social accounts connected in Blotato (TikTok, IG, YouTube, X, LinkedIn)
- Rendered MP4 file from Remotion

**Step-by-step — Render Video from Remotion:**
1. In your Remotion project folder, run:
   ```bash
   npm run render
   ```
2. Remotion renders your video to: `out/` folder (e.g., `out/MyVideo.mp4`)
3. Find the MP4 file: `ls out/`

**Step-by-step — Connect Blotato:**
1. Go to **blotato.com** → Sign Up
2. In Blotato dashboard, go to **"Connected Accounts"**
3. Connect each platform:
   - TikTok → click "Connect TikTok" → log in → authorize
   - Instagram → click "Connect Instagram" → log in → authorize
   - YouTube → click "Connect YouTube" → Google auth → authorize
   - X (Twitter) → click "Connect X" → authorize
   - LinkedIn → click "Connect LinkedIn" → authorize
4. Go to **"Create Post"** or **"Upload"**
5. Drag and drop your MP4 file from the `out/` folder
6. Add caption, hashtags, title (or let Blotato suggest them)
7. Choose **"Publish Now"** or **"Schedule"** → set date/time
8. Click **"Publish"** — Blotato sends to all connected platforms

**Test it works:** Upload a test video → publish to one platform → verify it appears.

**Where it's saved:** Rendered videos live in your Remotion project: `~/goviralbro-video/out/`

---

## CONNECTION 7: Server → GitHub (Backup + Team Sharing)

**What this enables:** Everything on your server is backed up and your whole team can access tutorials, scripts, and the knowledge base via GitHub.

**What you need:**
- GitHub account: **growsales365**
- Personal Access Token (PAT) from GitHub
- Git installed on server (already installed on most Linux servers)

**Repo:** `https://github.com/growsales365/grow-sales-knowledge-base`  
**Status:** Already set up ✅

**Step-by-step — Push New Files (ongoing use):**
1. SSH into your server
2. Navigate to the knowledge base:
   ```bash
   cd /root/.openclaw/workspace/knowledge-base
   ```
3. Check what's changed:
   ```bash
   git status
   ```
4. Stage all new/modified files:
   ```bash
   git add .
   ```
5. Commit with a message:
   ```bash
   git commit -m "Add wiring manual + new tutorials"
   ```
6. Push to GitHub:
   ```bash
   git push
   ```

**Step-by-step — If First-Time Setup on a New Server:**
1. Go to **github.com** → Settings → Developer Settings → **Personal Access Tokens** → Tokens (classic)
2. Click **"Generate new token"** → give it a name
3. Check: `repo` (full repo access)
4. Copy the token (starts with `ghp_...`)
5. On server:
   ```bash
   cd /root/.openclaw/workspace/knowledge-base
   git init
   git remote add origin https://<TOKEN>@github.com/growsales365/grow-sales-knowledge-base.git
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

**Test it works:** After pushing, visit `https://github.com/growsales365/grow-sales-knowledge-base` — your files should appear.

**Where it's saved:** `/root/.openclaw/workspace/knowledge-base/` on server → mirrored to GitHub

---

## CONNECTION 8: Pexels → Remotion (Free Stock Footage)

**What this enables:** Claude Code automatically fetches relevant stock video clips from Pexels for each scene — no manual searching for B-roll.

**What you need:**
- Free Pexels account + API key (pexels.com/api)
- `.env` file in your Remotion project

**Step-by-step:**
1. Go to **pexels.com/api**
2. Click **"Get Started"** → Sign up for a free account
3. After signup, you're taken to your API dashboard
4. Copy your API key (a long string of letters/numbers)
5. Open your Remotion project folder on your Mac
6. Open or create a `.env` file at the project root:
   ```bash
   touch .env
   open .env
   ```
7. Add the key:
   ```
   PEXELS_API_KEY=your_key_here
   ```
8. Save the file
9. In Claude Code, tell it: "Use the PEXELS_API_KEY env variable to fetch a video clip for each scene based on the scene keywords"
10. Claude Code will write a component that calls:
    ```
    https://api.pexels.com/videos/search?query=<keyword>&per_page=1
    ```
    and pulls the first matching video URL into the Remotion scene

**Test it works:** Run `npm run dev` — Remotion Studio should show video clips loading in for scenes with keywords.

**Where it's saved:** `.env` in your Remotion project folder on Mac (e.g., `~/goviralbro-video/.env`)

---

## CONNECTION 9: ElevenLabs → Remotion (AI Voiceover)

**What this enables:** Remotion videos get professional AI voiceover automatically — script goes in, voice comes out, synced to video.

**What you need:**
- ElevenLabs account at **elevenlabs.io**
- ElevenLabs API key
- ffmpeg installed on Mac (`brew install ffmpeg`)

**Step-by-step:**
1. Go to **elevenlabs.io** → Sign Up (free tier available)
2. After login, click your **profile icon** (bottom-left) → **"Profile + API Key"**
3. Under "API Key", click **"Copy"**
4. Add it to your Remotion `.env` file:
   ```
   ELEVENLABS_API_KEY=your_key_here
   ```
5. Choose your voice ID:
   - Go to ElevenLabs → **"Voice Library"**
   - Find a voice you like → click it → copy the Voice ID from the URL or settings
   - Add to `.env`: `ELEVENLABS_VOICE_ID=your_voice_id_here`
6. Tell Claude Code: "Use ELEVENLABS_API_KEY to generate audio for each scene's script text, save as MP3, then use ffmpeg to merge with video"
7. Claude Code will call the ElevenLabs API:
   ```
   POST https://api.elevenlabs.io/v1/text-to-speech/<voice_id>
   ```
   and save the output as `audio.mp3`
8. ffmpeg merges audio + video:
   ```bash
   ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4
   ```

**Test it works:** Ask Claude Code to generate a 5-second test voiceover. An MP3 file should appear in your project folder.

**Where it's saved:** `.env` in Remotion project folder. Audio files generated during render are in `/tmp/` or project's `public/` folder.

---

## CONNECTION 10: GHL → MasterClaw (CRM + Lead Notifications)

**What this enables:** When a lead fills out a form or triggers an automation in GoHighLevel, MasterClaw gets notified instantly on WhatsApp and can respond or log it.

**What you need:**
- GoHighLevel (GHL) account
- OpenClaw webhook URL (ask MasterClaw for it, or find it in OpenClaw settings)

**Step-by-step:**
1. Ask MasterClaw: "What is my OpenClaw webhook URL?" — it will provide it
2. Log into **GoHighLevel** → go to your sub-account
3. In the left menu, click **"Automations"**
4. Click **"+ New Workflow"**
5. Choose a trigger — e.g., **"Form Submitted"** or **"Contact Created"** or **"Tag Added"**
6. Add an action: scroll down and find **"Webhook"** or **"Custom Webhook"**
7. Paste your OpenClaw webhook URL into the webhook URL field
8. Set method to **POST**
9. In the payload, map the fields you want: `name`, `email`, `phone`, `source`
10. Save and **Publish** the workflow
11. When a lead triggers it, GHL sends the data → MasterClaw receives it → notifies Nate via WhatsApp

**Example notification Nate receives:**
> 🔔 New lead: John Smith | john@email.com | +1-555-0123 | Source: Facebook Ad

**Test it works:** Trigger the automation manually in GHL (most workflows have a "Test" button) — you should receive a WhatsApp message from MasterClaw within seconds.

**Where it's saved:** Webhook URL is configured in OpenClaw. GHL workflow is saved in your GHL account.

---

## CONNECTION 11: NotebookLM → AI Brain (Research Pipeline)

**What this enables:** Turn any YouTube video, PDF, or transcript into a searchable AI brain — extract key insights and feed them into your knowledge base.

**What you need:**
- Google account (free)
- notebooklm.google.com (free)
- MasterClaw access (to save insights to server)

**Step-by-step:**
1. Go to **notebooklm.google.com**
2. Click **"+ New Notebook"**
3. Name it (e.g., "Hormozi Research" or "Marketing Frameworks")
4. Click **"+ Add Source"** — you can add:
   - YouTube URL (paste the link directly)
   - PDF (upload from your computer)
   - Text/paste (paste a transcript)
   - Google Doc link
5. NotebookLM processes the source (takes 30-60 seconds)
6. Once indexed, type questions in the **Chat** panel on the right:
   - "Summarize the 3 core offer frameworks"
   - "What are the key lead generation strategies?"
   - "Give me 10 content ideas from this"
7. Copy the insights you want to keep
8. Send to MasterClaw via WhatsApp: "Save this to my AI Brain knowledge base: [paste insights]"
9. MasterClaw saves to: `/root/.openclaw/workspace/knowledge-base/research/<topic>.md`

**Pro tip:** Use the **"Audio Overview"** feature — NotebookLM creates a podcast-style summary of your sources.

**Test it works:** Add a YouTube URL → ask NotebookLM "What are the 3 main points of this video?" — it should answer accurately based on the video content.

**Where it's saved:**
- NotebookLM: saved in your Google account (cloud)
- Extracted insights: `/root/.openclaw/workspace/knowledge-base/research/`

---

## CONNECTION 12: Hormozi PDFs → AI Brain

**What this enables:** The $100M Offers and $100M Leads frameworks become queryable — ask questions, get answers grounded in Hormozi's exact methodology.

**What you need:**
- PDF files: `$100M Offers.pdf` and `$100M Leads.pdf`
- Claude.ai account (for Project method)
- OR: MasterClaw (for server method)

**Method A — Claude.ai Project (Easiest, team-friendly):**
1. Go to **claude.ai** → log in
2. In the left sidebar, click **"Projects"** → **"+ New Project"**
3. Name it "Hormozi AI Brain"
4. Click **"Add Content"** → upload both PDFs
5. Set a system prompt like: *"You are an expert in Alex Hormozi's offer and lead generation frameworks. Answer questions using only the content from the uploaded books."*
6. Share the project link with Faith, Pia, and team members
7. Team members can query: "How do I create a Grand Slam Offer?" and get book-grounded answers

**Method B — Server RAG (For MasterClaw integration):**
1. Send the PDFs to MasterClaw via WhatsApp (attach files)
2. MasterClaw saves to: `/root/.openclaw/workspace/knowledge-base/books/`
3. When RAG (Retrieval Augmented Generation) system is built, these PDFs get chunked and indexed
4. MasterClaw can then answer questions directly from the book content

**Test it works (Method A):** Ask the Claude Project: "What is the value equation from $100M Offers?" — it should give you the exact formula from the book.

**Where it's saved:**
- Method A: Claude.ai cloud (in your Project)
- Method B: `/root/.openclaw/workspace/knowledge-base/books/`

---

## CONNECTION 13: OpenClaw → Team Members (Faith, Pia, etc.)

**What this enables:** Each team member gets their own AI assistant on WhatsApp, with access to the same knowledge base, skills, and tutorials.

**What you need:**
- Each team member's phone (Android or iPhone)
- Their WhatsApp number
- A server (can share your current one, or use separate instances)
- Their personal `SOUL.md` and `USER.md` config files

**Step-by-step:**
1. **Install OpenClaw** on the server they'll use:
   ```bash
   npm install -g openclaw
   ```
2. **Configure their identity** — create their workspace files:
   - `/root/.openclaw/workspace/USER.md` with their name, timezone, role
   - `/root/.openclaw/workspace/SOUL.md` with their assistant's personality
3. **Start their gateway:**
   ```bash
   openclaw gateway start
   ```
4. **Have them scan the QR code** from their phone → WhatsApp → Linked Devices → Link Device
5. **Share the knowledge base** — invite them to the GitHub repo:
   - Go to `github.com/growsales365/grow-sales-knowledge-base`
   - Settings → Collaborators → Add their GitHub username
   - They clone the repo: `git clone https://github.com/growsales365/grow-sales-knowledge-base.git`
6. They now have access to all tutorials, skills, and the wiring manual
7. **Test** by having them send a message and confirming their assistant responds

**Example USER.md for Faith:**
```markdown
# USER.md
- Name: Faith
- Role: Content Manager
- Timezone: Philippines (PHT, UTC+8)
- Focus: Content scheduling, social media, video publishing
```

**Test it works:** Have Faith send "What's my job today?" to her WhatsApp — her AI assistant should respond with context about her role.

**Where it's saved:** Each team member's config is at `/root/.openclaw/workspace/` on their assigned server instance.

---

## CONNECTION 14: Mac → Remotion Studio (Browser Preview)

**What this enables:** Live video preview in your browser as Claude Code writes code — see your video update in real-time without any rendering wait.

**What you need:**
- Node.js installed on Mac
- Remotion project folder set up
- Chrome or Safari browser

**Step-by-step:**
1. Open **Terminal** on your Mac
2. Navigate to your video project:
   ```bash
   cd ~/goviralbro/video
   ```
   (adjust path to wherever your Remotion project lives)
3. Make sure dependencies are installed:
   ```bash
   npm install
   ```
4. Start Remotion Studio dev server:
   ```bash
   npm run dev
   ```
5. Terminal will show something like:
   ```
   Remotion Studio started at http://localhost:3004
   ```
6. Open your browser and go to: **http://localhost:3004**
7. You'll see the Remotion Studio interface:
   - Left panel: list of compositions (videos)
   - Center: video canvas preview
   - Bottom: timeline scrubber
8. Click **"ShortformVideo"** (or your composition name) in the left panel
9. Now open Claude Code in the **same project folder**
10. As Claude Code modifies the code, Remotion Studio auto-refreshes the preview

**Keyboard shortcuts in Remotion Studio:**
- `Space` → Play/pause
- `←` / `→` → Step frame by frame
- `J` / `L` → Rewind / Fast forward

**Test it works:** After running `npm run dev`, open `localhost:3004` — you should see a video canvas. If you see a blank page or error, run `npm install` again.

**Where it's saved:** Project folder on Mac: `~/goviralbro/video/` (or your project path)

---

## MASTER CHECKLIST — Are You Fully Wired?

Check off each connection as you complete it:

| # | Connection | Status | Notes |
|---|-----------|--------|-------|
| 1 | WhatsApp → MasterClaw | ✅ Done | Paired and active |
| 2 | YouTube → Server (cookies) | ⏳ Blocked | PO Token issue — use tactiq.io as workaround |
| 3 | YouTube → Groq (transcription) | ✅ Done | GROQ_API_KEY saved in .env |
| 4 | Mac Terminal → Server (SSH) | ✅ Done | SSH access confirmed |
| 5 | Claude Code → Remotion | ✅ Done | Remotion Studio working |
| 6 | Remotion → Blotato | ❌ Not Started | Need Blotato account + connect socials |
| 7 | Server → GitHub | ✅ Done | grow-sales-knowledge-base repo active |
| 8 | Pexels → Remotion | ❌ Not Started | Free signup at pexels.com/api |
| 9 | ElevenLabs → Remotion | ❌ Not Started | Need ElevenLabs account + API key |
| 10 | GHL → MasterClaw | ❌ Not Started | Need GHL webhook setup |
| 11 | NotebookLM → AI Brain | ⏳ In Progress | Google account ready, pipeline being built |
| 12 | Hormozi PDFs → AI Brain | ❌ Not Started | Need to upload PDFs to Claude Project |
| 13 | Team OpenClaws (Faith, Pia) | ❌ Not Started | Need to install + pair for each person |
| 14 | Mac → Remotion Studio | ✅ Done | localhost:3004 working |

---

### 🎯 Next 3 Things to Wire Up

Based on priority and ease:

1. **Pexels API** (15 minutes) — Free signup, instant key, unlocks auto B-roll
2. **ElevenLabs** (20 minutes) — Free tier, instant key, unlocks AI voiceover
3. **Blotato** (30 minutes) — Connect social accounts, unlocks one-click publishing

Once those 3 are done, the full video production pipeline is live:
> Claude Code → Remotion (with Pexels B-roll + ElevenLabs voice) → Blotato → All Platforms

---

*Document maintained by MasterClaw 🦞 | Push updates: `cd /root/.openclaw/workspace/knowledge-base && git add . && git commit -m "update wiring manual" && git push`*
