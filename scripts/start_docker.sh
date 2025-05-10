#!/bin/bash

# Script to start Docker containers for the assessment system

# Create tmp directory if it doesn't exist
mkdir -p tmp

# Build and start the containers
echo "Building and starting Docker containers..."
docker-compose up -d

# Check if containers are running
echo "Checking container status..."
docker-compose ps

echo "Docker containers are now running."
echo "MongoDB is available at localhost:27017"
echo "Code execution environment is ready for use."
echo ""
echo "To stop the containers, run: docker-compose down"
