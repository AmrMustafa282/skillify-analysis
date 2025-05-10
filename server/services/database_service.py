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

    def get_assessment_by_id(self, test_id: str) -> Optional[Dict]:
        """Get an assessment by ID.

        Args:
            test_id: Assessment ID

        Returns:
            Assessment document or None if not found
        """
        collection = self.get_collection(self.assessments_collection)
        return collection.find_one({"testId": test_id})

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
        return collection.find_one({"solution_id": solution_id})

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
        report = collection.find_one({"test_id": test_id})
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

    def drop_collections(self) -> None:
        """Drop all collections in the database."""
        logger.info("Dropping existing collections")
        self._db.drop_collection(self.assessments_collection)
        self._db.drop_collection(self.solutions_collection)
        self._db.drop_collection(self.analysis_collection)
        self._db.drop_collection(self.reports_collection)

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
