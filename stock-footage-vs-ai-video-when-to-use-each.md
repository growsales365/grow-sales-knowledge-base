# Stock Footage vs AI Video: When to Use Each

## Written Guide

### The Three Tools in Your Video Stack

When building an automated video pipeline, you have three fundamentally different ways to get visuals. Understanding what each one actually does — and doesn't do — saves you money and keeps your content looking right.

---

### Tool 1: Remotion (Motion Graphics)

**What it is:** A code-based video framework. You write React/JavaScript and it renders as a video.

**What it generates:**
- Animated text (headlines, subtitles, counters)
- Geometric shapes and transitions
- Data visualizations, charts, progress bars
- Branded lower-thirds and overlays
- Smooth scene transitions

**What it does NOT do:**
- Generate real-world footage (people, places, objects)
- Pull stock video from anywhere
- Create AI-generated imagery or video

**Best for:**
- Tutorial overlays and explainer content
- News-style text graphics
- Stats and data storytelling
- Branded intros/outros
- Any content where motion graphics ARE the content

**Cost:** Free (open source). Rendering is CPU/GPU on your own machine or server.

---

### Tool 2: Pexels API (Stock Video)

**What it is:** A free stock media library with an API that returns video clips matched to keywords.

**What it generates:**
- Real footage of people, places, nature, objects, lifestyle
- Professional quality, licensed for commercial use
- Searchable by keyword (e.g., "coffee shop", "technology", "beach sunset")

**Integration example:**
```javascript
const response = await fetch(
  `https://api.pexels.com/videos/search?query=${keyword}&per_page=5`,
  { headers: { Authorization: process.env.PEXELS_API_KEY } }
);
const { videos } = await response.json();
const clipUrl = videos[0].video_files[0].link;
```

**Best for:**
- B-roll footage behind voiceover
- Lifestyle content backgrounds
- High-volume content where you need variety fast
- Any "talking head with background" format

**Cost:** Free. Just need a free API key from pexels.com/api.

**Limitations:**
- You don't control exact content — you search and get what exists
- Can't generate something that doesn't exist in their library
- Generic footage can look "stock-y" if overused

---

### Tool 3: Seedance / Runway (AI-Generated Video)

**What they are:** AI video generation platforms. You provide a prompt (or an image), and they generate a realistic or stylized video clip.

**What they generate:**
- Custom scenes that don't exist anywhere else
- AI influencer / digital human content
- Cinematic shots generated from text prompts
- Image-to-video (animate a still photo)

**Best for:**
- AI influencer persona content
- Premium hero clips for ads
- Scenarios impossible to find in stock libraries
- Consistent character-based content (same AI person across videos)

**Cost:** ~$0.50–$2.00 per clip (see `seedance-vs-runway-pricing-breakdown.md` for full breakdown)

---

### Decision Framework: When to Use What

| Situation | Best Tool |
|---|---|
| Daily educational/tutorial content | Remotion + text graphics |
| Lifestyle B-roll for voiceover | Pexels API |
| High-volume content (10+ videos/day) | Remotion + Pexels |
| AI influencer series | Seedance (selectively) |
| Premium brand ad / hero clip | Runway or Seedance |
| Data story / stats breakdown | Remotion only |
| "Someone talking to camera" (no real human) | Seedance AI avatar |

---

### The Smart Stack for Scale

For **daily volume content** (the bread and butter of automation):

```
Remotion (structure + motion graphics)
  + Pexels API (B-roll clips)
  + ElevenLabs (voiceover)
  = Complete video at near-zero cost per video
```

For **premium / AI influencer content** (selective use):

```
Seedance (AI character clips)
  + Remotion (titles + transitions)
  + ElevenLabs (voice)
  = Premium video at ~$1-3 per video
