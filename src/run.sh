#!/bin/bash

# Create virtual environment
echo "🔧 Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🚀 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing required Python packages..."
pip install --upgrade pip
pip install pyshark wget

# Check for tshark and install if not present
if ! command -v tshark &> /dev/null
then
    echo "⚠️ tshark not found! Please install tshark/Wireshark first."
    deactivate
    exit 1
fi

# Run Python capture and analysis script
echo "🟢 Starting packet capture and analysis..."
sudo venv/bin/python lab7.py

# Deactivate virtual environment after completion
echo "✅ Analysis complete. Deactivating virtual environment..."
deactivate
