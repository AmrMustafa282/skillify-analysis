# Analyze solution endpoint
spec.path(
    path="/api/analyze/solution/{solution_id}",
    operations={
        "post": {
            "tags": ["Analysis"],
            "summary": "Analyze solution",
            "description": "Analyzes a specific solution",
            "parameters": [
                {
                    "name": "solution_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the solution to analyze"
                }
            ],
            "responses": {
                "200": {
                    "description": "Solution analyzed successfully"
                },
                "404": {
                    "description": "Solution or assessment not found"
                }
            }
        }
    }
)

# Analyze test endpoint
spec.path(
    path="/api/analyze/test/{test_id}",
    operations={
        "post": {
            "tags": ["Analysis"],
            "summary": "Analyze test",
            "description": "Analyzes all solutions for a specific test",
            "parameters": [
                {
                    "name": "test_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the test to analyze solutions for"
                }
            ],
            "responses": {
                "200": {
                    "description": "Solutions analyzed successfully"
                },
                "404": {
                    "description": "Assessment not found or no solutions found"
                }
            }
        }
    }
)

# Analyze all endpoint
spec.path(
    path="/api/analyze/all",
    operations={
        "post": {
            "tags": ["Analysis"],
            "summary": "Analyze all",
            "description": "Analyzes all unprocessed solutions",
            "responses": {
                "200": {
                    "description": "Solutions analyzed successfully"
                },
                "404": {
                    "description": "No unprocessed solutions found"
                }
            }
        }
    }
)

# Reports endpoints
spec.path(
    path="/api/reports",
    operations={
        "get": {
            "tags": ["Reports"],
            "summary": "Get all reports",
            "description": "Returns a list of all reports",
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/Report"}
                            }
                        }
                    }
                }
            }
        }
    }
)

# Report by ID endpoint
spec.path(
    path="/api/reports/{report_id}",
    operations={
        "get": {
            "tags": ["Reports"],
            "summary": "Get report by ID",
            "description": "Returns a specific report by ID",
            "parameters": [
                {
                    "name": "report_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the report to retrieve"
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
