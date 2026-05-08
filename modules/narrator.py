"""Narrator module.
Generates voice narration from text using Edge-TTS.
"""

import asyncio
import json
from pathlib import Path
import edge_tts


class Narrator:
    def __init__(self, config):
        self.config = config

    def generate_voice(self, script):
        """Read script JSON from data folder and generate narration audio."""
        
        output_path = self.config.paths["audio"] / "YanNeural.mp3"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Combine hook, body, and twist into narration text
        text_parts = [
            script.get('hook', ''),
            script.get('script_body', ''),
            script.get('twist', '')
        ]
        text = ' '.join(part for part in text_parts if part)
        
        asyncio.run(self._generate_voice(text, output_path))
        print(f"✓ Checkpoint: Audio narration saved to {output_path}")
        return output_path

    async def _generate_voice(self, text, output):
        communicate = edge_tts.Communicate(text, "en-HK-YanNeural")
        await communicate.save(str(output))
