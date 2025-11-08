# Manim Video Automation System

## Overview

This project includes a production-ready automated system for generating Manim videos from Python scripts. When you push a `.py` file containing Manim scenes to the repository, it automatically:

1. ✅ Detects Manim scene files
2. ✅ Renders videos with proper quality settings
3. ✅ Saves with timestamped names
4. ✅ Uploads as GitHub artifacts
5. ✅ Optionally commits back to repository

## Quick Start

### 1. Create a Manim Scene

```python
# manim_scenes/my_animation.py
from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, World!")
        self.play(Write(text))
        self.wait(2)
```

### 2. Push to Repository

```bash
git add manim_scenes/my_animation.py
git commit -m "Add new animation"
git push
```

### 3. Get Your Video

- **Check GitHub Actions** tab for progress
- **Download video** from workflow artifacts
- **Find video** in `generated_videos/` directory (if auto-commit enabled)

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Git Push                              │
│                    (*.py files)                              │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              GitHub Actions Workflow                         │
│  (.github/workflows/manim-video-generator.yml)              │
├─────────────────────────────────────────────────────────────┤
│  1. Detect Changed Files                                     │
│  2. Check for Manim Scenes                                   │
│  3. Setup Python + Manim                                     │
│  4. Render Videos                                            │
│  5. Save with Timestamps                                     │
│  6. Upload Artifacts                                         │
│  7. Commit Back (Optional)                                   │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   Generated Videos                           │
│                                                              │
│  generated_videos/                                          │
│  ├── my_animation_20231108_143022.mp4                       │
│  ├── quiz_scene_20231108_143156.mp4                        │
│  └── render_log.txt                                         │
└─────────────────────────────────────────────────────────────┘
```

## Configuration

### Video Quality Settings

Edit `.github/workflows/manim-video-generator.yml`:

```yaml
env:
  MANIM_QUALITY: 'high_quality'  # Options: low_quality, medium_quality, high_quality, production_quality
  OUTPUT_DIR: 'generated_videos'
```

### Quality Comparison

| Setting | Resolution | FPS | Render Time | File Size | Use Case |
|---------|-----------|-----|-------------|-----------|----------|
| `low_quality` | 854x480 | 15 | Fast | Small | Quick previews |
| `medium_quality` | 1280x720 | 30 | Moderate | Medium | Draft versions |
| `high_quality` | 1920x1080 | 60 | Slower | Large | **Production (Recommended)** |
| `production_quality` | 3840x2160 | 60 | Very Slow | Very Large | 4K final output |

### Advanced Configuration

Edit `config/video_automation_config.json`:

```json
{
  "automation": {
    "auto_commit_videos": true,
    "trigger_on_push": true
  },
  "video_settings": {
    "quality": "high_quality",
    "frame_rate": 60,
    "background_color": "#000000"
  },
  "naming_convention": {
    "pattern": "{filename}_{timestamp}",
    "timestamp_format": "%Y%m%d_%H%M%S"
  }
}
```

## Features

### 1. Automatic File Detection

The workflow automatically detects:
- ✅ All `.py` files in `manim_scenes/` directory
- ✅ Files with Manim imports (`from manim import *`)
- ✅ Classes inheriting from `Scene`

Excluded directories:
- ❌ `.github/` (workflow files)
- ❌ `tests/` (test files)
- ❌ `docs/` (documentation)

### 2. Smart Rendering

```python
# The workflow detects Manim scenes automatically
class MyScene(Scene):  # ✓ Will render
    def construct(self):
        pass

# Regular Python code
def helper_function():  # ✗ Will not render
    pass
```

### 3. Multiple Scenes Per File

```python
# All scenes in the file will be rendered
class Intro(Scene):
    def construct(self):
        # Intro animation
        pass

class MainContent(Scene):
    def construct(self):
        # Main content
        pass

class Outro(Scene):
    def construct(self):
        # Outro animation
        pass
