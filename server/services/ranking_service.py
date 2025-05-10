"""
Ranking service for ranking candidates.
"""
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

from server.services.database_service import DatabaseService

# Configure logging
logger = logging.getLogger(__name__)

class RankingService:
    """Service for ranking candidates."""

    def __init__(self, db_service: DatabaseService):
        """Initialize the ranking service.

        Args:
            db_service: Database service
        """
        self.db_service = db_service

    def rank_candidates(self, test_id: str) -> List[Dict]:
        """Rank candidates based on their assessment results.

        Args:
            test_id: Test ID

        Returns:
            List of ranked candidates with scores
        """
        # Get all analyses for the test
        analyses = self.db_service.get_analyses_by_test_id(test_id)

        if not analyses:
            logger.warning(f"No analyses found for test ID: {test_id}")
            return []

        # Calculate weighted scores for each candidate
        ranked_candidates = []

        for analysis in analyses:
            candidate_id = analysis.get("candidate_id", "")
            overall_score = analysis.get("overall_score", 0.0)

            # Calculate detailed scores
            coding_scores = self._calculate_coding_scores(analysis.get("coding_analyses", []))
            mcq_scores = self._calculate_mcq_scores(analysis.get("mcq_analyses", []))
            open_ended_scores = self._calculate_open_ended_scores(analysis.get("open_ended_analyses", []))

            # Create candidate ranking entry
            ranked_candidate = {
                "candidate_id": candidate_id,
                "overall_score": overall_score,
                "coding_score": coding_scores.get("overall", 0.0),
                "mcq_score": mcq_scores.get("overall", 0.0),
                "open_ended_score": open_ended_scores.get("overall", 0.0),
                "coding_details": coding_scores,
                "mcq_details": mcq_scores,
                "open_ended_details": open_ended_scores,
                "analysis_id": analysis.get("analysis_id", ""),
                "solution_id": analysis.get("solution_id", ""),
                "ranked_at": datetime.now().isoformat()
            }

            ranked_candidates.append(ranked_candidate)

        # Sort candidates by overall score (descending)
        ranked_candidates.sort(key=lambda x: x["overall_score"], reverse=True)

        # Add rank to each candidate
        for i, candidate in enumerate(ranked_candidates):
            candidate["rank"] = i + 1

        return ranked_candidates

    def _calculate_coding_scores(self, coding_analyses: List[Dict]) -> Dict[str, Any]:
        """Calculate detailed coding scores.

        Args:
            coding_analyses: List of coding question analyses

        Returns:
            Detailed coding scores
        """
        if not coding_analyses:
            return {"overall": 0.0}

        # Calculate average scores
        avg_correctness = sum(analysis.get("correctness_score", 0.0) for analysis in coding_analyses) / len(coding_analyses)

        # Handle AI detection scores
        ai_scores = []
        for analysis in coding_analyses:
            ai_detection = analysis.get("ai_detection", {})
            if isinstance(ai_detection, dict):
                ai_score = 1.0 - ai_detection.get("ai_generated_probability", 0.0)
            else:
                ai_score = 0.9  # Default value
            ai_scores.append(ai_score)
        avg_ai_detection = sum(ai_scores) / len(ai_scores) if ai_scores else 0.9

        # Handle code quality scores
        quality_scores = []
        for analysis in coding_analyses:
            code_quality = analysis.get("code_quality", {})
            if isinstance(code_quality, dict):
                maintainability = code_quality.get("maintainability_index", 0.0)
                if isinstance(maintainability, (int, float)):
                    quality_score = float(maintainability) / 100.0
                else:
                    quality_score = 0.8  # Default value
            else:
                quality_score = 0.8  # Default value
            quality_scores.append(quality_score)
        avg_code_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0.8

        # Handle performance scores
        performance_scores = []
        for analysis in coding_analyses:
            performance = analysis.get("performance_analysis", {})
            if isinstance(performance, dict):
                performance_score = performance.get("efficiency_score", 0.0)
            else:
                performance_score = 0.8  # Default value
            performance_scores.append(performance_score)
        avg_performance = sum(performance_scores) / len(performance_scores) if performance_scores else 0.8

        # Handle style scores
        style_scores = []
        for analysis in coding_analyses:
            style = analysis.get("style_analysis", {})
            if isinstance(style, dict):
                style_score = style.get("style_score", 0.0)
            else:
                style_score = 0.8  # Default value
            style_scores.append(style_score)
        avg_style = sum(style_scores) / len(style_scores) if style_scores else 0.8

        # Calculate test pass rate
        total_passed = 0
        total_tests = 0

        for analysis in coding_analyses:
            test_results = analysis.get("test_case_results", [])
            total_tests += len(test_results)
            total_passed += sum(1 for test in test_results if test.get("passed", False))

        test_pass_rate = total_passed / total_tests if total_tests > 0 else 0.0

        # Weights for different aspects
        weights = {
            "correctness": 0.4,
            "ai_detection": 0.1,
            "code_quality": 0.2,
            "performance": 0.2,
            "style": 0.1
        }

        # Calculate weighted overall score
        overall_score = (
            avg_correctness * weights["correctness"] +
            avg_ai_detection * weights["ai_detection"] +
            avg_code_quality * weights["code_quality"] +
            avg_performance * weights["performance"] +
            avg_style * weights["style"]
        )

        return {
            "overall": overall_score,
            "correctness": avg_correctness,
            "originality": avg_ai_detection,
            "code_quality": avg_code_quality,
            "performance": avg_performance,
            "style": avg_style,
            "test_pass_rate": test_pass_rate,
            "passed_tests": total_passed,
            "total_tests": total_tests
        }

    def _calculate_mcq_scores(self, mcq_analyses: List[Dict]) -> Dict[str, Any]:
        """Calculate detailed MCQ scores.

        Args:
            mcq_analyses: List of MCQ question analyses

        Returns:
            Detailed MCQ scores
        """
        if not mcq_analyses:
            return {"overall": 0.0}

        # Calculate average scores
        avg_correctness = sum(analysis.get("correctness_score", 0.0) for analysis in mcq_analyses) / len(mcq_analyses)

        # Calculate correct answer rate
        correct_count = sum(1 for analysis in mcq_analyses if analysis.get("is_correct", False))
        total_count = len(mcq_analyses)
        correct_rate = correct_count / total_count if total_count > 0 else 0.0

        return {
            "overall": avg_correctness,
            "correctness": avg_correctness,
            "correct_rate": correct_rate,
            "correct_count": correct_count,
            "total_count": total_count
        }

    def _calculate_open_ended_scores(self, open_ended_analyses: List[Dict]) -> Dict[str, Any]:
        """Calculate detailed open-ended scores.

        Args:
            open_ended_analyses: List of open-ended question analyses

        Returns:
            Detailed open-ended scores
        """
        if not open_ended_analyses:
            return {"overall": 0.0}

        # Calculate average scores
        avg_relevance = sum(analysis.get("relevance_score", 0.0) for analysis in open_ended_analyses) / len(open_ended_analyses)
        avg_clarity = sum(analysis.get("clarity_score", 0.0) for analysis in open_ended_analyses) / len(open_ended_analyses)

        # Weights for different aspects
        weights = {
            "relevance": 0.6,
            "clarity": 0.4
        }

        # Calculate weighted overall score
        overall_score = (
            avg_relevance * weights["relevance"] +
            avg_clarity * weights["clarity"]
        )

        return {
            "overall": overall_score,
            "relevance": avg_relevance,
            "clarity": avg_clarity
        }
