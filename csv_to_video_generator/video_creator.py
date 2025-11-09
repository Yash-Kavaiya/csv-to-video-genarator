import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, VideoFileClip, concatenate_videoclips

class GyanDariyoVideoCreator:
    def __init__(self, data_list, image_width=1920, image_height=1080, background_color=(255, 229, 244), font_color=(229, 0, 135), font_size=90, line_spacing=10, margin=80, default_fps=24):
        self.data_list = data_list
        self.image_width = image_width
        self.image_height = image_height
        self.background_color = background_color
        self.font_color = font_color
        self.font_size = font_size
        self.line_spacing = line_spacing
        self.margin = margin
        self.default_fps = default_fps

    def create_images(self):
        for idx, data in enumerate(self.data_list):
            image = Image.new("RGB", (self.image_width, self.image_height), self.background_color)
            draw = ImageDraw.Draw(image)

            # Try to load font with fallback options
            try:
                font = ImageFont.truetype("HindVadodara-SemiBold.ttf", self.font_size)
            except OSError:
                # Try system fonts as fallback
                font_paths = [
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                ]
                font = None
                for font_path in font_paths:
                    try:
                        font = ImageFont.truetype(font_path, self.font_size)
                        break
                    except OSError:
                        continue
                if font is None:
                    print("Warning: Using default font")
                    font = ImageFont.load_default()

            y_position = self.margin

            for text in data:
                wrapped_text = textwrap.fill(text, width=40)
                lines = wrapped_text.split('\n')

                for line in lines:
                    draw.text((self.margin, y_position), line, font=font, fill=self.font_color)
                    y_position += self.font_size + self.line_spacing

                y_position += self.line_spacing

            image.save(f"Gyan_Dariyo_image_{idx+1}.png")
            image.show()

    def create_audio(self):
        for idx, data in enumerate(self.data_list):
            text_to_speak = "\n".join(data)
            tts = gTTS(text=text_to_speak, lang='gu')
            audio_file_path = f"Gyan_Dariyo_audio_{idx+1}.mp3"
            tts.save(audio_file_path)

    def create_videos(self):
        video_list = []
        for idx, data in enumerate(self.data_list):
            text_to_speak = "\n".join(data)
            tts = gTTS(text=text_to_speak, lang='gu')
            audio_file_path = f"Gyan_Dariyo_audio_{idx+1}.mp3"
            tts.save(audio_file_path)

            audio_clip = AudioFileClip(audio_file_path)
            audio_duration = audio_clip.duration

            image_path = f"Gyan_Dariyo_image_{idx+1}.png"
            image_clip = ImageClip(image_path)
            video_clip = image_clip.set_audio(audio_clip).set_duration(audio_duration).set_fps(self.default_fps)

            video_file_path = f"Gyan_Dariyo_video_{idx+1}.mp4"
            video_list.append(video_file_path)
            video_clip.write_videofile(video_file_path, codec="libx264", audio_codec="aac")

        return video_list

    def create_final_video(self, video_list):
        video_clips = [VideoFileClip(video) for video in video_list]
        final_video = concatenate_videoclips(video_clips)
        final_video_file_path = "Gyan_Dariyo_final_video.mp4"
        final_video.write_videofile(final_video_file_path, codec="libx264", audio_codec="aac")
        return final_video_file_path
