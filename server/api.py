
"""
API Server for Assessment Analysis System
"""

import os
import logging
import json
import uuid
from datetime import datetime, timedelta
from functools import wraps

from flask import Flask, request, jsonify, g, send_from_directory
from flask_cors import CORS
import jwt

from server.services.database_service import DatabaseService
from server.services.analysis_service import AnalysisService
from server.services.reporting_service import ReportingService
from server.services.background_worker import BackgroundWorker
from server.swagger_new import spec, swagger_ui_blueprint, SWAGGER_URL
from server.utils.json_encoder import MongoJSONEncoder

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

app.json_encoder = MongoJSONEncoder

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev_secret_key")

db_service = DatabaseService()
analysis_service = AnalysisService(db_service)
reporting_service = ReportingService(db_service)
background_worker = BackgroundWorker(db_service, analysis_service)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            g.user = data["user"]
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated


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

    username = data.get("username")

    token = jwt.encode({
        "user": username,
        "exp": datetime.utcnow() + timedelta(seconds=app.config["JWT_EXPIRATION_DELTA"])
    }, app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({
        "token": token,
        "expires_in": app.config["JWT_EXPIRATION_DELTA"]
    })


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

    if "testId" not in data:
        return jsonify({"message": "testId is required"}), 400

    existing = db_service.get_assessment_by_id(data["testId"])
    if existing:
        return jsonify({"message": "Assessment with this ID already exists"}), 409

    if "createdAt" not in data:
        data["createdAt"] = datetime.now().isoformat()
    if "updatedAt" not in data:
        data["updatedAt"] = datetime.now().isoformat()

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

    existing = db_service.get_assessment_by_id(test_id)
    if not existing:
        return jsonify({"message": "Assessment not found"}), 404

    data["updatedAt"] = datetime.now().isoformat()

    db_service.update_assessment(test_id, data)

    return jsonify({
        "message": "Assessment updated successfully"
    })

@app.route("/api/assessments/<test_id>", methods=["DELETE"])
def delete_assessment(test_id):
    """Delete an assessment."""
    existing = db_service.get_assessment_by_id(test_id)
    if not existing:
        return jsonify({"message": "Assessment not found"}), 404

    db_service.delete_assessment(test_id)

    return jsonify({
        "message": "Assessment deleted successfully"
    })


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

    if "solution_id" not in data:
        return jsonify({"message": "solution_id is required"}), 400
    if "test_id" not in data:
        return jsonify({"message": "test_id is required"}), 400

    existing = db_service.get_solution_by_id(data["solution_id"])
    if existing:
        return jsonify({"message": "Solution with this ID already exists"}), 409

    solution_id = db_service.store_solution(data)

    return jsonify({
        "message": "Solution created successfully",
        "solution_id": solution_id
    }), 201

# analysis
@app.route("/api/analysis/<solution_id>", methods=["GET"])
def get_analysis(solution_id):
    """Get analysis for a specific solution."""
    analysis = db_service.get_analysis_by_solution_id(solution_id)

    if not analysis:
        return jsonify({"message": "Analysis not found"}), 404

    return jsonify(analysis)

@app.route("/api/analyze/solution/<solution_id>", methods=["POST"])
def analyze_solution(solution_id):
    """Analyze a specific solution asynchronously."""
    solution = db_service.get_solution_by_id(solution_id)
    if not solution:
        return jsonify({"message": "Solution not found"}), 404

    existing_jobs = db_service.get_all_analysis_jobs()
    for job in existing_jobs:
        if (job["job_type"] == "solution" and
            job["job_data"].get("solution_id") == solution_id and
            job["status"] in ["pending", "running"]):
            return jsonify({
                "message": "Solution is already being analyzed",
                "job_id": job["job_id"],
                "status": job["status"]
            })

    existing_analysis = db_service.get_analysis_by_solution_id(solution_id)
    if existing_analysis:
        return jsonify({
            "message": "Solution is already analyzed",
            "analysis_id": existing_analysis.get("analysis_id") or existing_analysis.get("_id")
        })

    job_id = background_worker.start_analysis_job("solution", {"solution_id": solution_id})

    return jsonify({
        "message": "Solution analysis started",
        "job_id": job_id
    })

@app.route("/api/analyze/test/<test_id>", methods=["POST"])
def analyze_test(test_id):
    """Analyze all solutions for a specific test asynchronously."""
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    solutions = db_service.get_solutions_by_test_id(test_id)
    if not solutions:
        return jsonify({"message": "No solutions found for this test"}), 404

    existing_jobs = db_service.get_all_analysis_jobs()
    for job in existing_jobs:
        if (job["job_type"] == "test" and
            job["job_data"].get("test_id") == test_id and
            job["status"] in ["pending", "running"]):
            return jsonify({
                "message": "Test is already being analyzed",
                "job_id": job["job_id"],
                "status": job["status"]
            })

    job_id = background_worker.start_analysis_job("test", {"test_id": test_id})

    return jsonify({
        "message": "Test analysis started",
        "job_id": job_id
    })

@app.route("/api/analyze/all", methods=["POST"])
def analyze_all():
    """Analyze all unprocessed solutions asynchronously."""
    existing_jobs = db_service.get_all_analysis_jobs()
    for job in existing_jobs:
        if (job["job_type"] == "all" and job["status"] in ["pending", "running"]):
            return jsonify({
                "message": "All solutions are already being analyzed",
                "job_id": job["job_id"],
                "status": job["status"]
            })

    job_id = background_worker.start_analysis_job("all", {})

    return jsonify({
        "message": "Analysis of all unprocessed solutions started",
        "job_id": job_id
    })

# analysis jobs
@app.route("/api/analysis/jobs", methods=["GET"])
def get_analysis_jobs():
    """Get all analysis jobs."""
    jobs = db_service.get_all_analysis_jobs()
    return jsonify(jobs)

@app.route("/api/analysis/jobs/<job_id>", methods=["GET"])
def get_analysis_job(job_id):
    """Get a specific analysis job."""
    job = background_worker.get_job_status(job_id)

    if not job:
        return jsonify({"message": "Analysis job not found"}), 404

    return jsonify(job)

@app.route("/api/analysis/jobs/<job_id>/logs", methods=["GET"])
def get_analysis_job_logs(job_id):
    """Get logs for a specific analysis job."""
    logs = background_worker.get_job_logs(job_id)

    if not logs:
        return jsonify([])

    for log in logs:
        for key, value in list(log.items()):
            if hasattr(value, '__str__') and not isinstance(value, (str, int, float, bool, type(None))):
                log[key] = str(value)

    return jsonify(logs)


@app.route("/api/assessments/<test_id>/start", methods=["POST"])
def start_assessment(test_id):
    data = request.get_json()
    if "candidate_id" not in data:
        return jsonify({"message": "Missing required field: candidate_id"}), 400
    candidate_id = data["candidate_id"]
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404
    existing_solution = db_service.get_solution_by_test_and_candidate(test_id, candidate_id)
    if existing_solution:
        return jsonify({
            "message": "Assessment already started for this candidate",
            "solution_id": existing_solution["solution_id"],
            "started_at": existing_solution["started_at"]
        }), 409

    solution_id = f"{test_id}-{candidate_id}-{uuid.uuid4().hex[:8]}"
    solution = {
        "solution_id": solution_id,
        "test_id": test_id,
        "candidate_id": candidate_id,
        "answers": [],
        "coding_answers": [],
        "started_at": datetime.now().isoformat(),
        "completed_at": None,
        "time_taken": None
    }
    db_service.store_solution(solution)

    return jsonify({
        "message": "Assessment started successfully",
        "solution_id": solution_id,
        "started_at": solution["started_at"]
    })

@app.route("/api/assessments/<test_id>/submit/coding", methods=["POST"])
def submit_coding_answer(test_id):
    data = request.get_json()
    required_fields = ["candidate_id", "question_id", "code", "language"]
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Missing required field: {field}"}), 400
    candidate_id = data["candidate_id"]
    question_id = data["question_id"]
    code = data["code"]
    language = data["language"]
    execution_time = data.get("execution_time", 0.0)
    memory_usage = data.get("memory_usage", 0)
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404
    solution = db_service.get_solution_by_test_and_candidate(test_id, candidate_id)
    if not solution:
        solution_id = f"{test_id}-{candidate_id}-{uuid.uuid4().hex[:8]}"
        solution = {
            "solution_id": solution_id,
            "test_id": test_id,
            "candidate_id": candidate_id,
            "answers": [],
            "coding_answers": [],
            "started_at": datetime.now().isoformat(),
            "completed_at": None,
            "time_taken": None
        }
        db_service.store_solution(solution)
    else:
        solution_id = solution["solution_id"]
    solution["coding_answers"] = [
        answer for answer in solution.get("coding_answers", [])
        if answer["question_id"] != question_id
    ]
    new_coding_answer = {
        "question_id": question_id,
        "code": code,
        "language": language,
        "execution_time": execution_time,
        "memory_usage": memory_usage,
        "submitted_at": datetime.now().isoformat()
    }
    solution["coding_answers"].append(new_coding_answer)
    db_service.update_solution(solution_id, solution)
    return jsonify({
        "message": "Coding answer submitted successfully",
        "solution_id": solution_id,
        "question_id": question_id,
        "coding_answer": new_coding_answer
    })

@app.route("/api/assessments/<test_id>/submit/complete", methods=["POST"])
def complete_assessment(test_id):
    data = request.get_json()
    required_fields = ["candidate_id", "answers"]
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Missing required field: {field}"}), 400
    candidate_id = data["candidate_id"]
    answers = data["answers"]
    if not isinstance(answers, list):
        return jsonify({"message": "answers must be a list"}), 400
    for i, answer in enumerate(answers):
        required_answer_fields = ["question_id", "answer_type", "value"]
        for field in required_answer_fields:
            if field not in answer:
                return jsonify({"message": f"Missing required field '{field}' in answer {i+1}"}), 400
        if answer["answer_type"] not in ["MCQ", "OPEN_ENDED"]:
            return jsonify({"message": f"Invalid answer_type in answer {i+1}. Must be 'MCQ' or 'OPEN_ENDED'"}), 400
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404
    solution = db_service.get_solution_by_test_and_candidate(test_id, candidate_id)
    if not solution:
        return jsonify({"message": "No solution found for this candidate. Please start the assessment first."}), 404
    if solution.get("completed_at"):
        return jsonify({
            "message": "Assessment already completed",
            "solution_id": solution["solution_id"],
            "completed_at": solution["completed_at"]
        }), 409

    submitted_at = datetime.now().isoformat()
    processed_answers = []
    for answer in answers:
        processed_answer = {
            "question_id": answer["question_id"],
            "answer_type": answer["answer_type"],
            "value": answer["value"],
            "submitted_at": submitted_at
        }
        processed_answers.append(processed_answer)

    started_at = datetime.fromisoformat(solution["started_at"])
    completed_at = datetime.now()
    time_taken = int((completed_at - started_at).total_seconds())
    solution["answers"] = processed_answers
    solution["completed_at"] = completed_at.isoformat()
    solution["time_taken"] = time_taken
    db_service.update_solution(solution["solution_id"], solution)
    return jsonify({
        "message": "Assessment completed successfully",
        "solution_id": solution["solution_id"],
        "completed_at": solution["completed_at"],
        "time_taken": time_taken,
        "answers_submitted": len(processed_answers)
    })

@app.route("/api/assessments/<test_id>/candidate/<candidate_id>/solution", methods=["GET"])
def get_candidate_solution(test_id, candidate_id):
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    solution = db_service.get_solution_by_test_and_candidate(test_id, candidate_id)
    if not solution:
        return jsonify({"message": "No solution found for this candidate"}), 404

    return jsonify(solution)

@app.route("/api/assessments/<test_id>/status", methods=["GET"])
def get_assessment_status(test_id):
    """Get assessment status for a candidate."""
    candidate_id = request.args.get("candidate_id")

    if not candidate_id:
        return jsonify({"message": "candidate_id parameter is required"}), 400

    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    print("creadintials",test_id, candidate_id)
    solution = db_service.get_solution_by_test_and_candidate(test_id, candidate_id)

    if not solution:
        return jsonify({
            "status": "not_started",
            "message": "Assessment not started",
            "assessment_duration": assessment.get("duration", 60),
            "total_questions": len(assessment.get("questions", [])) + len(assessment.get("codingQuestions", []))
        })

    if solution.get("completed_at"):
        return jsonify({
            "status": "completed",
            "message": "Assessment completed",
            "solution_id": solution["solution_id"],
            "completed_at": solution["completed_at"],
            "time_taken": solution.get("time_taken", 0)
        })

    started_at = datetime.fromisoformat(solution["started_at"])
    duration_minutes = assessment.get("duration", 60)
    expiry_time = started_at + timedelta(minutes=duration_minutes)
    current_time = datetime.now()

    if current_time > expiry_time:
        return jsonify({
            "status": "expired",
            "message": "Assessment time has expired",
            "solution_id": solution["solution_id"],
            "started_at": solution["started_at"],
            "expired_at": expiry_time.isoformat()
        })

    time_remaining = int((expiry_time - current_time).total_seconds())

    return jsonify({
        "status": "in_progress",
        "message": "Assessment in progress",
        "solution_id": solution["solution_id"],
        "started_at": solution["started_at"],
        "time_remaining": time_remaining,
        "answers_count": len(solution.get("answers", [])),
        "coding_answers_count": len(solution.get("coding_answers", [])),
        "last_activity": solution.get("last_activity", solution["started_at"])
    })

@app.route("/api/assessments/<test_id>/save-progress", methods=["POST"])
def save_progress(test_id):
    """Auto-save assessment progress."""
    data = request.get_json()

    if "candidate_id" not in data:
        return jsonify({"message": "Missing required field: candidate_id"}), 400

    candidate_id = data["candidate_id"]

    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    solution = db_service.get_solution_by_test_and_candidate(test_id, candidate_id)
    if not solution:
        return jsonify({"message": "Assessment not started"}), 404

    if solution.get("completed_at"):
        return jsonify({"message": "Assessment already completed"}), 409

    started_at = datetime.fromisoformat(solution["started_at"])
    duration_minutes = assessment.get("duration", 60)
    expiry_time = started_at + timedelta(minutes=duration_minutes)

    if datetime.now() > expiry_time:
        return jsonify({"message": "Assessment time has expired"}), 410

    progress_data = {}

    if "draft_answers" in data:
        progress_data["draft_answers"] = data["draft_answers"]

    if "current_question" in data:
        progress_data["current_question"] = data["current_question"]

    if "progress_data" in data:
        progress_data.update(data["progress_data"])

    progress_data["last_activity"] = datetime.now().isoformat()

    solution.update(progress_data)
    db_service.update_solution(solution["solution_id"], solution)

    return jsonify({
        "message": "Progress saved successfully",
        "last_saved": progress_data["last_activity"]
    })

@app.route("/api/assessments/<test_id>/heartbeat", methods=["POST"])
def assessment_heartbeat(test_id):
    """Keep assessment session alive with heartbeat."""
    data = request.get_json()

    if "candidate_id" not in data:
        return jsonify({"message": "Missing required field: candidate_id"}), 400

    candidate_id = data["candidate_id"]

    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    solution = db_service.get_solution_by_test_and_candidate(test_id, candidate_id)
    if not solution:
        return jsonify({
            "status": "not_started",
            "message": "Assessment not started"
        }), 404

    if solution.get("completed_at"):
        return jsonify({
            "status": "completed",
            "message": "Assessment already completed"
        }), 200

    started_at = datetime.fromisoformat(solution["started_at"])
    duration_minutes = assessment.get("duration", 60)
    expiry_time = started_at + timedelta(minutes=duration_minutes)
    current_time = datetime.now()

    if current_time > expiry_time:
        return jsonify({
            "status": "expired",
            "message": "Assessment time has expired",
            "should_submit": True
        }), 410

    time_remaining = int((expiry_time - current_time).total_seconds())
    solution["last_heartbeat"] = current_time.isoformat()
    solution["last_activity"] = current_time.isoformat()

    db_service.update_solution(solution["solution_id"], solution)

    return jsonify({
        "status": "active",
        "message": "Session active",
        "time_remaining": time_remaining,
    })

@app.route("/api/assessments/<test_id>/validate-session", methods=["POST"])
def validate_session(test_id):
    """Validate session and handle conflicts (multiple tabs)."""
    data = request.get_json()

    required_fields = ["candidate_id", "session_id"]
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Missing required field: {field}"}), 400

    candidate_id = data["candidate_id"]
    session_id = data["session_id"]

    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    solution = db_service.get_solution_by_test_and_candidate(test_id, candidate_id)
    if not solution:
        return jsonify({
            "valid": False,
            "message": "Assessment not started"
        }), 404

    if solution.get("completed_at"):
        return jsonify({
            "valid": False,
            "status": "completed",
            "message": "Assessment already completed"
        }), 200

    current_session = solution.get("active_session_id")
    if current_session and current_session != session_id:
        return jsonify({
            "valid": False,
            "conflict": True,
            "message": "Assessment is open in another tab/window",
            "action": "close_other_sessions"
        }), 409

    solution["active_session_id"] = session_id
    solution["last_session_check"] = datetime.now().isoformat()
    db_service.update_solution(solution["solution_id"], solution)

    return jsonify({
        "valid": True,
        "message": "Session validated successfully",
        "session_id": session_id
    })

@app.route("/api/assessments/<test_id>/auto-submit", methods=["POST"])
def auto_submit_assessment(test_id):
    """Auto-submit assessment when time expires."""
    data = request.get_json()

    if "candidate_id" not in data:
        return jsonify({"message": "Missing required field: candidate_id"}), 400

    candidate_id = data["candidate_id"]
    reason = data.get("reason", "time_expired")

    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    solution = db_service.get_solution_by_test_and_candidate(test_id, candidate_id)
    if not solution:
        return jsonify({"message": "Assessment not started"}), 404

    if solution.get("completed_at"):
        return jsonify({
            "message": "Assessment already completed",
            "solution_id": solution["solution_id"]
        }), 200

    started_at = datetime.fromisoformat(solution["started_at"])
    completed_at = datetime.now()
    time_taken = int((completed_at - started_at).total_seconds())

    solution["completed_at"] = completed_at.isoformat()
    solution["time_taken"] = time_taken
    solution["auto_submitted"] = True
    solution["submission_reason"] = reason

    db_service.update_solution(solution["solution_id"], solution)

    return jsonify({
        "message": "Assessment auto-submitted successfully",
        "solution_id": solution["solution_id"],
        "completed_at": solution["completed_at"],
        "time_taken": time_taken,
        "reason": reason
    })

@app.route("/api/assessments/<test_id>/test-code", methods=["POST"])
def test_code(test_id):
    """Test coding solution using Docker."""
    data = request.get_json()

    required_fields = ["question_id", "code", "language"]
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Missing required field: {field}"}), 400

    question_id = data["question_id"]
    code = data["code"]
    language = data["language"]

    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404

    coding_question = None
    for cq in assessment.get("codingQuestions", []):
        if str(cq.get("order")) == str(question_id):
            coding_question = cq
            break

    if not coding_question:
        return jsonify({"message": "Coding question not found"}), 404

    if coding_question.get("language") != language:
        return jsonify({
            "message": f"Invalid language. Expected {coding_question.get('language')}, got {language}"
        }), 400

    try:
        from server.services.code_execution_service import CodeExecutionService
        code_executor = CodeExecutionService()

        test_cases = coding_question.get("testCases", [])
        results = code_executor.execute_code(
            code=code,
            language=language,
            test_cases=test_cases,
        )

        return jsonify({
            "message": "Code tested successfully",
            "results": results,
            "question_id": question_id,
            "language": language
        })

    except Exception as e:
        logger.error(f"Error testing code: {str(e)}")
        return jsonify({
            "message": "Error testing code",
            "error": str(e)
        }), 500

# reports
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
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        return jsonify({"message": "Assessment not found"}), 404
    top_candidates = request.args.get("top_candidates", 10)

    report_id = reporting_service.generate_test_report(test_id, top_candidates)

    if not report_id:
        return jsonify({"message": "Failed to generate report"}), 500

    return jsonify({
        "message": "Report generated successfully",
        "report_id": report_id
    })

@app.route("/api/reports/generate/all", methods=["POST"])
def generate_all_reports():
    """Generate reports for all tests with analyzed solutions."""
    test_ids = db_service.get_all_test_ids()

    report_ids = []
    for test_id in test_ids:
        report_id = reporting_service.generate_test_report(test_id)
        if report_id:
            report_ids.append(report_id)

    return jsonify({
        "message": f"Generated {len(report_ids)} reports",
        "report_ids": report_ids
    })

@app.route('/api/swagger.json')
def swagger_json():
    """Return the Swagger specification as JSON."""
    return jsonify(spec.to_dict())

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5002))
    debug = os.getenv("DEBUG", "False").lower() == "true"

    app.run(host="0.0.0.0", port=port, debug=debug)
