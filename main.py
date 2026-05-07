"""Chronos AI orchestrator.
Run this script to build a video from research, narration, visuals, and composition.
"""

from modules.researcher import Researcher
from modules.narrator import Narrator
from modules.visualizer import Visualizer
from modules.composer import Composer
from config import Config


def main():
    config = Config()

    researcher = Researcher(config)
    narrator = Narrator(config)
    visualizer = Visualizer(config)
    composer = Composer(config)

    facts = researcher.scrape_facts()
    narration_audio = narrator.generate_voice(facts)
    clips = visualizer.generate_clips(facts)
    composer.assemble_video(narration_audio, clips)


if __name__ == "__main__":
    main()
