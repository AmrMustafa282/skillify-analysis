"""
Repository classes for database operations.
"""
from typing import List, Dict, Optional, Any
from bson import ObjectId
from pymongo.collection import Collection

from app.core.config import (
    ASSESSMENTS_COLLECTION,
    SOLUTIONS_COLLECTION,
    ANALYSIS_COLLECTION,
    REPORTS_COLLECTION,
)
from app.database.mongodb import MongoDB
from app.models.assessment import Assessment
from app.models.solution import Solution
from app.models.analysis import SolutionAnalysis


class BaseRepository:
    """Base repository with common operations."""

    def __init__(self, collection_name: str):
        self.db = MongoDB()
        self.collection: Collection = self.db.get_collection(collection_name)

    def find_one(self, query: Dict) -> Optional[Dict]:
        """Find a single document.

        Args:
            query: Query filter

        Returns:
            Document or None if not found
        """
        return self.collection.find_one(query)

    def find_many(self, query: Dict, limit: int = 0, skip: int = 0) -> List[Dict]:
        """Find multiple documents.

        Args:
            query: Query filter
            limit: Maximum number of documents to return
            skip: Number of documents to skip

        Returns:
            List of documents
        """
        cursor = self.collection.find(query)
        if skip:
            cursor = cursor.skip(skip)
        if limit:
            cursor = cursor.limit(limit)
        return list(cursor)

    def insert_one(self, document: Dict) -> str:
        """Insert a single document.

        Args:
            document: Document to insert

        Returns:
            ID of the inserted document
        """
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def update_one(self, query: Dict, update: Dict) -> int:
        """Update a single document.

        Args:
            query: Query filter
            update: Update operations

        Returns:
            Number of modified documents
        """
        result = self.collection.update_one(query, update)
        return result.modified_count

    def delete_one(self, query: Dict) -> int:
        """Delete a single document.

        Args:
            query: Query filter

        Returns:
            Number of deleted documents
        """
        result = self.collection.delete_one(query)
        return result.deleted_count


class AssessmentRepository(BaseRepository):
    """Repository for assessment operations."""

    def __init__(self):
        super().__init__(ASSESSMENTS_COLLECTION)

    def create_assessment(self, assessment: Assessment) -> str:
        """Create a new assessment.

        Args:
            assessment: Assessment to create

        Returns:
            ID of the created assessment
        """
        assessment_dict = assessment.model_dump(by_alias=True)
        return self.insert_one(assessment_dict)

    def get_assessment_by_id(self, test_id: str) -> Optional[Dict]:
        """Get an assessment by ID.

        Args:
            test_id: Assessment ID

        Returns:
            Assessment or None if not found
        """
        return self.find_one({"testId": test_id})


class SolutionRepository(BaseRepository):
    """Repository for solution operations."""

    def __init__(self):
        super().__init__(SOLUTIONS_COLLECTION)

    def create_solution(self, solution: Solution) -> str:
        """Create a new solution.

        Args:
            solution: Solution to create

        Returns:
            ID of the created solution
        """
        solution_dict = solution.model_dump()
        return self.insert_one(solution_dict)

    def get_solution_by_id(self, solution_id: str) -> Optional[Dict]:
        """Get a solution by ID.

        Args:
            solution_id: Solution ID

        Returns:
            Solution or None if not found
        """
        return self.find_one({"solution_id": solution_id})

    def get_solutions_by_test_id(self, test_id: str) -> List[Dict]:
        """Get all solutions for a test.

        Args:
            test_id: Test ID

        Returns:
            List of solutions
        """
        return self.find_many({"test_id": test_id})

    def get_solutions_by_candidate_id(self, candidate_id: str) -> List[Dict]:
        """Get all solutions for a candidate.

        Args:
            candidate_id: Candidate ID

        Returns:
            List of solutions
        """
        return self.find_many({"candidate_id": candidate_id})


class AnalysisRepository(BaseRepository):
    """Repository for analysis operations."""

    def __init__(self):
        super().__init__(ANALYSIS_COLLECTION)

    def create_analysis(self, analysis: SolutionAnalysis) -> str:
        """Create a new analysis.

        Args:
            analysis: Analysis to create

        Returns:
            ID of the created analysis
        """
        analysis_dict = analysis.model_dump()
        return self.insert_one(analysis_dict)

    def get_analysis_by_id(self, analysis_id: str) -> Optional[Dict]:
        """Get an analysis by ID.

        Args:
            analysis_id: Analysis ID

        Returns:
            Analysis or None if not found
        """
        return self.find_one({"analysis_id": analysis_id})

    def get_analysis_by_solution_id(self, solution_id: str) -> Optional[Dict]:
        """Get an analysis by solution ID.

        Args:
            solution_id: Solution ID

        Returns:
            Analysis or None if not found
        """
        return self.find_one({"solution_id": solution_id})

    def get_analyses_by_test_id(self, test_id: str) -> List[Dict]:
        """Get all analyses for a test.

        Args:
            test_id: Test ID

        Returns:
            List of analyses
        """
        return self.find_many({"test_id": test_id})
