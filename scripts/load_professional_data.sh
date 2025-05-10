#!/bin/bash

# Script to load professional data into the assessment database

# Set environment variables
export PYTHONPATH=$(pwd)

# Check if the --drop-existing flag is provided
if [ "$1" == "--drop-existing" ]; then
    echo "Running with --drop-existing flag to drop existing collections..."
    python scripts/load_professional_data.py --drop-existing
else
    echo "Running without --drop-existing flag..."
    python scripts/load_professional_data.py
fi

echo "Professional data loading complete!"
