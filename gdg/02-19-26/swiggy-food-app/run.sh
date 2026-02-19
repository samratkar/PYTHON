#!/bin/bash

# Swiggy Food Delivery App Launcher
# This script sets up and runs the Swiggy app

echo "🍔 Swiggy Food Delivery App"
echo "============================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
REQUIRED_MAJOR=3
REQUIRED_MINOR=8

# Extract major and minor version numbers
MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)

# Compare versions properly as integers
if [[ $MAJOR -lt $REQUIRED_MAJOR ]] || [[ $MAJOR -eq $REQUIRED_MAJOR && $MINOR -lt $REQUIRED_MINOR ]]; then
    echo "❌ Error: Python $REQUIRED_MAJOR.$REQUIRED_MINOR or higher is required"
    echo "You have Python $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies if requirements.txt exists and hasn't been installed
if [ -f "requirements.txt" ] && [ ! -f ".venv/.installed" ]; then
    echo "📦 Installing dependencies..."
    pip install -q --upgrade pip
    pip install -q -r requirements.txt
    touch .venv/.installed
    echo "✅ Dependencies installed"
fi

echo ""
echo "🚀 Launching Swiggy Food Delivery App..."
echo ""

# Run the app
python3 swiggy_app.py

# Deactivate virtual environment on exit
deactivate
