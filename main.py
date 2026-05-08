"""Chronos AI orchestrator.
Run this script to build a video from research, narration, visuals, and composition.
"""

import json
from pathlib import Path
from modules.researcher import Researcher
from modules.narrator import Narrator
from modules.visualizer import Visualizer
from modules.composer import Composer
from config import Config


def main():
    config = Config()

    # researcher = Researcher(config)
    # script = researcher.get_viral_script()
    
    # # Save script JSON to data folder for testing
    script_path = config.paths["data"] / "script.json"
    script_path.parent.mkdir(parents=True, exist_ok=True)
    # with open(script_path, 'w') as f:
    #     f.write(script)
    # print(f"✓ Checkpoint: Script saved to {script_path}")
        
    with open(script_path, 'r') as f:
        script_json = f.read()
    script = json.loads(script_json)
    script = script[0]   
    print("checkpoint: Script parsed", script)  # Debug: Print the parsed script
    # narrator = Narrator(config)
    # narration_audio = narrator.generate_voice(script)
    
    
    visualizer = Visualizer(config)
    visual_prompt = script.get('visual_prompt', '')
    visual_prompt = "dark mystery"
    clips = visualizer.get_stock_background(visual_prompt)
    
    # composer = Composer(config)
    # composer.assemble_video(narration_audio, clips)


if __name__ == "__main__":
    main()
