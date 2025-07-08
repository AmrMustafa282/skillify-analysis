"""
Database service for interacting with MongoDB.
"""
import logging
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)

class DatabaseService:
    """Service for interacting with MongoDB."""

    def __init__(self):
        """Initialize the database service."""
        self.mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/assessment_db")
        self.database_name = os.getenv("DATABASE_NAME", "assessment_db")

        # Collections
        self.assessments_collection = os.getenv("ASSESSMENTS_COLLECTION", "assessments")
        self.solutions_collection = os.getenv("SOLUTIONS_COLLECTION", "solutions")
        self.analysis_collection = os.getenv("ANALYSIS_COLLECTION", "analysis")
        self.reports_collection = os.getenv("REPORTS_COLLECTION", "reports")
        self.analysis_jobs_collection = os.getenv("ANALYSIS_JOBS_COLLECTION", "analysis_jobs")
        self.analysis_job_logs_collection = os.getenv("ANALYSIS_JOB_LOGS_COLLECTION", "analysis_job_logs")
        self.predefined_questions_collection = os.getenv("PREDEFINED_QUESTIONS_COLLECTION", "predefined_questions")

        # Connect to MongoDB
        try:
            self._client = MongoClient(self.mongodb_uri)
            self._db = self._client[self.database_name]

            # Create collections if they don't exist
            self._ensure_collections_exist()

            logger.info(f"Connected to MongoDB: {self.mongodb_uri}")
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise

    def _ensure_collections_exist(self):
        """Ensure that all required collections exist."""
        # Get list of existing collections
        existing_collections = self._db.list_collection_names()

        # Create collections if they don't exist
        if self.assessments_collection not in existing_collections:
            logger.info(f"Creating collection: {self.assessments_collection}")
            self._db.create_collection(self.assessments_collection)

        if self.solutions_collection not in existing_collections:
            logger.info(f"Creating collection: {self.solutions_collection}")
            self._db.create_collection(self.solutions_collection)

        if self.analysis_collection not in existing_collections:
            logger.info(f"Creating collection: {self.analysis_collection}")
            self._db.create_collection(self.analysis_collection)

        if self.reports_collection not in existing_collections:
            logger.info(f"Creating collection: {self.reports_collection}")
            self._db.create_collection(self.reports_collection)

        if self.analysis_jobs_collection not in existing_collections:
            logger.info(f"Creating collection: {self.analysis_jobs_collection}")
            self._db.create_collection(self.analysis_jobs_collection)

        if self.analysis_job_logs_collection not in existing_collections:
            logger.info(f"Creating collection: {self.analysis_job_logs_collection}")
            self._db.create_collection(self.analysis_job_logs_collection)

        if self.predefined_questions_collection not in existing_collections:
            logger.info(f"Creating collection: {self.predefined_questions_collection}")
            self._db.create_collection(self.predefined_questions_collection)

    def close(self):
        """Close the MongoDB connection."""
        if self._client:
            self._client.close()
            logger.info("MongoDB connection closed")

    def get_collection(self, collection_name: str) -> Collection:
        """Get a MongoDB collection.

        Args:
            collection_name: Name of the collection

        Returns:
            Collection object
        """
        return self._db[collection_name]

    # Assessment operations

    def get_assessment_by_id(self, test_id: str, include_sensitive_info: bool = True) -> Optional[Dict]:
        """Get an assessment by ID.

        Args:
            test_id: Assessment ID

        Returns:
            Assessment document or None if not found
        """
        collection = self.get_collection(self.assessments_collection)

        assessment = collection.find_one({"testId": test_id})
        if not assessment:
            return None

        # Remove `correctAnswer` from questions
        if not include_sensitive_info:
           for question in assessment.get("questions", []):
               question.pop("correctAnswer", None)

        # # Remove sensitive fields from codingQuestions
        if not include_sensitive_info:
           for coding in assessment.get("codingQuestions", []):
               coding.pop("solutionCode", None)

        # Convert ObjectId to string for JSON serialization
        if assessment and "_id" in assessment:
            assessment["_id"] = str(assessment["_id"])

        return assessment

    def get_code_question_by_q_id(self, test_id: str, question_id: str, include_sensitive_info: bool = False) -> Optional[Dict]:
        """Get an assessment by ID.

        Args:
            test_id: Assessment ID

        Returns:
            Assessment document or None if not found
        """
        collection = self.get_collection(self.assessments_collection)
        assessment = collection.find_one({"testId": test_id})

        if not assessment:
            return None

        for coding in assessment.get("codingQuestions", []):
            if coding.get("order") == int(question_id):
                # Make a shallow copy so the original DB data isn't affected
                sanitized_question = coding.copy()
                if not include_sensitive_info:
                   sanitized_question.pop("solutionCode", None)
                return sanitized_question

        return None

    def get_all_assessments(self) -> List[Dict]:
        """Get all assessments.

        Returns:
            List of assessment documents
        """
        collection = self.get_collection(self.assessments_collection)
        assessments = list(collection.find())

        # Convert ObjectId to string for JSON serialization
        for assessment in assessments:
            if "_id" in assessment:
                assessment["_id"] = str(assessment["_id"])

        return assessments

    def update_assessment(self, test_id: str, data: Dict) -> bool:
        """Update an assessment.

        Args:
            test_id: Assessment ID
            data: Updated assessment data

        Returns:
            True if successful, False otherwise
        """
        collection = self.get_collection(self.assessments_collection)
        result = collection.update_one({"testId": test_id}, {"$set": data})
        return result.modified_count > 0

    def store_assessment(self, assessment: Dict) -> str:
        """Store an assessment in the database.

        Args:
            assessment: Assessment document

        Returns:
            ID of the stored assessment
        """
        collection = self.get_collection(self.assessments_collection)

        # Add timestamps if not present
        if "createdAt" not in assessment:
            assessment["createdAt"] = datetime.now().isoformat()
        if "updatedAt" not in assessment:
            assessment["updatedAt"] = datetime.now().isoformat()

        result = collection.insert_one(assessment)
        return str(result.inserted_id)

    def delete_assessment(self, test_id: str) -> bool:
        """Delete an assessment.

        Args:
            test_id: Assessment ID

        Returns:
            True if successful, False otherwise
        """
        collection = self.get_collection(self.assessments_collection)
        result = collection.delete_one({"testId": test_id})
        return result.deleted_count > 0

    # Solution operations

    def get_solution_by_id(self, solution_id: str) -> Optional[Dict]:
        """Get a solution by ID.

        Args:
            solution_id: Solution ID

        Returns:
            Solution document or None if not found
        """
        collection = self.get_collection(self.solutions_collection)
        solution = collection.find_one({"solution_id": solution_id})

        # Convert ObjectId to string for JSON serialization
        if solution and "_id" in solution:
            solution["_id"] = str(solution["_id"])

        return solution

    def get_solution_by_test_and_candidate(self, test_id: str, candidate_id: str) -> Optional[Dict]:
        """Get a solution by test ID and candidate ID.

        Args:
            test_id: Test ID
            candidate_id: Candidate ID

        Returns:
            Solution document or None if not found
        """
        collection = self.get_collection(self.solutions_collection)
        solution = collection.find_one({"test_id": test_id, "candidate_id": candidate_id})

        # Convert ObjectId to string for JSON serialization
        if solution and "_id" in solution:
            solution["_id"] = str(solution["_id"])

        return solution

    def update_solution(self, solution_id: str, solution_data: Dict) -> bool:
        """Update a solution.

        Args:
            solution_id: Solution ID
            solution_data: Updated solution data

        Returns:
            True if successful, False otherwise
        """
        collection = self.get_collection(self.solutions_collection)

        # Remove _id from solution_data if present to avoid update conflicts
        if "_id" in solution_data:
            del solution_data["_id"]

        result = collection.update_one(
            {"solution_id": solution_id},
            {"$set": solution_data}
        )
        return result.modified_count > 0

    def get_solutions_by_test_id(self, test_id: str) -> List[Dict]:
        """Get all solutions for a test.

        Args:
            test_id: Test ID

        Returns:
            List of solution documents
        """
        collection = self.get_collection(self.solutions_collection)
        solutions = list(collection.find({"test_id": test_id}))

        # Convert ObjectId to string for JSON serialization
        for solution in solutions:
            if "_id" in solution:
                solution["_id"] = str(solution["_id"])

        return solutions

    def get_all_solutions(self) -> List[Dict]:
        """Get all solutions.

        Returns:
            List of solution documents
        """
        collection = self.get_collection(self.solutions_collection)
        solutions = list(collection.find())

        # Convert ObjectId to string for JSON serialization
        for solution in solutions:
            if "_id" in solution:
                solution["_id"] = str(solution["_id"])

        return solutions

    def store_solution(self, solution: Dict) -> str:
        """Store a solution in the database.

        Args:
            solution: Solution document

        Returns:
            ID of the stored solution
        """
        collection = self.get_collection(self.solutions_collection)
        result = collection.insert_one(solution)
        return str(result.inserted_id)

    def get_unprocessed_solutions(self) -> List[Dict]:
        """Get all solutions that have not been analyzed.

        Returns:
            List of solution documents
        """
        # Get all solutions
        solutions_collection = self.get_collection(self.solutions_collection)
        solutions = list(solutions_collection.find())

        # Get all analyses
        analysis_collection = self.get_collection(self.analysis_collection)
        analyses = list(analysis_collection.find())

        # Create a set of solution IDs that have been analyzed
        analyzed_solution_ids = {analysis.get("solution_id") for analysis in analyses}

        # Filter out solutions that have been analyzed
        unprocessed_solutions = [
            solution for solution in solutions
            if solution.get("solution_id") not in analyzed_solution_ids
        ]

        return unprocessed_solutions

    # Analysis operations

    def get_analysis_by_id(self, analysis_id: str) -> Optional[Dict]:
        """Get an analysis by ID.

        Args:
            analysis_id: Analysis ID

        Returns:
            Analysis document or None if not found
        """
        from bson.objectid import ObjectId

        collection = self.get_collection(self.analysis_collection)
        try:
            # Try to find by analysis_id field
            analysis = collection.find_one({"analysis_id": analysis_id})

            # If not found, try to find by _id field
            if not analysis:
                analysis = collection.find_one({"_id": ObjectId(analysis_id)})

            # Convert ObjectId to string for JSON serialization
            if analysis and "_id" in analysis:
                analysis["_id"] = str(analysis["_id"])

            return analysis
        except Exception:
            return None

    def get_analysis_by_solution_id(self, solution_id: str) -> Optional[Dict]:
        """Get an analysis by solution ID.

        Args:
            solution_id: Solution ID

        Returns:
            Analysis document or None if not found
        """
        collection = self.get_collection(self.analysis_collection)
        analysis = collection.find_one({"solution_id": solution_id})

        # Convert ObjectId to string for JSON serialization
        if analysis and "_id" in analysis:
            analysis["_id"] = str(analysis["_id"])

        return analysis

    def get_analyses_by_test_id(self, test_id: str) -> List[Dict]:
        """Get all analyses for a test.

        Args:
            test_id: Test ID

        Returns:
            List of analysis documents
        """
        collection = self.get_collection(self.analysis_collection)
        analyses = list(collection.find({"test_id": test_id}))

        # Convert ObjectId to string for JSON serialization
        for analysis in analyses:
            if "_id" in analysis:
                analysis["_id"] = str(analysis["_id"])

        return analyses

    def store_analysis(self, analysis: Dict) -> str:
        """Store an analysis in the database.

        Args:
            analysis: Analysis document

        Returns:
            ID of the stored analysis
        """
        collection = self.get_collection(self.analysis_collection)

        # Add timestamp if not present
        if "analyzed_at" not in analysis:
            analysis["analyzed_at"] = datetime.now().isoformat()

        result = collection.insert_one(analysis)
        return str(result.inserted_id)

    def get_tests_with_processed_solutions(self) -> List[str]:
        """Get all test IDs that have processed solutions.

        Returns:
            List of test IDs
        """
        collection = self.get_collection(self.analysis_collection)
        pipeline = [
            {"$group": {"_id": "$test_id"}},
            {"$project": {"test_id": "$_id", "_id": 0}}
        ]
        results = list(collection.aggregate(pipeline))
        return [result.get("test_id") for result in results]

    # Report operations

    def store_report(self, report: Dict) -> str:
        """Store a report in the database.

        Args:
            report: Report document

        Returns:
            ID of the stored report
        """
        collection = self.get_collection(self.reports_collection)

        # Add timestamp if not present
        if "generated_at" not in report:
            report["generated_at"] = datetime.now().isoformat()

        result = collection.insert_one(report)
        return str(result.inserted_id)

    def get_report_by_id(self, report_id: str) -> Optional[Dict]:
        """Get a report by ID.

        Args:
            report_id: Report ID

        Returns:
            Report document or None if not found
        """
        from bson.objectid import ObjectId

        collection = self.get_collection(self.reports_collection)
        try:
            report = collection.find_one({"_id": ObjectId(report_id)})
            if report and "_id" in report:
                report["_id"] = str(report["_id"])
            return report
        except Exception:
            return None

    def get_report_by_test_id(self, test_id: str) -> Optional[Dict]:
        """Get a report by test ID.

        Args:
            test_id: Test ID

        Returns:
            Report document or None if not found
        """
        collection = self.get_collection(self.reports_collection)
        report = collection.find_one({"test_id": test_id},sort=[("generated_at", -1)])
        if report and "_id" in report:
            report["_id"] = str(report["_id"])
        return report

    def get_all_reports(self) -> List[Dict]:
        """Get all reports.

        Returns:
            List of report documents
        """
        collection = self.get_collection(self.reports_collection)
        reports = list(collection.find())

        # Convert ObjectId to string for JSON serialization
        for report in reports:
            if "_id" in report:
                report["_id"] = str(report["_id"])

        return reports

    def get_all_test_ids(self) -> List[str]:
        """Get all test IDs.

        Returns:
            List of test IDs
        """
        collection = self.get_collection(self.assessments_collection)
        assessments = list(collection.find({}, {"testId": 1}))
        return [assessment.get("testId") for assessment in assessments if "testId" in assessment]

    # Analysis job operations

    def store_analysis_job(self, job: Dict) -> str:
        """Store an analysis job in the database.

        Args:
            job: Analysis job document

        Returns:
            ID of the stored job
        """
        collection = self.get_collection(self.analysis_jobs_collection)
        result = collection.insert_one(job)
        return str(result.inserted_id)

    def get_analysis_job(self, job_id: str) -> Optional[Dict]:
        """Get an analysis job by ID.

        Args:
            job_id: Job ID

        Returns:
            Analysis job document or None if not found
        """
        collection = self.get_collection(self.analysis_jobs_collection)
        job = collection.find_one({"job_id": job_id})

        # Convert ObjectId to string for JSON serialization
        if job and "_id" in job:
            job["_id"] = str(job["_id"])

        return job

    def update_analysis_job(self, job_id: str, job: Dict) -> bool:
        """Update an analysis job.

        Args:
            job_id: Job ID
            job: Updated job data

        Returns:
            True if successful, False otherwise
        """
        collection = self.get_collection(self.analysis_jobs_collection)
        result = collection.update_one({"job_id": job_id}, {"$set": job})
        return result.modified_count > 0

    def get_all_analysis_jobs(self) -> List[Dict]:
        """Get all analysis jobs.

        Returns:
            List of analysis job documents
        """
        collection = self.get_collection(self.analysis_jobs_collection)
        jobs = list(collection.find())

        # Convert ObjectId to string for JSON serialization
        for job in jobs:
            if "_id" in job:
                job["_id"] = str(job["_id"])

        return jobs

    def add_analysis_job_log(self, job_id: str, log_entry: Dict) -> str:
        """Add a log entry to an analysis job.

        Args:
            job_id: Job ID
            log_entry: Log entry document

        Returns:
            ID of the stored log entry
        """
        collection = self.get_collection(self.analysis_job_logs_collection)
        log_entry["job_id"] = job_id
        result = collection.insert_one(log_entry)
        return str(result.inserted_id)

    def get_analysis_job_logs(self, job_id: str) -> List[Dict]:
        """Get all log entries for an analysis job.

        Args:
            job_id: Job ID

        Returns:
            List of log entry documents
        """
        collection = self.get_collection(self.analysis_job_logs_collection)
        logs = list(collection.find({"job_id": job_id}).sort("timestamp", 1))

        # Convert ObjectId to string for JSON serialization
        for log in logs:
            if "_id" in log:
                log["_id"] = str(log["_id"])

            # Convert any other ObjectId fields to strings
            for key, value in log.items():
                if isinstance(value, ObjectId):
                    log[key] = str(value)

        return logs

    def drop_collections(self) -> None:
        """Drop all collections in the database."""
        logger.info("Dropping existing collections")
        self._db.drop_collection(self.assessments_collection)
        self._db.drop_collection(self.solutions_collection)
        self._db.drop_collection(self.analysis_collection)
        self._db.drop_collection(self.reports_collection)
        self._db.drop_collection(self.analysis_jobs_collection)
        self._db.drop_collection(self.analysis_job_logs_collection)

        # Recreate collections
        self._ensure_collections_exist()

    def load_sample_data(self, sample_data_dir: str = "sample_data", drop_existing: bool = True) -> None:
        """Load sample data into the database.

        Args:
            sample_data_dir: Directory containing sample data files
            drop_existing: Whether to drop existing collections before loading
        """
        import json
        import os

        logger.info(f"Loading sample data from {sample_data_dir}")

        # Drop existing collections if requested
        if drop_existing:
            self.drop_collections()

        # Check if the directory exists
        if not os.path.exists(sample_data_dir):
            logger.warning(f"Sample data directory not found: {sample_data_dir}")
            return

        # Load sample assessment
        assessment_path = os.path.join(sample_data_dir, "sample_assessment.json")
        if os.path.exists(assessment_path):
            try:
                with open(assessment_path, "r") as f:
                    assessment = json.load(f)

                # Check if assessment already exists
                existing = self.get_assessment_by_id(assessment.get("testId", ""))
                if not existing:
                    logger.info(f"Loading sample assessment: {assessment.get('testId', '')}")
                    self.get_collection(self.assessments_collection).insert_one(assessment)
                else:
                    logger.info(f"Sample assessment already exists: {assessment.get('testId', '')}")
            except Exception as e:
                logger.error(f"Failed to load sample assessment: {e}")

        # Load sample solutions
        solutions_dir = os.path.join(sample_data_dir, "solutions")
        if os.path.exists(solutions_dir):
            solution_files = [f for f in os.listdir(solutions_dir) if f.endswith(".json")]

            for solution_file in solution_files:
                try:
                    with open(os.path.join(solutions_dir, solution_file), "r") as f:
                        solution = json.load(f)

                    # Check if solution already exists
                    existing = self.get_solution_by_id(solution.get("solution_id", ""))
                    if not existing:
                        logger.info(f"Loading sample solution: {solution.get('solution_id', '')}")
                        self.get_collection(self.solutions_collection).insert_one(solution)
                    else:
                        logger.info(f"Sample solution already exists: {solution.get('solution_id', '')}")
                except Exception as e:
                    logger.error(f"Failed to load sample solution {solution_file}: {e}")

        logger.info("Sample data loading complete")

    # Predefined Questions Methods
    def get_predefined_questions(self, filter_criteria: Dict = None, limit: int = None, offset: int = 0) -> List[Dict]:
        """Get predefined questions with optional filtering and pagination."""
        try:
            collection = self.get_collection("predefined_questions")

            # Build query
            query = filter_criteria or {}

            # Create cursor with optional limit and offset
            cursor = collection.find(query, {"_id": 0})  # Exclude MongoDB _id field

            if offset > 0:
                cursor = cursor.skip(offset)

            if limit:
                cursor = cursor.limit(limit)

            # Sort by topic and difficulty for consistent ordering
            cursor = cursor.sort([("metadata.topic", 1), ("metadata.difficulty", 1)])

            questions = list(cursor)
            logger.info(f"Retrieved {len(questions)} predefined questions")
            return questions

        except Exception as e:
            logger.error(f"Error retrieving predefined questions: {e}")
            return []

    def count_predefined_questions(self, filter_criteria: Dict = None) -> int:
        """Count predefined questions matching the filter criteria."""
        try:
            collection = self.get_collection("predefined_questions")
            query = filter_criteria or {}
            count = collection.count_documents(query)
            return count

        except Exception as e:
            logger.error(f"Error counting predefined questions: {e}")
            return 0

    def get_predefined_question_by_id(self, question_id: str) -> Optional[Dict]:
        """Get a specific predefined question by its ID."""
        try:
            collection = self.get_collection("predefined_questions")
            question = collection.find_one({"id": question_id}, {"_id": 0})

            if question:
                logger.info(f"Retrieved predefined question: {question_id}")
            else:
                logger.warning(f"Predefined question not found: {question_id}")

            return question

        except Exception as e:
            logger.error(f"Error retrieving predefined question {question_id}: {e}")
            return None

    def get_predefined_question_topics(self) -> List[str]:
        """Get all unique topics from predefined questions."""
        try:
            collection = self.get_collection("predefined_questions")
            topics = collection.distinct("metadata.topic")
            topics.sort()  # Sort alphabetically
            logger.info(f"Retrieved {len(topics)} unique topics")
            return topics

        except Exception as e:
            logger.error(f"Error retrieving predefined question topics: {e}")
            return []

    def get_predefined_question_languages(self) -> List[str]:
        """Get all unique programming languages from predefined questions."""
        try:
            collection = self.get_collection("predefined_questions")

            # Use aggregation to get unique languages from implementations array
            pipeline = [
                {"$unwind": "$implementations"},
                {"$group": {"_id": "$implementations.language"}},
                {"$sort": {"_id": 1}}
            ]

            result = collection.aggregate(pipeline)
            languages = [doc["_id"] for doc in result]

            logger.info(f"Retrieved {len(languages)} unique languages")
            return languages

        except Exception as e:
            logger.error(f"Error retrieving predefined question languages: {e}")
            return []

    def get_predefined_question_companies(self) -> List[str]:
        """Get all unique companies from predefined questions."""
        try:
            collection = self.get_collection("predefined_questions")

            # Use aggregation to get unique companies from metadata.companies array
            pipeline = [
                {"$unwind": "$metadata.companies"},
                {"$group": {"_id": "$metadata.companies"}},
                {"$sort": {"_id": 1}}
            ]

            result = collection.aggregate(pipeline)
            companies = [doc["_id"] for doc in result]

            logger.info(f"Retrieved {len(companies)} unique companies")
            return companies

        except Exception as e:
            logger.error(f"Error retrieving predefined question companies: {e}")
            return []

    def get_predefined_question_difficulties(self) -> List[str]:
        """Get all unique difficulty levels from predefined questions."""
        try:
            collection = self.get_collection("predefined_questions")

            # Get unique difficulties from metadata.difficulty field
            difficulties = collection.distinct("metadata.difficulty")

            # Sort in logical order: EASY, MEDIUM, HARD
            difficulty_order = ["EASY", "MEDIUM", "HARD"]
            sorted_difficulties = [d for d in difficulty_order if d in difficulties]

            # Add any other difficulties that might exist
            for d in difficulties:
                if d not in sorted_difficulties:
                    sorted_difficulties.append(d)

            logger.info(f"Retrieved {len(sorted_difficulties)} unique difficulties")
            return sorted_difficulties

        except Exception as e:
            logger.error(f"Error retrieving predefined question difficulties: {e}")
            return []

    def store_predefined_questions(self, questions: List[Dict]) -> bool:
        """Store predefined questions in MongoDB."""
        try:
            collection = self.get_collection("predefined_questions")

            # Clear existing questions first
            collection.delete_many({})
            logger.info("Cleared existing predefined questions")

            # Insert new questions
            if questions:
                collection.insert_many(questions)
                logger.info(f"Stored {len(questions)} predefined questions")

            return True

        except Exception as e:
            logger.error(f"Error storing predefined questions: {e}")
            return False

    def update_predefined_question(self, question_id: str, question_data: Dict) -> bool:
        """Update a specific predefined question."""
        try:
            collection = self.get_collection("predefined_questions")

            result = collection.update_one(
                {"id": question_id},
                {"$set": question_data}
            )

            if result.modified_count > 0:
                logger.info(f"Updated predefined question: {question_id}")
                return True
            else:
                logger.warning(f"No predefined question found to update: {question_id}")
                return False

        except Exception as e:
            logger.error(f"Error updating predefined question {question_id}: {e}")
            return False

    def delete_predefined_question(self, question_id: str) -> bool:
        """Delete a specific predefined question."""
        try:
            collection = self.get_collection("predefined_questions")

            result = collection.delete_one({"id": question_id})

            if result.deleted_count > 0:
                logger.info(f"Deleted predefined question: {question_id}")
                return True
            else:
                logger.warning(f"No predefined question found to delete: {question_id}")
                return False

        except Exception as e:
            logger.error(f"Error deleting predefined question {question_id}: {e}")
            return False
