#!/bin/bash

# Phase 1: Python Vision Service Setup
echo "🚀 Setting up Python Vision Service (Phase 1)..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    echo "   macOS: brew install python"
    exit 1
fi

echo "📦 Installing Python dependencies..."
cd vision-python

# Create virtual environment
echo "🔧 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install dependencies
echo "📦 Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Phase 1 setup complete!"
echo ""
echo "🚀 Quick start:"
echo "  1. Activate environment: cd vision-python && source venv/bin/activate"
echo "  2. Run the service: python main.py"
echo ""
echo "📋 Phase 1 includes:"
echo "  • OpenCV for webcam capture"
echo "  • MediaPipe for pose/face/hand detection"
echo "  • FastAPI for REST endpoints (/start, /stop, /analyze)"
echo "  • Testing framework with pytest"