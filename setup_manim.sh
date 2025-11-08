#!/bin/bash

# Manim Setup Script for CSV-to-Video-Generator
# This script installs all dependencies needed for Manim video generation

set -e  # Exit on error

echo "=================================="
echo "Manim Setup Script"
echo "=================================="
echo ""

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
else
    echo "⚠️  Unsupported OS: $OSTYPE"
    echo "This script supports Linux and macOS only."
    exit 1
fi

echo "Detected OS: $OS"
echo ""

# Install system dependencies
echo "📦 Installing system dependencies..."
if [[ "$OS" == "linux" ]]; then
    sudo apt-get update
    sudo apt-get install -y \
        build-essential \
        python3-dev \
        ffmpeg \
        libcairo2-dev \
        libpango1.0-dev \
        libgdk-pixbuf2.0-dev \
        libffi-dev \
        shared-mime-info \
        texlive \
        texlive-latex-extra \
        texlive-fonts-extra \
        texlive-latex-recommended \
        texlive-science \
        tipa \
        libpng-dev \
        libfreetype6-dev

    echo "✓ System dependencies installed"
elif [[ "$OS" == "macos" ]]; then
    if ! command -v brew &> /dev/null; then
        echo "⚠️  Homebrew not found. Please install Homebrew first:"
        echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi

    brew update
    brew install cairo pango gdk-pixbuf libffi ffmpeg
    brew install --cask mactex

    echo "✓ System dependencies installed"
fi

echo ""

# Check Python version
echo "🐍 Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.10.0"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "⚠️  Python $PYTHON_VERSION found, but >= $REQUIRED_VERSION required"
    exit 1
fi

echo "✓ Python $PYTHON_VERSION is compatible"
echo ""

# Create virtual environment
echo "🔧 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip
echo "✓ pip upgraded"
echo ""

# Install Python dependencies
echo "📚 Installing Python dependencies..."

# Install Manim first
echo "Installing Manim..."
pip install manim

# Install other dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing from requirements.txt..."
    pip install -r requirements.txt
elif [ -f "pyproject.toml" ]; then
    echo "Installing from pyproject.toml using poetry..."
    pip install poetry
    poetry install
fi

echo "✓ Python dependencies installed"
echo ""

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p manim_scenes
mkdir -p generated_videos
mkdir -p logs
mkdir -p config
mkdir -p data

echo "✓ Directories created"
echo ""

# Test Manim installation
echo "🧪 Testing Manim installation..."
python3 -c "import manim; print(f'Manim version: {manim.__version__}')" || {
    echo "⚠️  Manim installation test failed"
    exit 1
}

echo "✓ Manim installed successfully"
echo ""

# Create a test scene
echo "🎬 Creating test scene..."
cat > test_scene.py << 'EOF'
from manim import *

class TestScene(Scene):
    def construct(self):
        text = Text("Manim Setup Complete!", font_size=48, color=GREEN)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
EOF

echo "✓ Test scene created"
echo ""

# Render test scene
echo "🎥 Rendering test scene..."
manim render test_scene.py TestScene -ql --format=mp4

if [ $? -eq 0 ]; then
    echo "✓ Test render successful!"
    echo ""
    echo "Test video location:"
    find media -name "TestScene.mp4" -type f | head -n 1
else
    echo "⚠️  Test render failed"
    exit 1
fi

echo ""
echo "=================================="
echo "✅ Setup Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Create your Manim scenes in the manim_scenes/ directory"
echo ""
echo "3. Test locally:"
echo "   manim render manim_scenes/your_scene.py YourScene -qh"
echo ""
echo "4. Push to GitHub to trigger automatic rendering"
echo ""
echo "Documentation:"
echo "- Manim docs: https://docs.manim.community/"
echo "- Project docs: See MANIM_AUTOMATION.md"
echo ""
echo "Happy animating! 🎬"
