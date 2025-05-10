"""
Service for ranking candidates based on their assessment results.
"""
from typing import Dict, List, Any
import uuid
from datetime import datetime

from app.database.repositories import AnalysisRepository
from app.core.config import ANALYSIS_CONFIG


class RankingService:
    """Service for ranking candidates based on their assessment results."""

    def __init__(self):
        """Initialize the ranking service."""
        self.analysis_repo = AnalysisRepository()

    def rank_candidates(self, test_id: str) -> List[Dict[str, Any]]:
        """Rank candidates based on their assessment results.

        Args:
            test_id: Test ID

        Returns:
            List of ranked candidates with scores
        """
        # Get all analyses for the test
        analyses = self.analysis_repo.get_analyses_by_test_id(test_id)
        
        if not analyses:
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
        
        # Get weights from config
        weights = ANALYSIS_CONFIG.get("coding", {})
        correctness_weight = weights.get("correctness_weight", 0.4)
        ai_detection_weight = weights.get("ai_detection_weight", 0.1)
        code_quality_weight = weights.get("code_quality_weight", 0.2)
        performance_weight = weights.get("performance_weight", 0.2)
        style_weight = weights.get("style_weight", 0.1)
        
        # Calculate average scores
        avg_correctness = sum(analysis.get("correctness_score", 0.0) for analysis in coding_analyses) / len(coding_analyses)
        avg_ai_detection = 1.0 - sum(analysis.get("ai_detection", {}).get("ai_generated_probability", 0.0) for analysis in coding_analyses) / len(coding_analyses)
        avg_code_quality = sum(analysis.get("code_quality", {}).get("maintainability_index", 0.0) / 100.0 for analysis in coding_analyses) / len(coding_analyses)
        avg_performance = sum(analysis.get("performance_analysis", {}).get("efficiency_score", 0.0) for analysis in coding_analyses) / len(coding_analyses)
        avg_style = sum(analysis.get("style_analysis", {}).get("style_score", 0.0) for analysis in coding_analyses) / len(coding_analyses)
        
        # Calculate weighted overall score
        overall_score = (
            avg_correctness * correctness_weight +
            avg_ai_detection * ai_detection_weight +
            avg_code_quality * code_quality_weight +
            avg_performance * performance_weight +
            avg_style * style_weight
        )
        
        return {
            "overall": overall_score,
            "correctness": avg_correctness,
            "originality": avg_ai_detection,
            "code_quality": avg_code_quality,
            "performance": avg_performance,
            "style": avg_style
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
        
        # Get weights from config
        weights = ANALYSIS_CONFIG.get("mcq", {})
        correctness_weight = weights.get("correctness_weight", 1.0)
        
        # Calculate average scores
        avg_correctness = sum(analysis.get("correctness_score", 0.0) for analysis in mcq_analyses) / len(mcq_analyses)
        
        # Calculate weighted overall score
        overall_score = avg_correctness * correctness_weight
        
        return {
            "overall": overall_score,
            "correctness": avg_correctness
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
        
        # Get weights from config
        weights = ANALYSIS_CONFIG.get("open_ended", {})
        relevance_weight = weights.get("relevance_weight", 0.6)
        clarity_weight = weights.get("clarity_weight", 0.4)
        
        # Calculate average scores
        avg_relevance = sum(analysis.get("relevance_score", 0.0) for analysis in open_ended_analyses) / len(open_ended_analyses)
        avg_clarity = sum(analysis.get("clarity_score", 0.0) for analysis in open_ended_analyses) / len(open_ended_analyses)
        
        # Calculate weighted overall score
        overall_score = (
            avg_relevance * relevance_weight +
            avg_clarity * clarity_weight
        )
        
        return {
            "overall": overall_score,
            "relevance": avg_relevance,
            "clarity": avg_clarity
        }
