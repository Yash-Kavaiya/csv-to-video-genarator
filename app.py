import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap
from gtts import gTTS
import os

#file_path = '/content/તલાટી અને જુનિયર કલાર્ક મોડેલ પેપર -2 - તલાટી અને જુનિયર કલાર્ક મોડેલ પેપર -2(1).csv'
#data_frame = pd.read_csv(file_path)
#data_list = data_frame.values.tolist()

# data_list = [["કલકત્તામાં એશિયાટિક સોસાયટીની સ્થાપના સમયે બંગાળના ગવર્નર જનરલ કોણ હતા ?", "A. કોનૅવોલીસ", "B. વિલિયમ બેન્ટિક", "C. વોરન હેસ્ટીંગ્સ", "D. વેલેસ્લી", "જવાબ :- વોરન હેસ્ટીંગ્સ", ""],
#     ["સ્વામી વિવેકાનંદ નું મૂળ નામ શું હતું ?", "A. સુરેન્દ્રનાથ", "B. રવીન્દ્રનાથ", "C. રામકૃષ્ણ", "D. નરેન્દ્રનાથ", "જવાબ  નરેન્દ્રનાથ", ""]]
data_list = [
    ["What is the primary goal of artificial intelligence?", 
     "A. Replicating human intelligence", 
     "B. Solving complex problems", 
     "C. Automating tasks", 
     "D. Enhancing decision-making processes", 
     "Answer: Replicating human intelligence", 
     ""],
    ["Which programming language is commonly used for developing AI applications?", 
     "A. Python", 
     "B. Java", 
     "C. C++", 
     "D. JavaScript", 
     "Answer: Python", 
     ""],
    ["What does the acronym 'ML' stand for in the context of AI?", 
     "A. Machine Learning", 
     "B. Memory Loss", 
     "C. Multiple Layers", 
     "D. Mobile Learning", 
     "Answer: Machine Learning", 
     ""],
    ["Which AI technique is used for teaching computers to learn from data?", 
     "A. Neural Networks", 
     "B. Genetic Algorithms", 
     "C. Expert Systems", 
     "D. Reinforcement Learning", 
     "Answer: Machine Learning", 
     ""],
    ["What is the name of the AI system developed by IBM that defeated human champions in the game show Jeopardy!?", 
     "A. Watson", 
     "B. DeepMind", 
     "C. AlphaGo", 
     "D. Siri", 
     "Answer: Watson", 
     ""],
    ["Which subfield of AI focuses on creating systems that can understand and generate human language?", 
     "A. Natural Language Processing (NLP)", 
     "B. Computer Vision", 
     "C. Robotics", 
     "D. Expert Systems", 
     "Answer: Natural Language Processing (NLP)", 
     ""],
    ["What is the process of training a machine learning model with large amounts of data called?", 
     "A. Supervised Learning", 
     "B. Unsupervised Learning", 
     "C. Reinforcement Learning", 
     "D. Deep Learning", 
     "Answer: Deep Learning", 
     ""],
    ["Which company developed the popular deep learning framework TensorFlow?", 
     "A. Google", 
     "B. Facebook", 
     "C. Microsoft", 
     "D. Amazon", 
     "Answer: Google", 
     ""],
    ["What is the term for the ability of an AI system to improve its performance over time without explicit programming?", 
     "A. Machine Learning", 
     "B. Artificial Intelligence", 
     "C. Reinforcement Learning", 
     "D. Self-learning", 
     "Answer: Reinforcement Learning", 
     ""],
    ["What is the name of the AI system developed by OpenAI that achieved superhuman performance in the game Dota 2?", 
     "A. AlphaGo", 
     "B. Watson", 
     "C. AlphaStar", 
     "D. OpenAI Five", 
     "Answer: OpenAI Five", 
     ""]
]


print(data_list)

image_width = 1920
image_height = 1080
background_color = (255, 229, 244)
font_color = (229, 0, 135)
font_size = 90
line_spacing = 10
margin = 80

# for idx, data in enumerate(data_list):
#     image = Image.new("RGB", (image_width, image_height), background_color)
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("./HindVadodara-Bold.ttf", font_size)
#     y_position = margin

#     for text in data:
#         wrapped_text = textwrap.fill(text, width=40)  # Adjust width as needed
#         lines = wrapped_text.split('\n')

#         for line in lines:

#             draw.text((margin, y_position), line, font=font, fill=font_color)
#             y_position += font_size + line_spacing

