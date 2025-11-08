@echo off
REM Manim Setup Script for Windows
REM This script installs all dependencies needed for Manim video generation

echo ==================================
echo Manim Setup Script for Windows
echo ==================================
echo.

REM Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.10 or higher from https://www.python.org/
    pause
    exit /b 1
)

python --version
echo.

REM Check Python version
python -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)"
if %errorlevel% neq 0 (
    echo [ERROR] Python 3.10 or higher is required
    pause
    exit /b 1
)

echo Python version is compatible
echo.

REM Check if Chocolatey is installed
echo Checking for Chocolatey...
choco --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Chocolatey is not installed
    echo.
    echo Chocolatey is recommended for installing FFmpeg and other dependencies.
    echo Install from: https://chocolatey.org/install
    echo.
    echo You can also install FFmpeg manually from: https://ffmpeg.org/download.html
    echo.
    set /p CONTINUE="Continue without Chocolatey? (y/n): "
    if /i not "%CONTINUE%"=="y" exit /b 1
) else (
    echo Installing system dependencies via Chocolatey...
    choco install ffmpeg -y
    echo System dependencies installed
)

echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)

echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo pip upgraded
echo.

REM Install Python dependencies
echo Installing Python dependencies...

echo Installing Manim...
pip install manim

if exist "requirements.txt" (
    echo Installing from requirements.txt...
    pip install -r requirements.txt
) else if exist "pyproject.toml" (
    echo Installing from pyproject.toml using poetry...
    pip install poetry
    poetry install
)

echo Python dependencies installed
echo.

REM Create necessary directories
echo Creating necessary directories...
if not exist "manim_scenes" mkdir manim_scenes
if not exist "generated_videos" mkdir generated_videos
if not exist "logs" mkdir logs
if not exist "config" mkdir config
if not exist "data" mkdir data

echo Directories created
echo.

REM Test Manim installation
echo Testing Manim installation...
python -c "import manim; print(f'Manim version: {manim.__version__}')"
if %errorlevel% neq 0 (
    echo [ERROR] Manim installation test failed
    pause
    exit /b 1
)

echo Manim installed successfully
echo.

REM Create a test scene
echo Creating test scene...
(
echo from manim import *
echo.
echo class TestScene^(Scene^):
echo     def construct^(self^):
echo         text = Text^("Manim Setup Complete!", font_size=48, color=GREEN^)
echo         self.play^(Write^(text^)^)
echo         self.wait^(2^)
echo         self.play^(FadeOut^(text^)^)
) > test_scene.py

echo Test scene created
echo.

REM Render test scene
echo Rendering test scene...
manim render test_scene.py TestScene -ql --format=mp4

if %errorlevel% equ 0 (
    echo Test render successful!
    echo.
    echo Test video location: media\videos\test_scene\480p15\TestScene.mp4
) else (
    echo [WARNING] Test render failed
    echo This might be due to missing LaTeX or other system dependencies
)

echo.
echo ==================================
echo Setup Complete!
echo ==================================
echo.
echo Next steps:
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Create your Manim scenes in the manim_scenes\ directory
echo.
echo 3. Test locally:
echo    manim render manim_scenes\your_scene.py YourScene -qh
echo.
echo 4. Push to GitHub to trigger automatic rendering
echo.
echo Documentation:
echo - Manim docs: https://docs.manim.community/
echo - Project docs: See MANIM_AUTOMATION.md
echo.
echo Happy animating!
echo.
pause
