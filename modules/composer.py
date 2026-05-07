"""Composer module.
Assembles final MP4 from audio and clips.
"""

class Composer:
    def __init__(self, config):
        self.config = config

    def assemble_video(self, narration_audio, clips):
        """Compose and save final MP4 video."""
        output_path = self.config.paths["final"] / "final_video.mp4"
        return output_path
