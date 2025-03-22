#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Setup complete! Activate the virtual environment with 'source venv/bin/activate'"
echo "Then run the app with 'python app.py'" 