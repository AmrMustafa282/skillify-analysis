#!/usr/bin/env python3
"""
API Server for Assessment Analysis System
"""

import os
import logging
import json
from datetime import datetime, timedelta
from functools import wraps

from flask import Flask, request, jsonify, g, send_from_directory
from flask_cors import CORS
import jwt

from server.services.database_service import DatabaseService
from server.services.analysis_service import AnalysisService
from server.services.reporting_service import ReportingService
from server.swagger_new import spec, swagger_ui_blueprint, SWAGGER_URL
from server.utils.json_encoder import MongoJSONEncoder

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure app to use custom JSON encoder for MongoDB ObjectId
app.json_encoder = MongoJSONEncoder

# Register Swagger UI blueprint
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Load configuration
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev_secret_key")
app.config["JWT_EXPIRATION_DELTA"] = int(os.getenv("JWT_EXPIRATION_DELTA", 86400))  # 24 hours in seconds

# Initialize services
db_service = DatabaseService()
analysis_service = AnalysisService(db_service)
reporting_service = ReportingService(db_service)

# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Check if token is in headers
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            # Decode token
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            g.user = data["user"]
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated

# Routes

@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

@app.route("/api/login", methods=["POST"])
def login():
    """Login endpoint."""
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"message": "Missing username or password"}), 400

    # For demo purposes, accept any username/password
    # In production, you would validate against a user database
    username = data.get("username")

    # Generate token
    token = jwt.encode({
        "user": username,
        "exp": datetime.utcnow() + timedelta(seconds=app.config["JWT_EXPIRATION_DELTA"])
    }, app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({
        "token": token,
        "expires_in": app.config["JWT_EXPIRATION_DELTA"]
    })

# Assessment endpoints

@app.route("/api/assessments", methods=["GET"])
def get_assessments():
    """Get all assessments."""
    assessments = db_service.get_all_assessments()
    return jsonify(assessments)

@app.route("/api/assessments/<test_id>", methods=["GET"])
def get_assessment(test_id):
    """Get a specific assessment."""
    assessment = db_service.get_assessment_by_id(test_id)

    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    return jsonify(assessment)

@app.route("/api/assessments", methods=["POST"])
def create_assessment():
    """Create a new assessment."""
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data provided"}), 400

    # Ensure testId is present
    if "testId" not in data:
        return jsonify({"message": "testId is required"}), 400

    # Check if assessment already exists
    existing = db_service.get_assessment_by_id(data["testId"])
    if existing:
        return jsonify({"message": "Assessment with this ID already exists"}), 409

    # Add timestamps
    if "createdAt" not in data:
        data["createdAt"] = datetime.now().isoformat()
    if "updatedAt" not in data:
        data["updatedAt"] = datetime.now().isoformat()

    # Store assessment
    assessment_id = db_service.store_assessment(data)

    return jsonify({
        "message": "Assessment created successfully",
        "assessment_id": assessment_id
    }), 201

@app.route("/api/assessments/<test_id>", methods=["PUT"])
def update_assessment(test_id):
    """Update an existing assessment."""
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data provided"}), 400

    # Check if assessment exists
    existing = db_service.get_assessment_by_id(test_id)
    if not existing:
        return jsonify({"message": "Assessment not found"}), 404

    # Update timestamp
    data["updatedAt"] = datetime.now().isoformat()

    # Update assessment
    db_service.update_assessment(test_id, data)

    return jsonify({
        "message": "Assessment updated successfully"
    })

@app.route("/api/assessments/<test_id>", methods=["DELETE"])
def delete_assessment(test_id):
    """Delete an assessment."""
    # Check if assessment exists
    existing = db_service.get_assessment_by_id(test_id)
    if not existing:
        return jsonify({"message": "Assessment not found"}), 404

    # Delete assessment
    db_service.delete_assessment(test_id)

    return jsonify({
        "message": "Assessment deleted successfully"
    })

# Solution endpoints

@app.route("/api/solutions", methods=["GET"])
def get_solutions():
    """Get all solutions."""
    solutions = db_service.get_all_solutions()
    return jsonify(solutions)

@app.route("/api/solutions/<solution_id>", methods=["GET"])
def get_solution(solution_id):
    """Get a specific solution."""
    solution = db_service.get_solution_by_id(solution_id)

    if not solution:
        return jsonify({"message": "Solution not found"}), 404

    return jsonify(solution)

@app.route("/api/assessments/<test_id>/solutions", methods=["GET"])
def get_solutions_by_test(test_id):
    """Get all solutions for a specific test."""
    solutions = db_service.get_solutions_by_test_id(test_id)
    return jsonify(solutions)

@app.route("/api/solutions", methods=["POST"])
def create_solution():
    """Create a new solution."""
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data provided"}), 400

    # Ensure required fields are present
    if "solution_id" not in data:
        return jsonify({"message": "solution_id is required"}), 400
    if "test_id" not in data:
        return jsonify({"message": "test_id is required"}), 400

    # Check if solution already exists
    existing = db_service.get_solution_by_id(data["solution_id"])
    if existing:
        return jsonify({"message": "Solution with this ID already exists"}), 409

    # Store solution
    solution_id = db_service.store_solution(data)

    return jsonify({
        "message": "Solution created successfully",
        "solution_id": solution_id
    }), 201

# Analysis endpoints

@app.route("/api/analysis/<solution_id>", methods=["GET"])
def get_analysis(solution_id):
    """Get analysis for a specific solution."""
    analysis = db_service.get_analysis_by_solution_id(solution_id)

    if not analysis:
        return jsonify({"message": "Analysis not found"}), 404

    return jsonify(analysis)

@app.route("/api/analyze/solution/<solution_id>", methods=["POST"])
def analyze_solution(solution_id):
    """Analyze a specific solution."""
    # Get solution
    solution = db_service.get_solution_by_id(solution_id)
    if not solution:
        return jsonify({"message": "Solution not found"}), 404

    # Get assessment
    test_id = solution.get("test_id")
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    # Analyze solution
    analysis_result = analysis_service.analyze_solution(solution, assessment)

    # Store analysis
    analysis_id = db_service.store_analysis(analysis_result)

    return jsonify({
        "message": "Solution analyzed successfully",
        "analysis_id": analysis_id
    })

@app.route("/api/analyze/test/<test_id>", methods=["POST"])
def analyze_test(test_id):
    """Analyze all solutions for a specific test."""
    # Get assessment
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    # Get solutions
    solutions = db_service.get_solutions_by_test_id(test_id)
    if not solutions:
        return jsonify({"message": "No solutions found for this test"}), 404

    # Analyze solutions
    analysis_ids = []
    for solution in solutions:
        # Skip already analyzed solutions
        if db_service.get_analysis_by_solution_id(solution["solution_id"]):
            continue

        # Analyze solution
        analysis_result = analysis_service.analyze_solution(solution, assessment)

        # Store analysis
        analysis_id = db_service.store_analysis(analysis_result)
        analysis_ids.append(analysis_id)

    return jsonify({
        "message": f"Analyzed {len(analysis_ids)} solutions",
        "analysis_ids": analysis_ids
    })

@app.route("/api/analyze/all", methods=["POST"])
def analyze_all():
    """Analyze all unprocessed solutions."""
    # Get all solutions
    solutions = db_service.get_all_solutions()

    # Filter unprocessed solutions
    unprocessed = []
    for solution in solutions:
        if not db_service.get_analysis_by_solution_id(solution["solution_id"]):
            unprocessed.append(solution)

    if not unprocessed:
        return jsonify({"message": "No unprocessed solutions found"}), 404

    # Analyze solutions
    analysis_ids = []
    for solution in unprocessed:
        # Get assessment
        test_id = solution.get("test_id")
        assessment = db_service.get_assessment_by_id(test_id)
        if not assessment:
            continue

        # Analyze solution
        analysis_result = analysis_service.analyze_solution(solution, assessment)

        # Store analysis
        analysis_id = db_service.store_analysis(analysis_result)
        analysis_ids.append(analysis_id)

    return jsonify({
        "message": f"Analyzed {len(analysis_ids)} solutions",
        "analysis_ids": analysis_ids
    })

# Report endpoints

@app.route("/api/reports", methods=["GET"])
def get_reports():
    """Get all reports."""
    reports = db_service.get_all_reports()
    return jsonify(reports)

@app.route("/api/reports/<report_id>", methods=["GET"])
def get_report(report_id):
    """Get a specific report."""
    report = db_service.get_report_by_id(report_id)

    if not report:
        return jsonify({"message": "Report not found"}), 404

    return jsonify(report)

@app.route("/api/reports/test/<test_id>", methods=["GET"])
def get_report_by_test(test_id):
    """Get report for a specific test."""
    report = db_service.get_report_by_test_id(test_id)

    if not report:
        return jsonify({"message": "Report not found"}), 404

    return jsonify(report)

@app.route("/api/reports/generate/<test_id>", methods=["POST"])
def generate_report(test_id):
    """Generate report for a specific test."""
    # Check if test exists
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    # Generate report
    report_id = reporting_service.generate_test_report(test_id)

    if not report_id:
        return jsonify({"message": "Failed to generate report"}), 500

    return jsonify({
        "message": "Report generated successfully",
        "report_id": report_id
    })

@app.route("/api/reports/generate/all", methods=["POST"])
def generate_all_reports():
    """Generate reports for all tests with analyzed solutions."""
    # Get all test IDs
    test_ids = db_service.get_all_test_ids()

    # Generate reports
    report_ids = []
    for test_id in test_ids:
        report_id = reporting_service.generate_test_report(test_id)
        if report_id:
            report_ids.append(report_id)

    return jsonify({
        "message": f"Generated {len(report_ids)} reports",
        "report_ids": report_ids
    })

# Swagger JSON endpoint
@app.route('/api/swagger.json')
def swagger_json():
    """Return the Swagger specification as JSON."""
    return jsonify(spec.to_dict())

# Main entry point
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5002))
    debug = os.getenv("DEBUG", "False").lower() == "true"

    app.run(host="0.0.0.0", port=port, debug=debug)
