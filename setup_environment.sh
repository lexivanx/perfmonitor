#!/bin/bash

echo "Creating Python virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
echo "Running venv/bin/activate..."
source venv/bin/activate

echo "Installing Python packages..."
pip install psutil

echo "Done. Run 'deactivate' in order to deactivate the virtual environment."
