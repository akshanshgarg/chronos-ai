"""Chronos AI configuration.
Contains API keys, style settings, and asset paths.
"""

import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv(Path(__file__).parent / ".env")


class Config:
    def __init__(self):
        self.api_keys = {
            "gemini": os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY"),
            "api_ninjas": os.getenv("api_ninjas", "YOUR_API_NINJAS_API_KEY"),
            "PEXELS_API_KEY": os.getenv("PEXELS_API_KEY", "YOUR_PEXELS_API_KEY"),
            "edge_tts": os.getenv("EDGE_TTS_API_KEY", "YOUR_EDGE_TTS_API_KEY"),
            "kling": os.getenv("KLING_API_KEY", "YOUR_KLING_API_KEY"),
            "stable_video": os.getenv("STABLE_VIDEO_API_KEY", "YOUR_STABLE_VIDEO_API_KEY"),
        }
        self.style = {
            "voice": "neutral",
            "video_resolution": "1920x1080",
            "frame_rate": 30,
        }
        self.paths = {
            "data": Path(__file__).parent / "data",
            "audio": Path(__file__).parent / "data" / "audio",
            "clips": Path(__file__).parent / "data" / "clips",
            "final": Path(__file__).parent / "data" / "final",
        }
