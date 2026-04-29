# How to Install Node.js on Mac

## Written Guide

### Why This Matters
If you've ever tried to run `npx` or `npm` and got an error like `command not found: npx`, it's because Node.js isn't installed on your Mac. Node.js is the runtime that powers nearly every modern JavaScript tool — including Remotion, Claude Code, and most AI automation workflows.

This guide walks you through the cleanest, most reliable way to install it.

---

### Why `npx` Fails Without Node

`npx` is bundled with Node.js. When you run `npx create-video@latest` or any similar command, your terminal looks for Node in your system PATH. If it's not there, you get:

```
zsh: command not found: npx
```

or

```
zsh: command not found: node
```

The fix is simple — install Node. Here's the right way to do it on a Mac.

---

### Step 1: Install Homebrew

Homebrew is a package manager for Mac. It's the easiest way to install developer tools. If you already have it, skip this step.

Open **Terminal** (Cmd + Space → type "Terminal") and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

It'll ask for your Mac password. Type it (nothing shows — that's normal) and press Enter. Installation takes 1–3 minutes.

When it's done, you may see a message like:
```
==> Next steps:
Add Homebrew to your PATH
```

If so, run the two `echo` and `eval` lines it shows you (they look like):
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

This makes `brew` available in your terminal.

---

### Step 2: Install Node.js

Now install Node via Homebrew:

```bash
brew install node
```

This installs both `node` and `npm` (Node Package Manager) and `npx`. It takes about a minute.

---

### Step 3: Verify the Installation

Check that everything installed correctly:

```bash
node --version
```
Expected output: something like `v22.4.0` (any v18+ is fine)

```bash
npm --version
```
Expected output: something like `10.7.0`

```bash
npx --version
```
Expected output: same version as npm

If you see version numbers — you're done! ✅

---

### Troubleshooting

**Still getting "command not found" after install?**

Your terminal session might be using old PATH settings. Close the terminal completely and reopen it. Then try again.

**On an older Mac with Intel chip?**

Homebrew installs to `/usr/local/` instead of `/opt/homebrew/`. Everything else works the same.

**Want to manage multiple Node versions?**

Use `nvm` (Node Version Manager) instead of Homebrew. Run:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
Then: `nvm install --lts`

---

### What's Next?
With Node installed, you can now:
- Run `npx create-video@latest` to start a Remotion project
- Install Claude Code: `npm install -g @anthropic-ai/claude-code`
- Use any npm package in the JavaScript ecosystem

---

## Video Script (9:16 Vertical, ~60 seconds)

**Format:** Terminal screen-capture style, clean dark aesthetic  
**Aspect Ratio:** 1080x1920  
**Duration:** 60 seconds  

---

### Scene 1 — Hook (0:00–0:05)
**Visual:** Red error text on black terminal background  
**Text:** `"zsh: command not found: npx"`  
**Subtext:** `"This trips up EVERYONE starting out"`  
**Animation:** Text flickers in like a real terminal error, then red glow  

---

### Scene 2 — Explain the Problem (0:05–0:12)
**Visual:** Simple diagram — "npx" arrow pointing to "Node.js" with a ❌  
**Text:** `"npx needs Node.js to run"`  
**Subtext:** `"Node isn't installed on Macs by default"`  
**Animation:** Diagram draws itself left to right  

---

### Scene 3 — Solution (0:12–0:17)
**Visual:** Clean white card, two logos: Homebrew 🍺 → Node.js  
**Text:** `"2-step fix"`  
**Subtext:** `"Takes about 3 minutes"`  
**Animation:** Cards pop in with satisfying bounce  

---

### Scene 4 — Step 1: Homebrew (0:17–0:30)
**Visual:** Terminal window, long install command types itself out  
**Code:** `/bin/bash -c "$(curl -fsSL https://...install.sh)"`  
**Text overlay:** `"Step 1: Install Homebrew"`  
**Subtext:** `"Mac's package manager — install it once, use forever"`  
**Animation:** Command types character by character, then loading bar pulses  

---

### Scene 5 — Step 2: Node (0:30–0:40)
**Visual:** New terminal, short command  
**Code:** `brew install node`  
**Text overlay:** `"Step 2: brew install node"`  
**Subtext:** `"That's literally it"`  
**Animation:** Command types in, progress bar appears, then ✅  

---

### Scene 6 — Verify (0:40–0:52)
**Visual:** Terminal shows two commands and their outputs  
**Code:**
```
node --version → v22.4.0 ✅
npm --version  → 10.7.0  ✅
```
**Text overlay:** `"Check it worked"`  
**Subtext:** `"Any version above 18 is fine"`  
**Animation:** Each line appears with a satisfying green checkmark  

---

### Scene 7 — What's Unlocked (0:52–0:57)
**Visual:** Icons for Remotion, Claude Code, npm packages flying in  
**Text:** `"Now you can build anything"`  
**Subtext:** `"Remotion, Claude Code, any npm package"`  
**Animation:** Icons zoom in from center, scattered layout  

---

### Scene 8 — CTA (0:57–1:00)
**Visual:** Clean card  
**Text:** `"Follow for the full Remotion + AI setup series"`  
**Animation:** Slide up, subtle glow  

---

## Publishing Notes

**Caption:**
> Getting "command not found: npx"? Here's the fix 🛠️ Install Node.js on Mac in 2 steps — takes 3 minutes. This is the foundation for Remotion, Claude Code, and basically every AI tool worth using. Save this! #NodeJS #MacSetup #WebDev

**Hashtags:**
`#NodeJS #MacSetup #WebDevelopment #Homebrew #JavaScriptTips #DevTools #TechTutorial #CodingForBeginners #AITools #Remotion`

**Platform Recommendations:**
- **TikTok** — Great for beginners searching dev tutorials
- **YouTube Shorts** — High SEO value ("how to install node mac")
- **Instagram Reels** — Works well as part of a dev tools series
- **Pinterest** — Surprisingly good for tech how-tos with clear steps

**Best Post Time:** Weekday mornings (8–10am) — people hit this error when they sit down to code
