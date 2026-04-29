#!/usr/bin/env python3
"""
Transcribe YouTube videos using Groq Whisper API.
No cookies needed — works from any IP.
Usage: python3 groq_transcribe.py <youtube_url> [--api-key KEY]
"""

import sys
import os
import subprocess
import tempfile
import argparse

def transcribe_with_groq(youtube_url: str, api_key: str, output_dir: str = None):
    """Download audio from YouTube and transcribe with Groq Whisper."""
    if not output_dir:
        output_dir = "/root/.openclaw/workspace/content-pipeline/transcripts"
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract video ID
    video_id = youtube_url.split("v=")[-1].split("&")[0].split("/")[-1].split("?")[0]
    
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_path = os.path.join(tmpdir, f"{video_id}.mp3")
        
        print(f"Downloading audio for {video_id}...")
        result = subprocess.run([
            "yt-dlp", "-x", "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", audio_path,
            youtube_url
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error downloading: {result.stderr}")
            sys.exit(1)
        
        print("Transcribing with Groq Whisper...")
        try:
            from groq import Groq
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", "groq", "--break-system-packages", "-q"])
            from groq import Groq
        
        client = Groq(api_key=api_key)
        
        with open(audio_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-large-v3",
                file=audio_file,
                response_format="text"
            )
        
        output_path = os.path.join(output_dir, f"{video_id}.txt")
        with open(output_path, "w") as f:
            f.write(transcription)
        
        print(f"Saved to: {output_path}")
        print(f"Length: {len(transcription)} characters")
        return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe YouTube video with Groq Whisper")
    parser.add_argument("url", help="YouTube URL")
    parser.add_argument("--api-key", default=os.environ.get("GROQ_API_KEY"), help="Groq API key")
    args = parser.parse_args()
    
    if not args.api_key:
        print("Error: Groq API key required. Pass --api-key or set GROQ_API_KEY env var.")
        sys.exit(1)
    
    transcribe_with_groq(args.url, args.api_key)
