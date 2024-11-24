# csv-to-video-genarator

## Overview

This package provides functionality to generate videos from CSV data. It includes tools to create images, audio, and videos from the data provided in a CSV file.

## Installation

To install the package, use the following command:

```bash
pip install csv-to-video-generator
```

## Usage

Here is an example of how to use the `GyanDariyoVideoCreator` class to generate videos from CSV data:

```python
from csv_to_video_generator.video_creator import GyanDariyoVideoCreator

# Sample data list
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
     ""]
]

# Create an instance of the video creator
video_creator = GyanDariyoVideoCreator(data_list)

# Create images
video_creator.create_images()

# Create audio
video_creator.create_audio()

# Create videos
video_list = video_creator.create_videos()

# Create final video
final_video_path = video_creator.create_final_video(video_list)

print(f"Final video created at: {final_video_path}")
```

## License

This project is licensed under the MIT License.
