#!/bin/bash

# Script to drop the assessment database

# Check if MongoDB is running
echo "Checking if MongoDB is running..."
if ! pgrep -x "mongod" > /dev/null; then
    echo "MongoDB is not running. Starting MongoDB..."
    mongod --dbpath ./data/db &
    sleep 5  # Wait for MongoDB to start
else
    echo "MongoDB is already running."
fi

# Drop the database using Python
echo "Dropping the assessment_db database..."
python -c "
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
client.drop_database('assessment_db')
print('Database assessment_db has been dropped.')
"

echo "Database has been dropped successfully."
