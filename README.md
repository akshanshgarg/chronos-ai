# Chronos AI

A lightweight orchestrator for generating short-form video content from research, narration, visuals, and composition logic.

## Overview

`Chronos AI` is a proof-of-concept project that stitches together:

- historical/topic research via Gemini/API-Ninjas
- voice narration using Edge-TTS
- video background generation via Pexels
- final MP4 composition with MoviePy

The current implementation is designed to read a prepared script JSON file and assemble the final video from existing audio and clip assets.

## Features

- `main.py` orchestrates the workflow
- `modules/researcher.py` can generate a viral-style script using Gemini and API-Ninjas
- `modules/narrator.py` can produce an audio narration file using Edge-TTS
- `modules/visualizer.py` can download stock background video clips from Pexels
- `modules/composer.py` combines audio, video, and captions into a final MP4

## Requirements

- Python 3.11+ (recommended)
- `moviepy`
- `requests`
- `python-dotenv`
- `edge-tts`
- `pandas`
- `genai`

## Setup

1. Clone the repository.
2. Create a Python virtual environment.

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Create a `.env` file at the repository root containing API keys:

```env
GEMINI_API_KEY=your_gemini_api_key
api_ninjas=your_api_ninjas_api_key
PEXELS_API_KEY=your_pexels_api_key
EDGE_TTS_API_KEY=your_edge_tts_api_key
KLING_API_KEY=your_kling_api_key
STABLE_VIDEO_API_KEY=your_stable_video_api_key
```

5. Ensure the required asset folders exist if they are not already created:

- `data/`
- `data/audio/`
- `data/clips/`
- `data/final/`

## Usage

Currently, `main.py` loads `data/script.json`, then builds the final video using `modules/composer.py`.

```bash
python main.py
```

### Current runtime flow

- `main.py` reads `data/script.json`
- `Composer.build_video()` expects:
  - `data/audio/main_audio.mp3`
  - `data/clips/bg.mp4`
- Output is written to `data/final/final_video.mp4`

## Project Structure

- `main.py` - Orchestrator
- `config.py` - Configuration and path management
- `modules/researcher.py` - Script generation and research
- `modules/narrator.py` - Text-to-speech narration
- `modules/visualizer.py` - Video background acquisition
- `modules/composer.py` - Final video composition
- `requirements.txt` - Python dependencies

## Notes

- The research, narration, and visualizer stages are currently commented out in `main.py` for local testing.
- The composer currently uses a simple 3-part caption split based on audio duration.
- Add or update `data/script.json` with a script containing `hook`, `script_body`, and `twist`.

## Example `data/script.json`

```json
{
  "hook": "This forgotten secret changed history.",
  "script_body": "In 1923, a hidden message was discovered inside the museum walls. Experts still debate why it was never published.",
  "twist": "What would you do if the truth surfaced today?"
}
```

## Future Enhancements

- enable full end-to-end research, narration, and visual generation
- add clip trimming and format control for vertical Shorts
- improve caption timing accuracy with subtitles or transcript timestamps
- add error handling for missing assets and API failures
