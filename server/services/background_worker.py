"""
Background worker for running analysis jobs asynchronously.
"""
import logging
import threading
import time
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any

from server.services.database_service import DatabaseService
from server.services.analysis_service import AnalysisService

# Configure logging
logger = logging.getLogger(__name__)

class BackgroundWorker:
    """Background worker for running analysis jobs asynchronously."""

    def __init__(self, db_service: DatabaseService, analysis_service: AnalysisService):
        """Initialize the background worker.

        Args:
            db_service: Database service
            analysis_service: Analysis service
        """
        self.db_service = db_service
        self.analysis_service = analysis_service
        self.active_jobs = {}
        self.job_threads = {}
        self.job_logs = {}
        self.job_lock = threading.Lock()

    def start_analysis_job(self, job_type: str, job_data: Dict) -> str:
        """Start an analysis job.

        Args:
            job_type: Type of job (solution, test, all)
            job_data: Job data

        Returns:
            Job ID
        """
        # Generate a unique job ID
        job_id = str(uuid.uuid4())

        # Create job document
        job = {
            "job_id": job_id,
            "job_type": job_type,
            "job_data": job_data,
            "status": "pending",
            "progress": 0,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "completed_at": None,
            "result": None,
            "error": None
        }

        # Store job in database
        self.db_service.store_analysis_job(job)

        # Initialize job logs
        self.job_logs[job_id] = []
        self._add_job_log(job_id, "Job created")

        # Start job in a separate thread
        thread = threading.Thread(target=self._run_job, args=(job_id, job_type, job_data))
        thread.daemon = True
        thread.start()

        with self.job_lock:
            self.job_threads[job_id] = thread
            self.active_jobs[job_id] = job

        return job_id

    def _run_job(self, job_id: str, job_type: str, job_data: Dict):
        """Run an analysis job.

        Args:
            job_id: Job ID
            job_type: Type of job (solution, test, all)
            job_data: Job data
        """
        try:
            self._update_job_status(job_id, "running", 0)
            self._add_job_log(job_id, f"Starting {job_type} analysis job")

            if job_type == "solution":
                self._run_solution_analysis(job_id, job_data)
            elif job_type == "test":
                self._run_test_analysis(job_id, job_data)
            elif job_type == "all":
                self._run_all_analysis(job_id, job_data)
            else:
                raise ValueError(f"Unknown job type: {job_type}")

            self._update_job_status(job_id, "completed", 100)
            self._add_job_log(job_id, "Job completed successfully")

        except Exception as e:
            logger.error(f"Error in job {job_id}: {str(e)}")
            self._update_job_status(job_id, "failed", 0, error=str(e))
            self._add_job_log(job_id, f"Job failed: {str(e)}")

        finally:
            # Remove job from active jobs
            with self.job_lock:
                if job_id in self.active_jobs:
                    del self.active_jobs[job_id]
                if job_id in self.job_threads:
                    del self.job_threads[job_id]

    def _run_solution_analysis(self, job_id: str, job_data: Dict):
        """Run analysis for a single solution.

        Args:
            job_id: Job ID
            job_data: Job data
        """
        solution_id = job_data.get("solution_id")
        if not solution_id:
            raise ValueError("Solution ID is required")

        self._add_job_log(job_id, f"Analyzing solution: {solution_id}")

        # Get solution
        solution = self.db_service.get_solution_by_id(solution_id)
        if not solution:
            raise ValueError(f"Solution not found: {solution_id}")

        # Get assessment
        test_id = solution.get("test_id")
        if not test_id:
            raise ValueError(f"Test ID not found in solution: {solution_id}")

        assessment = self.db_service.get_assessment_by_id(test_id)
        if not assessment:
            raise ValueError(f"Assessment not found: {test_id}")

        # Analyze solution
        self._add_job_log(job_id, "Running analysis")
        analysis_result = self.analysis_service.analyze_solution(solution, assessment)

        # Store analysis
        self._add_job_log(job_id, "Storing analysis results")
        analysis_id = self.db_service.store_analysis(analysis_result)

        # Update job result
        self._update_job_result(job_id, {"analysis_id": analysis_id})

    def _run_test_analysis(self, job_id: str, job_data: Dict):
        """Run analysis for all solutions in a test.

        Args:
            job_id: Job ID
            job_data: Job data
        """
        test_id = job_data.get("test_id")
        if not test_id:
            raise ValueError("Test ID is required")

        self._add_job_log(job_id, f"Analyzing test: {test_id}")

        # Get assessment
        assessment = self.db_service.get_assessment_by_id(test_id)
        if not assessment:
            raise ValueError(f"Assessment not found: {test_id}")

        # Get solutions
        solutions = self.db_service.get_solutions_by_test_id(test_id)
        if not solutions:
            raise ValueError(f"No solutions found for test: {test_id}")

        # Analyze solutions
        analysis_ids = []
        total_solutions = len(solutions)

        for i, solution in enumerate(solutions):
            # Skip already analyzed solutions
            if self.db_service.get_analysis_by_solution_id(solution["solution_id"]):
                self._add_job_log(job_id, f"Skipping already analyzed solution: {solution['solution_id']}")
                continue

            # Update progress
            progress = int((i / total_solutions) * 100)
            self._update_job_status(job_id, "running", progress)

            # Analyze solution
            self._add_job_log(job_id, f"Analyzing solution {i+1}/{total_solutions}: {solution['solution_id']}")
            analysis_result = self.analysis_service.analyze_solution(solution, assessment)

            # Store analysis
            analysis_id = self.db_service.store_analysis(analysis_result)
            analysis_ids.append(analysis_id)

        # Update job result
        self._update_job_result(job_id, {"analysis_ids": analysis_ids})

    def _run_all_analysis(self, job_id: str, job_data: Dict):
        """Run analysis for all unprocessed solutions.

        Args:
            job_id: Job ID
            job_data: Job data
        """
        self._add_job_log(job_id, "Analyzing all unprocessed solutions")

        # Get all solutions
        solutions = self.db_service.get_all_solutions()

        # Filter unprocessed solutions
        unprocessed = []
        for solution in solutions:
            if not self.db_service.get_analysis_by_solution_id(solution["solution_id"]):
                unprocessed.append(solution)

        if not unprocessed:
            self._add_job_log(job_id, "No unprocessed solutions found")
            return

        # Analyze solutions
        analysis_ids = []
        total_solutions = len(unprocessed)

        for i, solution in enumerate(unprocessed):
            # Update progress
            progress = int((i / total_solutions) * 100)
            self._update_job_status(job_id, "running", progress)

            # Get assessment
            test_id = solution.get("test_id")
            assessment = self.db_service.get_assessment_by_id(test_id)
            if not assessment:
                self._add_job_log(job_id, f"Skipping solution with unknown test: {solution['solution_id']}")
                continue

            # Analyze solution
            self._add_job_log(job_id, f"Analyzing solution {i+1}/{total_solutions}: {solution['solution_id']}")
            analysis_result = self.analysis_service.analyze_solution(solution, assessment)

            # Store analysis
            analysis_id = self.db_service.store_analysis(analysis_result)
            analysis_ids.append(analysis_id)

        # Update job result
        self._update_job_result(job_id, {"analysis_ids": analysis_ids})

    def _update_job_status(self, job_id: str, status: str, progress: int, error: Optional[str] = None):
        """Update job status.

        Args:
            job_id: Job ID
            status: Job status
            progress: Job progress (0-100)
            error: Error message (if any)
        """
        # Update job in database
        job = self.db_service.get_analysis_job(job_id)
        if job:
            # Create a new job object with only the fields to update
            update_data = {
                "status": status,
                "progress": progress,
                "updated_at": datetime.now().isoformat()
            }

            if status == "completed":
                update_data["completed_at"] = datetime.now().isoformat()

            if error:
                update_data["error"] = error

            self.db_service.update_analysis_job(job_id, update_data)

        # Update job in memory
        with self.job_lock:
            if job_id in self.active_jobs:
                self.active_jobs[job_id]["status"] = status
                self.active_jobs[job_id]["progress"] = progress
                self.active_jobs[job_id]["updated_at"] = datetime.now().isoformat()

                if status == "completed":
                    self.active_jobs[job_id]["completed_at"] = datetime.now().isoformat()

                if error:
                    self.active_jobs[job_id]["error"] = error

    def _update_job_result(self, job_id: str, result: Dict):
        """Update job result.

        Args:
            job_id: Job ID
            result: Job result
        """
        # Update job in database
        job = self.db_service.get_analysis_job(job_id)
        if job:
            # Create a new job object with only the fields to update
            update_data = {
                "result": result
            }
            self.db_service.update_analysis_job(job_id, update_data)

        # Update job in memory
        with self.job_lock:
            if job_id in self.active_jobs:
                self.active_jobs[job_id]["result"] = result

    def _add_job_log(self, job_id: str, message: str):
        """Add a log message to a job.

        Args:
            job_id: Job ID
            message: Log message
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "message": message
        }

        # Add log to memory
        if job_id in self.job_logs:
            self.job_logs[job_id].append(log_entry)

        # Add log to database
        self.db_service.add_analysis_job_log(job_id, log_entry)

        # Log to application logger as well
        logger.info(f"Job {job_id}: {message}")

    def get_job_status(self, job_id: str) -> Optional[Dict]:
        """Get job status.

        Args:
            job_id: Job ID

        Returns:
            Job status or None if not found
        """
        # Check active jobs first
        with self.job_lock:
            if job_id in self.active_jobs:
                return self.active_jobs[job_id]

        # Check database
        return self.db_service.get_analysis_job(job_id)

    def get_job_logs(self, job_id: str) -> List[Dict]:
        """Get job logs.

        Args:
            job_id: Job ID

        Returns:
            List of log entries
        """
        # Check memory first
        if job_id in self.job_logs:
            return self.job_logs[job_id]

        # Check database
        return self.db_service.get_analysis_job_logs(job_id)

    def get_all_jobs(self) -> List[Dict]:
        """Get all jobs.

        Returns:
            List of jobs
        """
        return self.db_service.get_all_analysis_jobs()