```

Each scene generates a separate video file.

### 4. Timestamped Output

Videos are automatically named with timestamps:

```
generated_videos/
├── example_basic_20231108_120000.mp4
├── example_basic_20231108_120130.mp4  # Same file, rendered again
└── quiz_animation_20231108_120215.mp4
```

### 5. Comprehensive Logging

Every render generates a detailed log:

```
generated_videos/render_log.txt
```

Contains:
- Files processed
- Render status (success/failure)
- Error messages
- Video locations
- Timing information

## Manual Triggering

### Via GitHub UI

1. Go to **Actions** tab
2. Select **Manim Video Generator** workflow
3. Click **Run workflow**
4. Enter file path (optional): `manim_scenes/my_animation.py`
5. Click **Run workflow**

### Via GitHub CLI

```bash
gh workflow run manim-video-generator.yml \
  -f scene_file=manim_scenes/my_animation.py
```

## Local Development

### Install Dependencies

```bash
# Using pip
pip install -r requirements-manim.txt

# Using poetry
poetry install

# System dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev \
  texlive texlive-latex-extra texlive-fonts-extra
```

### Test Locally

```bash
# Render a specific scene
manim render manim_scenes/example_basic.py BasicShapes -qh

# Render all scenes in a file
python manim_scenes/example_basic.py

# Preview with auto-reload
manim render manim_scenes/example_basic.py BasicShapes -pql
```

### Quality Flags

- `-ql`: Low quality (fast preview)
- `-qm`: Medium quality
- `-qh`: High quality (recommended for production)
- `-qp`: Production quality (4K)

Additional flags:
- `-p`: Preview after rendering
- `--format=gif`: Output as GIF
- `--transparent`: Transparent background

## Workflow Integration

### Branches

The workflow runs on:
- `main`
- `master`
- `develop`
- `claude/**` (Claude Code branches)

To add more branches, edit the workflow:

```yaml
on:
  push:
    branches:
      - main
      - feature/*  # Add this line
```

### Path Filters

Currently triggers on:
- All `*.py` files
- Files in `manim_scenes/**/*.py`

To modify, edit:

```yaml
on:
  push:
    paths:
      - '**.py'
      - 'animations/**/*.py'  # Add this line
