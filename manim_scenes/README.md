# Manim Animation Scenes

This directory contains Manim scene files that are automatically rendered into videos when pushed to the repository.

## How It Works

1. **Create** a Python file with Manim scenes in this directory
2. **Push** the file to the repository
3. **Automated workflow** detects the file and renders it
4. **Video** is automatically saved to `generated_videos/` directory

## File Structure

```
manim_scenes/
├── example_basic.py          # Basic shapes and animations
├── quiz_animation.py         # Educational quiz animations
├── csv_data_animation.py     # CSV data visualizations
└── README.md                 # This file
```

## Creating Your Own Scene

### Basic Template

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Your animation code here
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(2)
```

### Running Locally

```bash
# Render a specific scene
manim render manim_scenes/example_basic.py MyScene -qh

# Render all scenes in a file
python manim_scenes/example_basic.py

# Preview with live reload
manim render manim_scenes/example_basic.py MyScene -pql
```

## Quality Settings

- `-ql` or `--low_quality`: 854x480 @ 15fps (fast rendering)
- `-qm` or `--medium_quality`: 1280x720 @ 30fps
- `-qh` or `--high_quality`: 1920x1080 @ 60fps (recommended)
- `-qp` or `--production_quality`: 3840x2160 @ 60fps (4K)

## Example Scenes

### 1. Basic Shapes (`example_basic.py`)
- `BasicShapes`: Geometric shapes with transformations
- `MathEquation`: LaTeX equations with animations
- `DataVisualization`: Charts and graphs

### 2. Quiz Animations (`quiz_animation.py`)
- `QuizQuestion`: Single quiz question with options
- `MultipleQuizQuestions`: Sequential quiz questions
- `AnimatedChart`: Bar chart for quiz results
- `IntroOutro`: Intro/outro animations

### 3. CSV Data (`csv_data_animation.py`)
- `CSVDataVisualization`: Bar charts from data
- `DynamicTextAnimation`: Q&A animations
- `NumberAnimation`: Animated counters
- `TimelineAnimation`: Timeline visualizations
- `CSVTableDisplay`: Animated tables

## Automatic Rendering

When you push a `.py` file to the repository:

1. GitHub Actions detects the change
2. Checks if file contains Manim scenes
3. Renders all scenes in the file
4. Saves videos with timestamp: `{filename}_{timestamp}.mp4`
5. Uploads videos as artifacts
6. Optionally commits back to repository

## Configuration

Edit `config/video_automation_config.json` to customize:

- Output directory
- Video quality
- Naming conventions
- Auto-commit settings
- File detection patterns

## Tips

### Performance
- Use `-ql` for quick previews
- Use `-qh` for final videos
- Cache is enabled by default for faster rendering

### Debugging
- Add `self.wait()` to see each step
- Use `print()` for debugging (appears in logs)
- Check `generated_videos/render_log.txt` for details

### Best Practices
- One scene = one concept
- Keep scenes under 30 seconds
- Use descriptive class names
- Add docstrings to scenes
- Test locally before pushing

## Integrating with CSV Data

```python
import csv
from manim import *

class CSVScene(Scene):
    def construct(self):
        # Load CSV data
        with open('data/questions.csv', 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        # Use data in animation
        for row in data:
            text = Text(row['question'])
            self.play(Write(text))
            self.wait(1)
            self.play(FadeOut(text))
```

## Resources

- [Manim Documentation](https://docs.manim.community/)
- [Example Gallery](https://docs.manim.community/en/stable/examples.html)
- [Manim Discord](https://discord.gg/manim)

## Troubleshooting

### Video not generated?
- Check if file contains Manim imports
- Verify Scene class exists
- Check workflow logs in GitHub Actions

### Rendering errors?
- Verify syntax with local render
- Check for missing dependencies
- Review error logs in artifacts

### Quality issues?
- Increase quality setting in workflow
- Check manim.cfg settings
- Verify resolution settings

## Examples to Try

```bash
# Render basic examples
python manim_scenes/example_basic.py

# Render quiz animations
python manim_scenes/quiz_animation.py

# Render CSV data visualizations
python manim_scenes/csv_data_animation.py
```

## Contributing

1. Create your scene file in this directory
2. Test locally first
3. Push to trigger automatic rendering
4. Check generated videos in `generated_videos/`

---

**Happy Animating! 🎬**
