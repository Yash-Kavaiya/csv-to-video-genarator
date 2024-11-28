import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import numpy as np
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto
from gtts import gTTS
import logging
from pathlib import Path
import tempfile
import shutil
from functools import lru_cache

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContentPhase(Enum):
    """Enumeration for content progression phases"""
    INITIAL = auto()
    QUESTION = auto()
    OPTIONS = auto()
    ANSWER = auto()
    EXPLANATION = auto()
    COMPLETE = auto()

@dataclass
class VideoConfig:
    """Configuration for video generation parameters"""
    width: int = 1080
    height: int = 1920
    fps: int = 30
    background_color: Tuple[int, int, int] = (255, 240, 245)
    text_color: Tuple[int, int, int] = (0, 0, 0)
    font_size_title: int = 48
    font_size_options: int = 40
    font_size_answer: int = 44
    font_size_explanation: int = 36
    font_paths: List[str] = field(default_factory=lambda: [
        "/content/Roboto-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    ])
    # Add smooth transition parameters
    transition_duration: float = 0.5
    hold_frame_duration: float = 0.2

@dataclass
class AudioConfig:
    """Audio processing configuration"""
    language: str = 'en'
    tld: str = 'com'
    sample_rate: int = 44100
    channels: int = 2
    codec: str = 'aac'
    bitrate: str = '192k'

class VideoGenerator:
    def __init__(self, video_config: VideoConfig, audio_config: AudioConfig):
        self.video_config = video_config
        self.audio_config = audio_config
        self.temp_dir = Path(tempfile.mkdtemp())
        
    def cleanup(self):
        """Clean up temporary resources"""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def _get_font(self, size: int) -> ImageFont.FreeTypeFont:
        """Get font with fallback options"""
        for font_path in self.video_config.font_paths:
            try:
                return ImageFont.truetype(font_path, size)
            except OSError:
                continue
        return ImageFont.load_default()

    def create_frame(self, question: str, options: List[str], 
                    answer: str = "", explanation: str = "", 
                    show_answer: bool = False) -> np.ndarray:
        """Create a single frame with all content"""
        img = Image.new('RGB', (self.video_config.width, self.video_config.height), 
                       self.video_config.background_color)
        draw = ImageDraw.Draw(img)
        
        # Layout configuration
        margin = int(self.video_config.width * 0.1)
        max_width = self.video_config.width - (2 * margin)
        y_pos = int(self.video_config.height * 0.15)

        # Render question
        question_font = self._get_font(self.video_config.font_size_title)
        y_pos = self._render_text_block(draw, question, y_pos, 
                                      question_font, max_width)

        # Render options with spacing
        if options:
            y_pos = int(self.video_config.height * 0.35)
            options_font = self._get_font(self.video_config.font_size_options)
            for option in options:
                y_pos = self._render_text_block(draw, option, y_pos, 
                                              options_font, max_width) + 20

        # Render answer and explanation if needed
        if show_answer:
            if answer:
                y_pos = int(self.video_config.height * 0.65)
                answer_font = self._get_font(self.video_config.font_size_answer)
                y_pos = self._render_text_block(draw, f"Answer: {answer}", 
                                              y_pos, answer_font, max_width)

            if explanation:
                y_pos = int(self.video_config.height * 0.75)
                explanation_font = self._get_font(self.video_config.font_size_explanation)
                self._render_text_block(draw, explanation, y_pos, 
                                      explanation_font, max_width)

        return np.array(img)

    def _render_text_block(self, draw: ImageDraw.Draw, text: str, 
                          y_pos: int, font: ImageFont.FreeTypeFont, 
                          max_width: int) -> int:
        """Render text block with improved layout and anti-aliasing"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = font.getbbox(test_line)
            if bbox[2] <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))

        for line in lines:
            bbox = font.getbbox(line)
            line_width = bbox[2] - bbox[0]
            x_pos = (self.video_config.width - line_width) // 2
            
            # Draw text with anti-aliasing
            draw.text((x_pos, y_pos), line, 
                     font=font, fill=self.video_config.text_color)
            y_pos += bbox[3] - bbox[1] + 10

        return y_pos

    async def generate_video(self, data: List[str]) -> str:
        """Generate video with smooth transitions"""
        question, options, answer, explanation = data[0], data[1:5], data[5], data[6]
        output_path = str(self.temp_dir / "output.mp4")
        
        try:
            clips = []
            current_time = 0.0

            # Create base frames
            question_frame = self.create_frame(question, [], "", "")
            options_frame = self.create_frame(question, options, "", "")
            answer_frame = self.create_frame(question, options, answer, "", True)
            final_frame = self.create_frame(question, options, answer, explanation, True)

            # Generate TTS audio for each segment
            segments = [
                (question, question_frame),
                *[(opt, options_frame) for opt in options],
                (answer, answer_frame),
                (explanation, final_frame)
            ]

            for i, (text, frame) in enumerate(segments):
                # Generate audio
                audio_path = str(self.temp_dir / f"audio_{i}.mp3")
                tts = gTTS(text=text, lang=self.audio_config.language,
                          tld=self.audio_config.tld)
                tts.save(audio_path)
                audio_clip = AudioFileClip(audio_path)
                
                # Create video clip with smooth transitions
                duration = audio_clip.duration + self.video_config.hold_frame_duration
                video_clip = ImageClip(frame).set_duration(duration)
                
                # Apply fade transitions
                if clips:
                    video_clip = video_clip.crossfadein(self.video_config.transition_duration)
                
                # Combine audio and video
                final_clip = video_clip.set_audio(audio_clip)
                final_clip = final_clip.set_start(current_time)
                clips.append(final_clip)
                
                current_time += duration - self.video_config.transition_duration

            # Composite final video
            final_video = CompositeVideoClip(clips)
            final_video.write_videofile(
                output_path,
                fps=self.video_config.fps,
                codec='libx264',
                audio_codec=self.audio_config.codec,
                audio_bitrate=self.audio_config.bitrate,
                threads=4,
                preset='medium'
            )

            return output_path

        except Exception as e:
            logger.error(f"Video generation error: {e}", exc_info=True)
            raise

async def main(data_list: List[List[str]]) -> None:
    """Main execution function"""
    video_config = VideoConfig()
    audio_config = AudioConfig()
    generator = VideoGenerator(video_config, audio_config)
    
    try:
        for i, data in enumerate(data_list, 1):
            output_path = await generator.generate_video(data)
            final_path = f"output_video_{i}.mp4"
            shutil.move(output_path, final_path)
            logger.info(f"Generated video: {final_path}")
    finally:
        generator.cleanup()

if __name__ == "__main__":
    test_data = [
        ["What is the primary goal of artificial intelligence?",
         "A. Replicating human intelligence",
         "B. Solving complex problems",
         "C. Automating tasks",
         "D. Enhancing decision-making processes",
         "Answer: Replicating human intelligence",
         "Explanation: The primary goal of AI is to create systems that can perform tasks that typically require human intelligence."]
    ]
    
    import asyncio
    asyncio.run(main(test_data))