```

## Artifacts & Downloads

### Viewing Artifacts

1. Go to **Actions** tab
2. Click on a workflow run
3. Scroll to **Artifacts** section
4. Download `manim-videos-{sha}.zip`

### Artifact Contents

```
manim-videos-abc1234.zip
├── my_animation_20231108_120000.mp4
├── quiz_scene_20231108_120130.mp4
└── render_log.txt
```

### Retention

- Default: 30 days
- Configurable in workflow file

## Auto-Commit

If enabled, videos are automatically committed back to the repository:

```yaml
- name: Commit and push generated videos
  if: steps.render.outputs.videos_generated == 'true'
  run: |
    git add generated_videos/*.mp4
    git commit -m "🎬 Auto-generated Manim videos"
    git push
```

**Note**: Requires write permissions. May fail with branch protection rules.

## Troubleshooting

### Problem: Video not generated

**Possible causes:**
- File doesn't contain Manim imports
- No Scene classes found
- Syntax errors in Python file

**Solution:**
1. Check workflow logs in GitHub Actions
2. Test locally: `manim render file.py SceneName -ql`
3. Verify imports: `from manim import *`

### Problem: Render timeout

**Possible causes:**
- Scene too complex
- Rendering in 4K quality
- Infinite loops in construct()

**Solution:**
1. Reduce quality: `-qm` or `-ql`
2. Simplify scene
3. Increase timeout in workflow

### Problem: LaTeX errors

**Possible causes:**
- Missing LaTeX packages
- Invalid LaTeX syntax

**Solution:**
1. Test LaTeX locally
2. Ensure system packages installed
3. Check Manim LaTeX documentation

### Problem: Push failed

**Possible causes:**
- Branch protection enabled
- No write permissions

**Solution:**
1. Disable auto-commit in config
2. Download from artifacts instead
3. Configure branch protection exceptions

## Best Practices

### 1. Scene Organization

```
manim_scenes/
├── basic/
│   ├── shapes.py
│   ├── text.py
│   └── colors.py
├── advanced/
│   ├── 3d_scenes.py
│   ├── graphs.py
│   └── transforms.py
└── projects/
    ├── quiz_2023.py
    └── tutorial_series.py
```

### 2. Scene Naming

```python
# Good: Descriptive names
class IntroWithLogo(Scene):
    pass

class QuizQuestion01(Scene):
    pass

# Avoid: Generic names
class Scene1(Scene):
    pass

class Test(Scene):
    pass
```

### 3. Testing

```python
# Test locally before pushing
if __name__ == "__main__":
    # Quick preview
    import subprocess
    subprocess.run([
        "manim", "render", __file__,
        "MyScene", "-ql", "-p"
    ])
```

### 4. Performance

- Use `-ql` for iteration
- Cache heavy computations
- Limit `wait()` times
- Optimize object counts

### 5. Version Control

```bash
# Don't commit generated videos (too large)
echo "generated_videos/*.mp4" >> .gitignore

# Do commit source files
git add manim_scenes/*.py
```

## Examples

### Example 1: Quiz Video

```python
from manim import *

class QuizIntro(Scene):
    def construct(self):
        title = Text("Python Quiz", font_size=72)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

class Question1(Scene):
    def construct(self):
        question = Text("What is 2 + 2?")
        options = VGroup(
            Text("A) 3"),
            Text("B) 4"),
            Text("C) 5")
        ).arrange(DOWN)

        self.play(Write(question))
        self.play(FadeIn(options))
        self.wait(2)
```

### Example 2: CSV Data

```python
from manim import *
import csv

class DataChart(Scene):
    def construct(self):
        # Load CSV
        with open('data/sales.csv') as f:
            data = list(csv.DictReader(f))

        # Create chart
        for row in data:
            bar = Rectangle(
                height=float(row['value'])/100,
                width=0.5,
                fill_opacity=0.8
            )
            label = Text(row['name'])
            self.play(Create(bar), Write(label))
            self.wait(0.5)
```

## Performance Metrics

Average render times (high quality, 10-second animation):

| Scene Complexity | Render Time | File Size |
|-----------------|-------------|-----------|
| Simple (text only) | 10-20 sec | 1-2 MB |
| Moderate (shapes + text) | 30-60 sec | 3-5 MB |
| Complex (3D + transforms) | 2-5 min | 8-15 MB |
| Very Complex (4K + effects) | 10-20 min | 20-50 MB |

## Security

### Permissions

The workflow requires:
- `contents: write` (for auto-commit)
- `actions: read` (for artifacts)

### Secrets

No secrets required for basic operation. Optional:
- `GITHUB_TOKEN` (automatically provided)
- Custom deployment tokens (for advanced workflows)

## Monitoring

### GitHub Actions Summary

Each run includes a summary showing:
- Files processed
- Videos generated
- Render status
- Download links

### Notifications

Configure in `config/video_automation_config.json`:

```json
{
  "notifications": {
    "enabled": true,
    "on_success": true,
    "on_failure": true
  }
}
```

## Future Enhancements

Planned features:
- [ ] Parallel rendering for multiple files
- [ ] Custom quality profiles
- [ ] Video thumbnails generation
- [ ] Automatic video compression
- [ ] Integration with cloud storage
- [ ] Slack/Discord notifications
- [ ] Preview videos in PR comments

## Support

### Documentation
- [Manim Documentation](https://docs.manim.community/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

### Community
- [Manim Discord](https://discord.gg/manim)
- [GitHub Issues](https://github.com/ManimCommunity/manim/issues)

### Troubleshooting
- Check workflow logs in Actions tab
- Review `render_log.txt` in artifacts
- Test locally before pushing

---

**Made with ❤️ using Manim Community Edition**
