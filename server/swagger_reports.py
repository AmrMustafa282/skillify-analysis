# Report by test ID endpoint
spec.path(
    path="/api/reports/test/{test_id}",
    operations={
        "get": {
            "tags": ["Reports"],
            "summary": "Get report by test ID",
            "description": "Returns report for a specific test",
            "parameters": [
                {
                    "name": "test_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the test to retrieve report for"
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Report"}
                        }
                    }
                },
                "404": {
                    "description": "Report not found"
                }
            }
        }
    }
)

# Generate report endpoint
spec.path(
    path="/api/reports/generate/{test_id}",
    operations={
        "post": {
            "tags": ["Reports"],
            "summary": "Generate report",
            "description": "Generates report for a specific test",
            "parameters": [
                {
                    "name": "test_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the test to generate report for"
                }
            ],
            "responses": {
                "200": {
                    "description": "Report generated successfully"
                },
                "404": {
                    "description": "Assessment not found"
                },
                "500": {
                    "description": "Failed to generate report"
                }
            }
        }
    }
)

# Generate all reports endpoint
spec.path(
    path="/api/reports/generate/all",
    operations={
        "post": {
            "tags": ["Reports"],
            "summary": "Generate all reports",
            "description": "Generates reports for all tests with analyzed solutions",
            "responses": {
                "200": {
                    "description": "Reports generated successfully"
                }
            }
        }
    }
)
