#!/bin/bash

# Script to analyze all unprocessed solutions

# Check if MongoDB is running
echo "Checking if MongoDB is running..."
if ! pgrep -x "mongod" > /dev/null; then
    echo "MongoDB is not running. Starting MongoDB..."
    mongod --dbpath ./data/db &
    sleep 5  # Wait for MongoDB to start
else
    echo "MongoDB is already running."
fi

# Analyze all unprocessed solutions
echo "Analyzing all unprocessed solutions..."
python -m server.server --analyze-all

echo "Analysis complete."
