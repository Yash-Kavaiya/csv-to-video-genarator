# GitHub Actions - Automated CSV to Video Generation

## Overview

This repository includes a GitHub Actions workflow that automatically generates educational videos when CSV files are pushed to the repository. The workflow can also be triggered manually to process specific CSV files.

## Features

- **Automatic Trigger**: Generates videos automatically when `.csv` files are pushed to the repository
- **Manual Trigger**: Run the workflow manually via GitHub Actions UI to process specific files
- **Artifact Upload**: Videos are saved as GitHub Actions artifacts (retained for 30 days)
- **Optional Commit**: Videos can optionally be committed back to the repository
- **Batch Processing**: Processes multiple CSV files in a single run

## How It Works

```mermaid
graph LR
    A[Push CSV File] --> B[GitHub Actions Triggered]
    B --> C[Setup Environment]
    C --> D[Install Dependencies]
    D --> E[Process CSV Files]
    E --> F[Generate Videos]
    F --> G[Upload as Artifacts]
    G --> H[Optional: Commit to Repo]
```

## CSV File Format

Your CSV file should have the following columns:

| Column | Description | Required |
|--------|-------------|----------|
| `question` | The question text | Yes |
| `option_a` | First option | Yes |
| `option_b` | Second option | Yes |
| `option_c` | Third option | Yes |
| `option_d` | Fourth option | Yes |
| `answer` | The correct answer | Yes |
| `additional_info` | Extra explanation or context | No |

### Example CSV

```csv
question,option_a,option_b,option_c,option_d,answer,additional_info
What is the primary goal of artificial intelligence?,Replicating human intelligence,Solving complex problems,Automating tasks,Enhancing decision-making processes,Replicating human intelligence,The primary goal of AI is to create systems that can perform tasks that typically require human intelligence.
Which programming language is commonly used for developing AI applications?,Python,Java,C++,JavaScript,Python,Python is widely used in AI due to its extensive libraries and frameworks.
```

See [sample_questions.csv](sample_questions.csv) for a complete example.

## Usage

### Automatic Workflow (Push Trigger)

1. Create or edit a `.csv` file with your questions
2. Commit and push the file to the repository:
   ```bash
   git add your_questions.csv
   git commit -m "Add new questions"
   git push
   ```
3. The workflow will automatically start
4. Check the "Actions" tab in GitHub to monitor progress
5. Download generated videos from the workflow artifacts

### Manual Workflow

1. Go to the "Actions" tab in your GitHub repository
2. Click on "Generate Video from CSV" workflow
3. Click "Run workflow"
4. (Optional) Specify a CSV file path in the input field
5. Click "Run workflow" button
6. Monitor the progress and download artifacts when complete

## Workflow Configuration

The workflow is defined in `.github/workflows/csv-to-video.yml`

### Triggers

- **Push**: Automatically runs when `.csv` files are pushed
- **Manual**: Can be triggered manually via workflow_dispatch

### Steps

1. **Checkout repository**: Gets the latest code
2. **Set up Python**: Installs Python 3.10
3. **Install dependencies**: Installs system packages (ffmpeg, imagemagick) and Python packages
4. **Detect changed CSV files**: Identifies which CSV files to process
5. **Generate videos**: Runs the video generation script
6. **Upload artifacts**: Saves videos as downloadable artifacts
7. **Commit videos** (optional): Commits videos back to the repository

### Customization

#### Disable Auto-Commit

By default, the workflow can commit generated videos back to the repository. To disable this:

1. Open `.github/workflows/csv-to-video.yml`
2. Find the step "Commit and push videos to repository"
3. Change the condition to `if: false` or remove the step entirely

#### Change Output Directory

To change where videos are saved:

1. Edit the workflow file
2. Modify the `--output-dir` parameter in the "Generate videos from CSV" step
3. Update the artifact upload path accordingly

#### Adjust Video Settings

To customize video appearance (resolution, colors, fonts):

1. Edit `generate_video_from_csv.py`
2. Modify the `GyanDariyoVideoCreator` initialization parameters
3. Commit and push the changes

Example:
```python
video_creator = GyanDariyoVideoCreator(
    data_list,
    image_width=1920,
    image_height=1080,
    background_color=(255, 255, 255),  # White background
    font_color=(0, 0, 0),              # Black text
    font_size=80
)
```

## Output

### Artifacts

Videos are uploaded as GitHub Actions artifacts with the name format:
- `generated-videos-{commit-sha}`

To download:
1. Go to the completed workflow run
2. Scroll to the "Artifacts" section at the bottom
3. Click to download the zip file containing all videos

### Video Files

Generated videos are named based on the CSV filename:
- `{csv_filename}_final_video.mp4`

For example, if your CSV file is `quiz_questions.csv`, the video will be:
- `quiz_questions_final_video.mp4`

## Local Testing

You can test the video generation locally before pushing:

```bash
# Install dependencies
pip install pandas Pillow moviepy gTTS

# Process a specific CSV file
python generate_video_from_csv.py --csv-file sample_questions.csv --output-dir output

# Process all CSV files in the repository
python generate_video_from_csv.py --all
```

## Troubleshooting

### Workflow Not Triggering

- Ensure the CSV file path matches `**.csv` pattern
- Check if the workflow file is in the default branch
- Verify the workflow is enabled in repository settings

### Video Generation Fails

- Check the CSV file format matches the expected columns
- Ensure CSV file is properly formatted (no missing commas)
- Review the workflow logs for specific error messages

### Font Issues

The workflow uses system fonts. If you encounter font-related errors:
- The workflow installs `fonts-dejavu-core` by default
- You can add custom fonts to the `Fonts/` directory
- Modify `generate_video_from_csv.py` to use your custom font

### Large CSV Files

For CSV files with many questions:
- The workflow may take longer to complete
- Consider splitting large files into smaller batches
- Monitor workflow execution time (GitHub has time limits)

## Cost Considerations

- GitHub Actions provides free minutes for public repositories
- Private repositories have limited free minutes
- Video generation is CPU-intensive and may consume minutes quickly
- Artifacts are stored for 30 days by default

## Advanced Usage

### Multiple CSV Files

The workflow can process multiple CSV files in one run:
1. Commit multiple CSV files in a single push
2. Each file will be processed separately
3. Individual videos will be created for each CSV file
4. All videos are uploaded together as artifacts

### Integration with Other Workflows

You can extend this workflow to:
- Upload videos to cloud storage (S3, Azure, etc.)
- Post videos to social media
- Send notifications when videos are ready
- Trigger subsequent workflows based on video generation

Example: Upload to S3
```yaml
- name: Upload to S3
  env:
    AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
  run: |
    aws s3 cp output/ s3://my-bucket/videos/ --recursive
```

## Contributing

To improve the workflow:
1. Fork the repository
2. Make your changes to `.github/workflows/csv-to-video.yml` or `generate_video_from_csv.py`
3. Test thoroughly
4. Submit a pull request

## License

This workflow and scripts are part of the CSV to Video Generator project and follow the same MIT License.
