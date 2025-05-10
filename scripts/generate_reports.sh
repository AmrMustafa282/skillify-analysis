#!/bin/bash

# Script to generate reports for all tests

# Check if MongoDB is running
echo "Checking if MongoDB is running..."
if ! pgrep -x "mongod" > /dev/null; then
    echo "MongoDB is not running. Starting MongoDB..."
    mongod --dbpath ./data/db &
    sleep 5  # Wait for MongoDB to start
else
    echo "MongoDB is already running."
fi

# Generate reports
echo "Generating reports for all tests..."
python -m server.server --generate-reports

echo "Reports generated successfully."
