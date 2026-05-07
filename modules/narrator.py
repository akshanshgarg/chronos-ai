"""Narrator module.
Generates voice narration from text using Edge-TTS.
"""

import asyncio
from pathlib import Path
import edge_tts


class Narrator:
    def __init__(self, config):
        self.config = config

    def generate_voice(self, facts):
        """Generate narration audio from facts and return the output path."""
        output_path = self.config.paths["audio"] / "narration.mp3"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        text = " ".join(facts)
        asyncio.run(self._generate_voice(text, output_path))
        return output_path

    async def _generate_voice(self, text, output):
        communicate = edge_tts.Communicate(text, "en-US-ChristopherNeural")
        await communicate.save(str(output))
