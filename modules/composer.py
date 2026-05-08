"""Composer module.
Assembles final MP4 from audio and clips.
"""
import os

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip, TextClip, ColorClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip, concatenate_videoclips


class Composer:
    def __init__(self, config):
        self.config = config

    def create_caption(self, text, duration, fontsize=70, color='yellow'):
        """Creates a stylized caption for the Short."""
        return TextClip(
            text,
            fontsize=fontsize,
            color=color,
            font='Arial-Bold',
            method='caption',
            size=(720 * 0.8, None) # 80% of width
        ).set_duration(duration).set_position(('center', 'center'))

    def build_video(self, video_path, audio_path, script_data, filename):
        """
        Assembles all pieces into the final MP4.
        'script_data' should be a dictionary with hook, body, and twist.
        """
        # 1. Load Assets
        audio = AudioFileClip(audio_path)
        background = VideoFileClip(video_path).loop(duration=audio.duration)
        
        # 2. Sync Audio & Video
        background = background.set_audio(audio)
        
        # 3. Generate Dynamic Captions
        # For simplicity, we split the captions by the three sections
        # In a pro version, you'd use word-level timestamps
        section_duration = audio.duration / 3
        
        caption1 = self.create_caption(script_data['hook'], section_duration).set_start(0)
        caption2 = self.create_caption(script_data['body'], section_duration).set_start(section_duration)
        caption3 = self.create_caption(script_data['twist'], section_duration).set_start(section_duration * 2)

        # 4. Composite the Layers
        final_video = CompositeVideoClip([background, caption1, caption2, caption3])
        
        # 5. Write Output
        output_path = self.config.paths["final"] / filename
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        output_path = os.path.join(self.output_dir, filename)
        final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
        
        return output_path



# --- Integration Logic ---
def assemble_final_short(video, audio, data, name):
    composer = Composer()
    return composer.build_video(video, audio, data, name)