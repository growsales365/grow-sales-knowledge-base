---
name: youtube-transcribe
description: Transcribe YouTube videos to text using yt-dlp and browser cookies. Use when Nate sends YouTube URLs and wants transcripts saved, asks to "transcribe this video", "save this transcript", or "pull the transcript for this". Also handles cookie refresh when YouTube blocks the server. Cookies are stored at /root/.openclaw/workspace/content-pipeline/youtube-cookies.txt and must come from a youtube.com browser tab.
---

# YouTube Transcribe

Transcribes YouTube videos to text using yt-dlp with browser cookies to bypass AWS IP blocks.

## Quick Start

1. Check if valid cookies exist: `ls -la /root/.openclaw/workspace/content-pipeline/youtube-cookies.txt`
2. Run transcription script for each URL
3. Save cleaned transcript to `/root/.openclaw/workspace/content-pipeline/transcripts/<video-id>.txt`

## Transcription Script

```bash
# Pull auto-captions (free, works for ~90% of videos)
yt-dlp --write-auto-sub --sub-lang en --skip-download \
  --cookies /root/.openclaw/workspace/content-pipeline/youtube-cookies.txt \
  -o "/root/.openclaw/workspace/content-pipeline/transcripts/%(id)s" \
  "YOUTUBE_URL"

# Convert .vtt to clean text
python3 /root/.openclaw/workspace/content-pipeline/vtt_to_text.py \
  "/root/.openclaw/workspace/content-pipeline/transcripts/VIDEO_ID.en.vtt"
```

## When Cookies Are Missing or Expired

YouTube blocks this server's AWS IP. Cookies from Nate's browser are required.

Tell Nate:
> "I need fresh YouTube cookies to pull transcripts. On your Mac:
> 1. Open Chrome → go to **youtube.com** (must be this tab, logged in)
> 2. Click the **'Get cookies.txt LOCALLY'** extension
> 3. Export → send me the `youtube-cookies.txt` file"

Save received file to: `/root/.openclaw/workspace/content-pipeline/youtube-cookies.txt`

## Pending Queue

URLs waiting for transcription are in:
`/root/.openclaw/workspace/content-pipeline/transcripts/pending-transcribe.txt`

Always check this file and batch-process all pending URLs when cookies are available.

## Saving Transcripts

- Save each transcript as: `/root/.openclaw/workspace/content-pipeline/transcripts/<video-id>.txt`
- Update `pending-transcribe.txt` to remove completed URLs
- Confirm to Nate how many were transcribed and where they're saved

## Groq Whisper Alternative (no cookies needed)

If Nate provides a Groq API key (console.groq.com), use `scripts/groq_transcribe.py` instead — no cookies ever needed. See references/groq-setup.md for setup.
