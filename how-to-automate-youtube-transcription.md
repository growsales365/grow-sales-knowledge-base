# How to Automate YouTube Transcription

## Written Guide

### What This Does
Automatically downloads the transcript (captions) from any YouTube video using `yt-dlp`, then saves it as a text file you can feed into your AI pipeline — for summaries, repurposed content, or research.

---

### The Problem: YouTube Blocks Server IPs

If you're running this on a cloud server (AWS, DigitalOcean, Hetzner, etc.), YouTube will often return errors like:

```
ERROR: Sign in to confirm you're not a bot
ERROR: HTTP Error 429: Too Many Requests
```

This happens because YouTube detects datacenter IP addresses and blocks them. Your home or office IP works fine — servers don't.

There are two solutions:

---

### Solution 1: Browser Cookies (Quick Fix)

YouTube trusts requests that come with a valid browser session cookie. You can export yours and pass it to `yt-dlp`.

#### Install the Extension
1. In Chrome, install **"Get cookies.txt LOCALLY"** from the Chrome Web Store
2. Navigate to **youtube.com** and make sure you're logged in
3. Click the extension icon
4. Select **"Export"** → saves a `cookies.txt` file to your Downloads folder

#### Upload to Your Server
```bash
scp ~/Downloads/cookies.txt user@your-server:/path/to/project/
```

#### Use with yt-dlp
```bash
yt-dlp --cookies cookies.txt --write-auto-sub --skip-download \
  --sub-format vtt --output "%(id)s.%(ext)s" \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Limitation:** Cookies expire. You'll need to re-export every few weeks or when YouTube forces a re-login.

---

### Solution 2: Groq Whisper API (Permanent Fix)

Instead of fighting YouTube's blocks, download the audio file first, then transcribe it using Groq's blazing-fast Whisper API. No cookies needed, ever.

#### How It Works
1. `yt-dlp` downloads the audio (works even on server IPs for most videos)
2. Groq Whisper transcribes the audio to text in seconds
3. Transcript saved as `.txt` or `.json`

#### Install Dependencies
```bash
pip install yt-dlp
npm install groq  # or pip install groq for Python
```

#### Download Audio Only
```bash
yt-dlp -f "bestaudio" --extract-audio --audio-format mp3 \
  -o "audio.%(ext)s" "https://www.youtube.com/watch?v=VIDEO_ID"
```

#### Transcribe with Groq
```javascript
import Groq from "groq-sdk";
import fs from "fs";

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });

const transcription = await groq.audio.transcriptions.create({
  file: fs.createReadStream("audio.mp3"),
  model: "whisper-large-v3",
  response_format: "text",
});

fs.writeFileSync("transcript.txt", transcription);
console.log("Saved to transcript.txt");
```

**Cost:** Groq Whisper is extremely cheap — roughly $0.111 per hour of audio. A 10-minute video costs about $0.02.

---

### How yt-dlp Pulls Auto-Captions

YouTube auto-generates captions for most videos. `yt-dlp` can pull these directly without transcribing:

```bash
yt-dlp --write-auto-sub --skip-download \
  --sub-lang en --sub-format vtt \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

This downloads the `.vtt` (WebVTT) caption file. To convert to plain text, strip the timestamps:

```bash
yt-dlp --write-auto-sub --skip-download --sub-lang en \
  --convert-subs srt -o "%(title)s" \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

### Where Transcripts Are Saved

By default, `yt-dlp` saves files in your current working directory. To specify a path:

```bash
yt-dlp --write-auto-sub --skip-download \
  -o "/path/to/transcripts/%(upload_date)s-%(title)s.%(ext)s" \
  "URL"
