#!/bin/bash

# Script to set up Postman collection for the Assessment Analysis API

# Create a directory for Postman files if it doesn't exist
mkdir -p postman

# Copy the Postman collection to the postman directory
cp assessment_analysis_api.postman_collection.json postman/

# Copy the README to the postman directory
cp POSTMAN_README.md postman/README.md

# Create a Postman environment file
cat > postman/assessment_analysis_api_environment.json << 'EOF'
{
  "id": "12345678-1234-1234-1234-123456789012",
  "name": "Assessment Analysis API - Local",
  "values": [
    {
      "key": "baseUrl",
      "value": "http://localhost:5001",
      "type": "default",
      "enabled": true
    },
    {
      "key": "token",
      "value": "",
      "type": "default",
      "enabled": true
    }
  ],
  "_postman_variable_scope": "environment",
  "_postman_exported_at": "2023-01-01T00:00:00.000Z",
  "_postman_exported_using": "Postman/10.0.0"
}
EOF

echo "Postman collection and environment have been set up in the 'postman' directory."
echo "To import them into Postman:"
echo "1. Open Postman"
echo "2. Click on 'Import' in the top left corner"
echo "3. Select 'Folder' and choose the 'postman' directory"
echo "4. Click 'Import'"
echo ""
echo "For more information, see the README.md file in the 'postman' directory."
