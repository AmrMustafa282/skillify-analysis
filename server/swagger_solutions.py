# Solutions endpoints
spec.path(
    path="/api/solutions",
    operations={
        "get": {
            "tags": ["Solutions"],
            "summary": "Get all solutions",
            "description": "Returns a list of all solutions",
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/Solution"}
                            }
                        }
                    }
                }
            }
        },
        "post": {
            "tags": ["Solutions"],
            "summary": "Create a new solution",
            "description": "Creates a new solution",
            "requestBody": {
                "description": "Solution object",
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Solution"}
                    }
                }
            },
            "responses": {
                "201": {
                    "description": "Solution created successfully"
                },
                "400": {
                    "description": "Invalid input"
                },
                "409": {
                    "description": "Solution already exists"
                }
            }
        }
    }
)

# Solution by ID endpoint
spec.path(
    path="/api/solutions/{solution_id}",
    operations={
        "get": {
            "tags": ["Solutions"],
            "summary": "Get solution by ID",
            "description": "Returns a specific solution by ID",
            "parameters": [
                {
                    "name": "solution_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the solution to retrieve"
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Solution"}
                        }
                    }
                },
                "404": {
                    "description": "Solution not found"
                }
            }
        }
    }
)

# Solutions by test ID endpoint
spec.path(
    path="/api/assessments/{test_id}/solutions",
    operations={
        "get": {
            "tags": ["Solutions"],
            "summary": "Get solutions by test ID",
            "description": "Returns all solutions for a specific test",
            "parameters": [
                {
                    "name": "test_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the test to retrieve solutions for"
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/Solution"}
                            }
                        }
                    }
                }
            }
        }
    }
)

# Analysis endpoints
spec.path(
    path="/api/analysis/{solution_id}",
    operations={
        "get": {
            "tags": ["Analysis"],
            "summary": "Get analysis by solution ID",
            "description": "Returns analysis for a specific solution",
            "parameters": [
                {
                    "name": "solution_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the solution to retrieve analysis for"
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Analysis"}
                        }
                    }
                },
                "404": {
                    "description": "Analysis not found"
                }
            }
        }
    }
)