#         y_position += line_spacing  # Add extra spacing between wrapped lines
#     image.save(f"Gyan_Dariyo_image_{idx+1}.png")
from PIL import Image, ImageDraw, ImageFont
import textwrap
from gtts import gTTS
import os

# data_list = [
#     ["કલકત્તામાં એશિયાટિક સોસાયટીની સ્થાપના સમયે બંગાળના ગવર્નર જનરલ કોણ હતા ?", "A. કોનૅવોલીસ", "B. વિલિયમ બેન્ટિક", "C. વોરન હેસ્ટીંગ્સ", "D. વેલેસ્લી", "જવાબ :- વોરન હેસ્ટીંગ્સ", ""],
#     ["સ્વામી વિવેકાનંદ નું મૂળ નામ શું હતું ?", "A. સુરેન્દ્રનાથ", "B. રવીન્દ્રનાથ", "C. રામકૃષ્ણ", "D. નરેન્દ્રનાથ", "જવાબ  નરેન્દ્રનાથ", ""]
#     # Add more data here for a total of 7 objects
# ]

image_width = 1920
image_height = 1080
background_color = (238, 164, 127)
font_color = (1, 83, 157)
font_size = 90
line_spacing = 10
margin = 80

for idx, data in enumerate(data_list):
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("HindVadodara-SemiBold.ttf", font_size)
    y_position = margin

    text_to_speak = ""

    for text in data:
        wrapped_text = textwrap.fill(text, width=40)  # Adjust width as needed
        lines = wrapped_text.split('\n')

        for line in lines:
            draw.text((margin, y_position), line, font=font, fill=font_color)
            y_position += font_size + line_spacing
            text_to_speak += line + "\n"

        y_position += line_spacing  # Add extra spacing between wrapped lines

    image.save(f"Gyan_Dariyo_image_{idx+1}.png")
    image.show()

    # Convert text to speech and create an audio file
    tts = gTTS(text=text_to_speak, lang='gu')
    audio_file_path = f"Gyan_Dariyo_audio_{idx+1}.mp3"
    tts.save(audio_file_path)

from moviepy.editor import ImageClip, AudioFileClip
from gtts import gTTS
import textwrap
video_list = []
default_fps = 24  # Default frames per second for the video clips

for idx, data in enumerate(data_list):
    text_to_speak = "\n".join(data)

    # Convert text to speech and create an audio file
    tts = gTTS(text=text_to_speak, lang='gu')
    audio_file_path = f"Gyan_Dariyo_audio_{idx+1}.mp3"
    tts.save(audio_file_path)

    # Load the audio clip
    audio_clip = AudioFileClip(audio_file_path)

    # Get the audio duration
    audio_duration = audio_clip.duration

    # Create an image clip
    image_path = f"Gyan_Dariyo_image_{idx+1}.png"
    image_clip = ImageClip(image_path)

    # Set the audio of the image clip
    video_clip = image_clip.set_audio(audio_clip)

    # Set the duration of the video clip to match the audio duration
    video_clip = video_clip.set_duration(audio_duration)

    # Set the fps for the video clip
    video_clip = video_clip.set_fps(default_fps)

    # Write the final video
    video_file_path = f"Gyan_Dariyo_video_{idx+1}.mp4"
    video_list.append(f"Gyan_Dariyo_video_{idx+1}.mp4")
    video_clip.write_videofile(video_file_path, codec="libx264", audio_codec="aac")

    # Print a message to indicate completion
    print(f"Video {idx+1} created: {video_file_path}")
import time
from gtts import gTTS

def create_combined_mp3(data_list, output_file):
    combined_text = " ".join(data_list)
    tts = gTTS(text=combined_text, lang='gu')
    tts.save(output_file)
    time.sleep(10)
    print(f"Created combined MP3: {output_file}")

for i in range(len(data_list)):
    output_file = f"combined_output_{i+1}.mp3"
    create_combined_mp3([str(data_list[i])], output_file)
from moviepy.editor import VideoFileClip, concatenate_videoclips

video_list = []

for idx, data in enumerate(data_list):
    video_file_path = f"Gyan_Dariyo_video_{idx+1}.mp4"
    video_clip = VideoFileClip(video_file_path)
    video_list.append(video_clip)

final_video = concatenate_videoclips(video_list)

final_video_file_path = "Gyan_Dariyo_final_video.mp4"
final_video.write_videofile(final_video_file_path, codec="libx264", audio_codec="aac")

print(f"Final video created: {final_video_file_path}")

