#!/usr/bin/env python3
"""
GitHub Action script to generate videos from CSV files
This script processes CSV files and creates educational videos using the csv_to_video_generator package.
"""

import pandas as pd
import os
import sys
import argparse
from pathlib import Path
from csv_to_video_generator.video_creator import GyanDariyoVideoCreator
import shutil

def find_csv_files(directory="."):
    """Find all CSV files in the repository"""
    csv_files = []
    for root, dirs, files in os.walk(directory):
        # Skip .git directory and output directory
        if '.git' in root or 'output' in root:
            continue
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files

def read_csv_data(csv_path):
    """
    Read CSV file and convert to format required by GyanDariyoVideoCreator
    Expected CSV columns: question, option_a, option_b, option_c, option_d, answer, additional_info (optional)
    """
    print(f"Reading CSV file: {csv_path}")
    df = pd.read_csv(csv_path)

    data_list = []
    for _, row in df.iterrows():
        data_entry = [
            str(row.get('question', '')),
            f"A. {row.get('option_a', '')}" if 'option_a' in row else '',
            f"B. {row.get('option_b', '')}" if 'option_b' in row else '',
            f"C. {row.get('option_c', '')}" if 'option_c' in row else '',
            f"D. {row.get('option_d', '')}" if 'option_d' in row else '',
            f"Answer: {row.get('answer', '')}" if 'answer' in row else '',
            str(row.get('additional_info', ''))
        ]
        # Filter out empty strings
        data_entry = [item for item in data_entry if item and item not in ['A. ', 'B. ', 'C. ', 'D. ', 'Answer: ']]
        data_list.append(data_entry)

    return data_list

def setup_font():
    """Copy font file to working directory if not present"""
    font_name = "HindVadodara-SemiBold.ttf"
    fonts_dir = Path(__file__).parent / "Fonts"

    # Check if font exists in current directory
    if not Path(font_name).exists():
        # Try to use Roboto font from Fonts directory
        roboto_font = fonts_dir / "Roboto-Medium.ttf"
        if roboto_font.exists():
            print(f"Using Roboto font: {roboto_font}")
            shutil.copy(roboto_font, font_name)
            return True
        else:
            print(f"Warning: Font file not found. Video generation may fail.")
            return False
    return True

def generate_videos_from_csv(csv_path, output_dir="output"):
    """Generate videos from a CSV file"""
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Read CSV data
    data_list = read_csv_data(csv_path)

    if not data_list:
        print(f"No data found in {csv_path}")
        return None

    print(f"Processing {len(data_list)} entries from {csv_path}")

    # Setup font
    setup_font()

    # Create video creator instance
    video_creator = GyanDariyoVideoCreator(data_list)

    # Create images
    print("Creating images...")
    video_creator.create_images()

    # Create audio
    print("Creating audio...")
    video_creator.create_audio()

    # Create videos
    print("Creating videos...")
    video_list = video_creator.create_videos()

    # Create final video
    print("Creating final video...")
    final_video_path = video_creator.create_final_video(video_list)

    # Move final video to output directory with descriptive name
    csv_filename = Path(csv_path).stem
    output_filename = f"{csv_filename}_final_video.mp4"
    output_path = os.path.join(output_dir, output_filename)

    if os.path.exists(final_video_path):
        shutil.move(final_video_path, output_path)
        print(f"Final video saved to: {output_path}")

        # Clean up intermediate files
        cleanup_intermediate_files()

        return output_path
    else:
        print(f"Error: Final video was not created")
        return None

def cleanup_intermediate_files():
    """Clean up intermediate image, audio, and video files"""
    patterns = [
        "Gyan_Dariyo_image_*.png",
        "Gyan_Dariyo_audio_*.mp3",
        "Gyan_Dariyo_video_*.mp4"
    ]

    import glob
    for pattern in patterns:
        for file in glob.glob(pattern):
            try:
                os.remove(file)
                print(f"Cleaned up: {file}")
            except Exception as e:
                print(f"Warning: Could not remove {file}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate videos from CSV files')
    parser.add_argument('--csv-file', help='Specific CSV file to process')
    parser.add_argument('--output-dir', default='output', help='Output directory for videos (default: output)')
    parser.add_argument('--all', action='store_true', help='Process all CSV files in the repository')

    args = parser.parse_args()

    output_dir = args.output_dir
    csv_files = []

    if args.csv_file:
        # Process specific CSV file
        if os.path.exists(args.csv_file):
            csv_files = [args.csv_file]
        else:
            print(f"Error: CSV file not found: {args.csv_file}")
            sys.exit(1)
    elif args.all:
        # Process all CSV files
        csv_files = find_csv_files()
        if not csv_files:
            print("No CSV files found in the repository")
            sys.exit(0)
    else:
        # Default: process all CSV files
        csv_files = find_csv_files()
        if not csv_files:
            print("No CSV files found. Use --csv-file to specify a file or --all to process all CSV files.")
            sys.exit(0)

    print(f"Found {len(csv_files)} CSV file(s) to process")

    # Process each CSV file
    generated_videos = []
    for csv_file in csv_files:
        try:
            video_path = generate_videos_from_csv(csv_file, output_dir)
            if video_path:
                generated_videos.append(video_path)
        except Exception as e:
            print(f"Error processing {csv_file}: {e}")
            import traceback
            traceback.print_exc()
            continue

    print(f"\n{'='*60}")
    print(f"Video generation complete!")
    print(f"Generated {len(generated_videos)} video(s):")
    for video in generated_videos:
        print(f"  - {video}")
    print(f"{'='*60}")

    return 0 if generated_videos else 1

if __name__ == "__main__":
    sys.exit(main())
