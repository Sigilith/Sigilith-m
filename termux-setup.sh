#!/data/data/com.termux/files/usr/bin/bash
# Sigilith-M Termux Setup Script
# Run this script from within the cloned Sigilith-m repository directory.
# Example:
#   pkg install git
#   git clone https://github.com/Sigilith/Sigilith-m.git
#   cd Sigilith-m
#   bash termux-setup.sh
pkg update && pkg upgrade -y
pkg install -y git python python-numpy
pip install -r requirements.txt && echo "Setup complete. Run: uvicorn main:app --host 0.0.0.0 --port 8000"
