#!/bin/bash

# Script to start the API server

# Install dependencies
pip install -r server/requirements.txt

# Make sure all required packages are installed
pip install flask-swagger-ui apispec marshmallow

# Check if MongoDB is running
echo "Checking if MongoDB is running..."
if ! pgrep -x "mongod" > /dev/null; then
    echo "MongoDB is not running. Starting MongoDB..."
    mongod --dbpath ./data/db &
    sleep 5  # Wait for MongoDB to start
else
    echo "MongoDB is already running."
fi

# Set environment variables
export FLASK_APP=server.api
export FLASK_ENV=development
export DEBUG=true
export PORT=5000
export SECRET_KEY="your_secret_key_here"  # Change this in production

# Start the API server
echo "Starting the API server..."
python -m flask run --host=0.0.0.0 --port=$PORT