```

**Rule of thumb:** Use AI video generation for the clips that make viewers stop scrolling — not for every single video. Reserve Seedance/Runway for your hero content.

---

### Common Mistake to Avoid

Spending $50/month on Runway to generate B-roll that Pexels would give you for free. AI video generation is a creative tool, not a stock footage replacement. Use it for content that genuinely requires a custom visual that doesn't exist anywhere else.

---

## Video Script (9:16 Vertical, ~60 seconds)

**Format:** Triptych layout (3 panels), clean modern tech aesthetic  
**Aspect Ratio:** 1080x1920  
**Duration:** 60 seconds  

---

### Scene 1 — Hook (0:00–0:06)
**Visual:** Three clips playing simultaneously in a vertical split  
- Left: Code/terminal (Remotion)
- Center: Beautiful beach footage (Pexels)
- Right: AI-generated person talking (Seedance)

**Text overlay:** `"3 ways to get video. Big difference."`  
**Animation:** All three panels fade in at once  

---

### Scene 2 — Tool 1: Remotion (0:06–0:18)
**Visual:** Full screen — Remotion logo, then animated text examples  
**Text:** `"Remotion = motion graphics"`  
**Bullet points appear:**
- ✅ Animated text & shapes
- ✅ Transitions & overlays
- ❌ Not real footage
- ❌ Not AI video

**Subtext:** `"Free. Code-based. Perfect for tutorials."`  
**Animation:** Bullets pop in one by one  

---

### Scene 3 — Tool 2: Pexels (0:18–0:32)
**Visual:** Beautiful Pexels-style footage (lifestyle, nature, city)  
**Text:** `"Pexels API = free stock video"`  
**Bullet points:**
- ✅ Real footage, any keyword
- ✅ Commercial license
- ✅ Free API
- ❌ Generic, can't customize

**Subtext:** `"Best for B-roll at scale. Zero cost."`  
**Animation:** Footage plays softly, bullets slide in  

---

### Scene 4 — Tool 3: AI Video (0:32–0:46)
**Visual:** AI-generated cinematic clip playing  
**Text:** `"Seedance/Runway = AI-generated clips"`  
**Bullet points:**
- ✅ Custom scenes from text prompts
- ✅ AI influencer content
- ✅ Cinematic quality
- ❌ ~$0.50–$2 per clip

**Subtext:** `"Use selectively. This is your scroll-stopper."`  
**Animation:** Clip plays, price tag appears with caution color  

---

### Scene 5 — The Smart Stack (0:46–0:54)
**Visual:** Equation layout  
**Text:**
```
Daily content:
Remotion + Pexels = ~$0/video

Premium content:
Seedance + Remotion = ~$1-3/video
```
**Subtext:** `"Match the tool to the job"`  
**Animation:** Equations build out with connecting arrows  

---

### Scene 6 — Key Rule (0:54–0:58)
**Visual:** Bold text card  
**Text:** `"Don't use AI video for B-roll"`  
**Subtext:** `"That's what Pexels is for 🎬"`  
**Animation:** Text punches in  

---

### Scene 7 — CTA (0:58–1:00)
**Visual:** Clean branded card  
**Text:** `"Follow for the full AI video stack breakdown"`  
**Animation:** Slide up  

---

## Publishing Notes

**Caption:**
> Not all video tools are equal 🎬 Here's when to use Remotion (motion graphics), Pexels (free stock footage), and Seedance/Runway (AI video) — and how to combine them for scale. The wrong tool choice can waste $100s/month. Save this breakdown! #AIVideo #ContentCreation #VideoAutomation

**Hashtags:**
`#AIVideo #ContentCreation #VideoAutomation #Remotion #PexelsAPI #Seedance #RunwayML #CreatorTools #ContentStrategy #VideoMarketing`

**Platform Recommendations:**
- **TikTok** — Great for creators researching tools
- **YouTube Shorts** — Comparison content performs well for search
- **Twitter/X** — The "tool comparison" format gets strong RT engagement
- **LinkedIn** — Excellent for "content strategy at scale" angle

**Best Post Time:** Monday or Thursday, 10am–12pm (planning/strategy mindset)
