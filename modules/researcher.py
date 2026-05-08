"""Researcher module.
Scrapes facts from Gemini or Perplexity.
"""
from google import genai
from google.genai import types
import requests
import random

class Researcher:
    def __init__(self, config):
        self.config = config
        gem_api_key = self.config.api_keys["gemini"]
        self.ninjas_api_key = self.config.api_keys["api_ninjas"]
        self.client = genai.Client(api_key=gem_api_key)
        self.model_id = "gemini-3-flash-preview" # Current 2026 workhorse


    def get_dark_topics(self, limit=1):
        """
        Fetches historical events based on a 'dark' keyword.
        """
        dark_keywords = ["unsolved", "mystery", "conspiracy", "execution", "ghost", "disappearance"]
        current_keyword = random.choice(dark_keywords)
        print(f"Selected keyword for research: {current_keyword}")
        headers = {'X-Api-Key': self.ninjas_api_key}
        params = {'text': current_keyword, 'limit': limit}

        base_url = 'https://api.api-ninjas.com/v1/historicalevents'

        try:
            response = requests.get(base_url, params=params, headers=headers)
            response.raise_for_status()
            
            events = response.json()
            # API-Ninjas returns a list of objects: [{'year', 'month', 'day', 'event'}]
            return events[0]  # Return top event
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching from API-Ninjas: {e}")
            return []
        

    def get_viral_script(self):

        """Uses Gemini to research and format a script into JSON."""
        
        dark_topics = self.get_dark_topics()
        print(f"Dark topics: {dark_topics}")
        # return "All good"
        if dark_topics:
            date_str = f"{dark_topics['month']}/{dark_topics['day']}/{dark_topics['year']}"
            topic = dark_topics['event']
            print(f"Selected topic: {topic} on {date_str}")
        else:
            date_str = "Unknown date"
            print(f"No dark topics found, using provided topic: {topic}")
        
        # We use System Instructions to force JSON output without a wrapper
        sys_instruct = "You are a viral history documentarian. Always return response in JSON."
        
        prompt = f"""
        Research the topic: '{topic}' which happened on {date_str}.
        Create a 50-second dark history script with:
        1. Start the script with the date: {date_str}.
        2. A 'hook' that stops the scroll.
        3. A 'script body' with 3 disturbing facts.
        4. A 'twist' or question at the end.
        5. A 'visual_prompt' for an AI video generator (cinematic, moody).
        """

        response = self.client.models.generate_content(
            model=self.model_id,
            config=types.GenerateContentConfig(
                system_instruction=sys_instruct,
                response_mime_type="application/json" 
            ),
            contents=prompt
        )
        
        return response.text


# if __name__ == "__main__":
#     import sys
#     from pathlib import Path

#     repo_root = Path(__file__).resolve().parent.parent
#     sys.path.insert(0, str(repo_root))

#     from config import Config

#     r = Researcher(Config())
#     print(r.get_viral_script())