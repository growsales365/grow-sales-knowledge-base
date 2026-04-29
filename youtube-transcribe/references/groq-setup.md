# Groq Whisper Setup

Groq offers free Whisper transcription — no cookies, no IP blocks, works from the server.

## Setup (one time)

1. Nate signs up at **console.groq.com**
2. Creates an API key
3. Sends the key to MasterClaw
4. Save key to server: `echo "GROQ_API_KEY=your_key_here" >> /root/.openclaw/workspace/.env`

## Usage

```bash
python3 /root/.openclaw/workspace/skills/youtube-transcribe/scripts/groq_transcribe.py \
  "https://youtu.be/VIDEO_ID" \
  --api-key $GROQ_API_KEY
```

## Pricing

- Free tier: 7,200 seconds/day (~2 hours of audio)
- Paid: $0.111/hour beyond free tier
- A 10-minute video costs ~$0.02 on paid tier

## Why This Is Better Than Cookies

- No browser extension needed
- Works from iPhone (just tell me a URL)
- Never expires
- Can batch-process unlimited videos
- Faster than yt-dlp caption method
