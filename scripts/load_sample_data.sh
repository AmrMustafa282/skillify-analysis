#!/bin/bash

# Script to load sample data into the database

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

echo "Sample data has been loaded successfully."
