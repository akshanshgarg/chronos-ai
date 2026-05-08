"""Visualizer module.
Generates background clips using video generation APIs.
"""

import requests
import random
import os
# from moviepy.editor import VideoFileClip


class Visualizer:
    def __init__(self, config):
        self.config = config
        self.pexels_url = "https://api.pexels.com/videos/search"

    def get_stock_background(self, query, clip_name="temp_bg3.mp4"):
        """Fetches a free vertical video from Pexels based on the topic."""
        headers = {"Authorization": self.config.api_keys["PEXELS_API_KEY"]}
        params = {
            "query": query,
            "orientation": "portrait", # 9:16 for Shorts
            "per_page": 5
        }
        

        response = requests.get(self.pexels_url, headers=headers, params=params)
        data = response.json()
        

        output_path = self.config.paths["clips"] / clip_name
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if data.get('videos'):
            selected_video = random.choice(data['videos'])
            # Get the link for the HD mobile version
            video_url = selected_video['video_files'][0]['link']
            
            # Download the file
            r = requests.get(video_url, stream=True)
            with open(output_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk: f.write(chunk)
            
            print(f"Background video downloaded: {output_path}")
            return output_path
        else:
            print("No videos found for this query.")
            return None

    # def process_for_shorts(self, input_path, duration=58):
    #     """Trims the video to fit the Shorts time limit."""
    #     clip = VideoFileClip(input_path).subclip(0, duration)
    #     # Final formatting could be added here
    #     return clip


