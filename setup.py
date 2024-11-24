from setuptools import setup, find_packages

setup(
    name="csv_to_video_generator",
    version="0.1.0",
    description="A package to generate videos from CSV data",
    author="Yash Kavaiya",
    author_email="yash@example.com",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "Pillow",
        "moviepy",
        "gTTS"
    ],
    entry_points={
        'console_scripts': [
            'csv_to_video_generator=csv_to_video_generator.video_creator:main',
        ],
    },
)