```

For the OpenClaw content pipeline, transcripts are saved to:
```
/root/.openclaw/workspace/content-pipeline/transcripts/
```

---

### Choosing Between the Two Solutions

| | Cookies Method | Groq Whisper |
|---|---|---|
| **Setup time** | 5 minutes | 15 minutes |
| **Reliability** | Breaks when cookies expire | Always works |
| **Cost** | Free | ~$0.02/video |
| **Speed** | Fast (pre-made captions) | Fast (Groq is ~10x realtime) |
| **Best for** | Quick one-off use | Automation at scale |

**Recommendation:** Use cookies for quick manual runs. Use Groq Whisper for any automated pipeline.

---

## Video Script (9:16 Vertical, ~60 seconds)

**Format:** Split-screen terminal + annotation style, dark theme  
**Aspect Ratio:** 1080x1920  
**Duration:** 60 seconds  

---

### Scene 1 — Hook (0:00–0:05)
**Visual:** Red error text on dark terminal  
**Text:** `"Sign in to confirm you're not a bot"`  
**Subtext:** `"YouTube hates your server. Here's the fix."`  
**Animation:** Error text flickers, red pulse border  

---

### Scene 2 — Why It Happens (0:05–0:12)
**Visual:** Simple map diagram — Server IP → YouTube → ❌ / Home IP → YouTube → ✅  
**Text:** `"Datacenter IPs = instant block"`  
**Subtext:** `"AWS, DigitalOcean, Hetzner — all flagged"`  
**Animation:** Diagram draws itself with animated arrows  

---

### Scene 3 — Two Solutions (0:12–0:17)
**Visual:** Two cards side by side  
**Card 1:** 🍪 "Cookies Method"  
**Card 2:** ⚡ "Groq Whisper"  
**Text:** `"Two ways to fix it"`  
**Animation:** Cards flip in  

---

### Scene 4 — Solution 1 (0:17–0:30)
**Visual:** Chrome browser mockup, extension highlighted  
**Text:** `"Fix #1: Export your browser cookies"`  
**Steps shown:**
- Install "Get cookies.txt LOCALLY" in Chrome
- Go to youtube.com (logged in)
- Export → cookies.txt
- Pass to yt-dlp: `--cookies cookies.txt`

**Subtext:** `"Works immediately. Expires in a few weeks."`  
**Animation:** Steps appear one by one with checkmarks  

---

### Scene 5 — Solution 2 (0:30–0:45)
**Visual:** Code snippet, clean syntax highlighting  
**Text:** `"Fix #2: Groq Whisper (permanent)"`  
**Code shown:**
```
yt-dlp -f bestaudio → audio.mp3
groq.transcriptions.create(audio.mp3)
→ transcript.txt ✅
```
**Subtext:** `"~$0.02 per video. No cookies. Never breaks."`  
**Animation:** Code types in, then output file "appears" with glow  

---

### Scene 6 — Where Files Go (0:45–0:52)
**Visual:** File tree visual  
**Text:** `"Transcripts saved to:"`  
**Path shown:** `/content-pipeline/transcripts/`  
**Subtext:** `"Date + title + .txt — ready for your AI pipeline"`  
**Animation:** File tree expands, file highlights  

---

### Scene 7 — Which to Use (0:52–0:57)
**Visual:** Quick comparison card  
**Text:**
- Cookies = quick tests ✓
- Groq = automation at scale ✓

**Animation:** Two rows slide in  

---

### Scene 8 — CTA (0:57–1:00)
**Visual:** Clean branded card  
**Text:** `"Follow for the full AI content pipeline series"`  
**Animation:** Slide up  

---

## Publishing Notes

**Caption:**
> YouTube keeps blocking your server? 😤 Here are 2 ways to automate transcription — browser cookies for quick use, Groq Whisper for permanent automation. Second method costs ~$0.02 per video and never breaks. Full code in comments 👇 #YouTubeAutomation #AITools #ytdlp

**Hashtags:**
`#YouTubeAutomation #AITools #ytdlp #PythonAutomation #ContentCreator #WhisperAI #Groq #TranscriptionTool #ContentPipeline #DevTips`

**Platform Recommendations:**
- **TikTok** — Strong for developer automation content
- **YouTube Shorts** — Meta/recursive appeal (YouTube tutorial about YouTube)
- **Twitter/X** — Good for sharing the code snippet angle
- **LinkedIn** — Works for "AI workflow" professional audience

**Best Post Time:** Tuesday–Wednesday, late morning
