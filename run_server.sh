#!/bin/bash

# Install dependencies
pip install -r server/requirements.txt

# Make sure MongoDB is running
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

# Run the server
echo "Starting the Assessment Analysis Server..."
python -m server.server --analyze-all --generate-reports
