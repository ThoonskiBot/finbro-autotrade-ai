#!/bin/bash

echo "🔧 Setting up FINBRO on your VPS..."

# Update and install Python + pip
sudo apt update && sudo apt install -y python3 python3-pip unzip

# Create FINBRO directory
mkdir -p ~/FINBRO
cd ~/FINBRO

# Clone or extract your project manually into this directory (e.g., via scp or curl)

# Install required Python packages
pip3 install -r requirements.txt

echo "✅ FINBRO environment ready."
echo "⚙️  To run FINBRO manually:"
echo "python3 finbro_runner.py"
