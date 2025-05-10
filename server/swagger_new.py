"""
Swagger configuration and specification for the API.
"""

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_swagger_ui import get_swaggerui_blueprint
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="Assessment Analysis API",
    version="1.0.0",
    openapi_version="3.0.2",
    info=dict(
        description="API for analyzing coding solutions and generating reports",
        contact=dict(email="admin@example.com"),
        license=dict(name="MIT"),
    ),
    plugins=[MarshmallowPlugin()],
)

# Define schemas for request and response objects
class LoginRequest(Schema):
    username = fields.Str(required=True, metadata={"description": "Username"})
    password = fields.Str(required=True, metadata={"description": "Password"})

class LoginResponse(Schema):
    token = fields.Str(metadata={"description": "JWT token"})
    expires_in = fields.Int(metadata={"description": "Token expiration time in seconds"})

class HealthResponse(Schema):
    status = fields.Str(metadata={"description": "API status"})
    timestamp = fields.Str(metadata={"description": "Current timestamp"})
    version = fields.Str(metadata={"description": "API version"})

class AssessmentSchema(Schema):
    testId = fields.Str(metadata={"description": "Assessment ID"})
    title = fields.Str(metadata={"description": "Assessment title"})
    description = fields.Str(metadata={"description": "Assessment description"})
    duration = fields.Int(metadata={"description": "Assessment duration in minutes"})
    questions = fields.List(fields.Dict(), metadata={"description": "List of questions"})
    codingQuestions = fields.List(fields.Dict(), metadata={"description": "List of coding questions"})
    createdAt = fields.Str(metadata={"description": "Creation timestamp"})
    updatedAt = fields.Str(metadata={"description": "Last update timestamp"})

class SolutionSchema(Schema):
    solution_id = fields.Str(metadata={"description": "Solution ID"})
    test_id = fields.Str(metadata={"description": "Assessment ID"})
    candidate_id = fields.Str(metadata={"description": "Candidate ID"})
    answers = fields.List(fields.Dict(), metadata={"description": "List of answers"})
    coding_answers = fields.List(fields.Dict(), metadata={"description": "List of coding answers"})
    started_at = fields.Str(metadata={"description": "Start timestamp"})
    completed_at = fields.Str(metadata={"description": "Completion timestamp"})
    time_taken = fields.Int(metadata={"description": "Time taken in seconds"})

class AnalysisSchema(Schema):
    analysis_id = fields.Str(metadata={"description": "Analysis ID"})
    solution_id = fields.Str(metadata={"description": "Solution ID"})
    test_id = fields.Str(metadata={"description": "Assessment ID"})
    candidate_id = fields.Str(metadata={"description": "Candidate ID"})
    overall_score = fields.Float(metadata={"description": "Overall score"})
    coding_analyses = fields.List(fields.Dict(), metadata={"description": "List of coding analyses"})
    mcq_analyses = fields.List(fields.Dict(), metadata={"description": "List of MCQ analyses"})
    open_ended_analyses = fields.List(fields.Dict(), metadata={"description": "List of open-ended analyses"})
    analyzed_at = fields.Str(metadata={"description": "Analysis timestamp"})

class ReportSchema(Schema):
    report_id = fields.Str(metadata={"description": "Report ID"})
    test_id = fields.Str(metadata={"description": "Assessment ID"})
    candidate_rankings = fields.List(fields.Dict(), metadata={"description": "List of candidate rankings"})
    statistics = fields.Dict(metadata={"description": "Report statistics"})
    generated_at = fields.Str(metadata={"description": "Generation timestamp"})

# Register schemas with spec
spec.components.schema("LoginRequest", schema=LoginRequest)
spec.components.schema("LoginResponse", schema=LoginResponse)
spec.components.schema("HealthResponse", schema=HealthResponse)
spec.components.schema("Assessment", schema=AssessmentSchema)
spec.components.schema("Solution", schema=SolutionSchema)
spec.components.schema("Analysis", schema=AnalysisSchema)
spec.components.schema("Report", schema=ReportSchema)

# Define security schemes (kept for future use but not required)
spec.components.security_scheme(
    "bearerAuth",
    {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
    }
)

# Add paths to spec
# Health endpoint
spec.path(
    path="/api/health",
    operations={
        "get": {
            "tags": ["Health"],
            "summary": "Health check",
            "description": "Returns the health status of the API",
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/HealthResponse"}
                        }
                    }
                }
            }
        }
    }
)

# Login endpoint
spec.path(
    path="/api/login",
    operations={
        "post": {
            "tags": ["Authentication"],
            "summary": "Login",
            "description": "Authenticates a user and returns a JWT token",
            "requestBody": {
                "description": "Login credentials",
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/LoginRequest"}
                    }
                }
            },
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/LoginResponse"}
                        }
                    }
                },
                "400": {
                    "description": "Missing username or password"
                }
            }
        }
    }
)

# Assessment endpoints
spec.path(
    path="/api/assessments",
    operations={
        "get": {
            "tags": ["Assessments"],
            "summary": "Get all assessments",
            "description": "Returns a list of all assessments",
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/Assessment"}
                            }
                        }
                    }
                }
            }
        },
        "post": {
            "tags": ["Assessments"],
            "summary": "Create a new assessment",
            "description": "Creates a new assessment",
            "requestBody": {
                "description": "Assessment object",
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Assessment"}
                    }
                }
            },
            "responses": {
                "201": {
                    "description": "Assessment created successfully"
                },
                "400": {
                    "description": "Invalid input"
                },
                "409": {
                    "description": "Assessment already exists"
                }
            }
        }
    }
)

# Assessment by ID endpoint
spec.path(
    path="/api/assessments/{test_id}",
    operations={
        "get": {
            "tags": ["Assessments"],
            "summary": "Get assessment by ID",
            "description": "Returns a specific assessment by ID",
            "parameters": [
                {
                    "name": "test_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the assessment to retrieve"
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Assessment"}
                        }
                    }
                },
                "404": {
                    "description": "Assessment not found"
                }
            }
        },
        "put": {
            "tags": ["Assessments"],
            "summary": "Update assessment",
            "description": "Updates an existing assessment",
            "parameters": [
                {
                    "name": "test_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the assessment to update"
                }
            ],
            "requestBody": {
                "description": "Updated assessment object",
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Assessment"}
                    }
                }
            },
            "responses": {
                "200": {
                    "description": "Assessment updated successfully"
                },
                "400": {
                    "description": "Invalid input"
                },
                "404": {
                    "description": "Assessment not found"
                }
            }
        },
        "delete": {
            "tags": ["Assessments"],
            "summary": "Delete assessment",
            "description": "Deletes an assessment",
            "parameters": [
                {
                    "name": "test_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "ID of the assessment to delete"
                }
            ],
            "responses": {
                "200": {
                    "description": "Assessment deleted successfully"
                },
                "404": {
                    "description": "Assessment not found"
                }
            }
        }
    }
)

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

# Configure Swagger UI
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI
API_URL = '/api/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Assessment Analysis API",
        'validatorUrl': None
    }
)
