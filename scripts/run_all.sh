#!/bin/bash

# Script to run the entire pipeline: load data, analyze, generate reports

# Check if MongoDB is running
echo "Checking if MongoDB is running..."
if ! pgrep -x "mongod" > /dev/null; then
    echo "MongoDB is not running. Starting MongoDB..."
    mongod --dbpath ./data/db &
    sleep 5  # Wait for MongoDB to start
else
    echo "MongoDB is already running."
fi

# Load sample data
echo "Loading sample data..."
python -m server.server --load-sample-data --drop-existing

# Analyze all solutions
echo "Analyzing all solutions..."
python -m server.server --analyze-all

# Generate reports
echo "Generating reports..."
python -m server.server --generate-reports

echo "Pipeline completed successfully."
