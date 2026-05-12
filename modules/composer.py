"""Composer module.
Assembles final MP4 from audio and clips.
"""
import os

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import TextClip, ColorClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip, concatenate_videoclips


class Composer:
    def __init__(self, config):
        self.config = config

    def create_caption(self, text, duration, fontsize=70, color='yellow'):
        """Creates a stylized caption for the Short."""
        return TextClip(
            text=text,
            font_size=fontsize,
            color=color,
            size=(int(720 * 0.8), None), # 80% of width,
            method ='caption',
            duration=duration
        )

    def build_video(self, script_data, filename):
        """
        Assembles all pieces into the final MP4.
        'script_data' should be a dictionary with hook, body, and twist.
        """
        # 1. Load Assets
        audio_path = self.config.paths["audio"] / "main_audio.mp3"
        video_path = self.config.paths["clips"] / "bg.mp4"

        audio = AudioFileClip(audio_path)
        background = VideoFileClip(video_path).with_duration(audio.duration)
        
        # 2. Sync Audio & Video
        background = background.with_audio(audio)
        
        # 3. Generate Dynamic Captions
        # For simplicity, we split the captions by the three sections
        # In a pro version, you'd use word-level timestamps
        section_duration = audio.duration / 3
        
        caption1 = self.create_caption(script_data['hook'], section_duration).with_start(0)
        caption2 = self.create_caption(script_data['script_body'], section_duration).with_start(section_duration)
        caption3 = self.create_caption(script_data['twist'], section_duration).with_start(section_duration * 2)

        # 4. Composite the Layers
        final_video = CompositeVideoClip([background, caption1, caption2, caption3])
        
        # 5. Write Output
        output_path = self.config.paths["final"] / filename
        self.config.paths["final"].mkdir(parents=True, exist_ok=True)
        final_video.write_videofile(str(output_path), fps=24, codec="libx264", audio_codec="aac")
        
        return output_path



# # --- Integration Logic ---
# def assemble_final_short(data, name):
#     composer = Composer()
#     return composer.build_video(data, name)