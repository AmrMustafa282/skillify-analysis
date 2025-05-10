"""
Analysis service for analyzing solutions.
"""
import logging
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional

from server.services.database_service import DatabaseService
from server.services.analyzers.correctness_analyzer import CorrectnessAnalyzer
from server.services.analyzers.code_quality_analyzer import CodeQualityAnalyzer
from server.services.analyzers.ai_detection_analyzer import AIDetectionAnalyzer
from server.services.analyzers.style_analyzer import StyleAnalyzer
from server.services.analyzers.performance_analyzer import PerformanceAnalyzer
from server.services.transformers.solution_transformer import SolutionTransformer

# Configure logging
logger = logging.getLogger(__name__)

class AnalysisService:
    """Service for analyzing solutions."""

    def __init__(self, db_service: DatabaseService):
        """Initialize the analysis service.

        Args:
            db_service: Database service
        """
        self.db_service = db_service
        self.transformer = SolutionTransformer()

        # Initialize analyzers
        self.analyzers = {
            "correctness": CorrectnessAnalyzer(),
            "code_quality": CodeQualityAnalyzer(),
            "ai_detection": AIDetectionAnalyzer(),
            "style": StyleAnalyzer(),
            "performance": PerformanceAnalyzer()
        }

    def analyze_solution(self, solution: Dict, assessment: Dict) -> Dict:
        """Analyze a solution.

        Args:
            solution: Solution document
            assessment: Assessment document

        Returns:
            Analysis result
        """
        # Transform solution into analyzable format
        transformed_data = self.transformer.transform_to_analyzable_format(solution, assessment)

        # Analyze coding answers
        coding_results = self._analyze_coding_answers(transformed_data.get("coding_answers", []))

        # Analyze MCQ answers
        mcq_results = self._analyze_mcq_answers(transformed_data.get("answers", []))

        # Analyze open-ended answers
        open_ended_results = self._analyze_open_ended_answers(transformed_data.get("answers", []))

        # Calculate overall score
        overall_score = self._calculate_overall_score(coding_results, mcq_results, open_ended_results)

        # Create analysis object
        analysis = {
            "analysis_id": str(uuid.uuid4()),
            "solution_id": transformed_data.get("solution_id", ""),
            "test_id": transformed_data.get("test_id", ""),
            "candidate_id": transformed_data.get("candidate_id", ""),
            "coding_analyses": coding_results,
            "mcq_analyses": mcq_results,
            "open_ended_analyses": open_ended_results,
            "overall_score": overall_score,
            "analyzed_at": datetime.now().isoformat()
        }

        return analysis

    def _analyze_coding_answers(self, coding_answers: List[Dict]) -> List[Dict]:
        """Analyze coding answers.

        Args:
            coding_answers: List of coding answers

        Returns:
            List of coding analysis results
        """
        results = []

        for answer in coding_answers:
            # Run each analyzer on the answer
            correctness_result = self.analyzers["correctness"].analyze(answer)
            code_quality_result = self.analyzers["code_quality"].analyze(answer)
            ai_detection_result = self.analyzers["ai_detection"].analyze(answer)
            style_result = self.analyzers["style"].analyze(answer)
            performance_result = self.analyzers["performance"].analyze(answer)

            # Combine results
            analysis_result = {
                "question_id": answer.get("question_id", ""),
                "correctness_score": correctness_result.get("correctness_score", 0.0),
                "test_case_results": correctness_result.get("test_case_results", []),
                "code_quality": code_quality_result.get("code_quality", {}),
                "ai_detection": ai_detection_result.get("ai_detection", {}),
                "style_analysis": style_result.get("style_analysis", {}),
                "performance_analysis": performance_result.get("performance_analysis", {})
            }

            # Calculate overall score for this coding answer
            analysis_result["overall_score"] = self._calculate_coding_score(analysis_result)

            results.append(analysis_result)

        return results

    def _analyze_mcq_answers(self, answers: List[Dict]) -> List[Dict]:
        """Analyze MCQ answers.

        Args:
            answers: List of answers

        Returns:
            List of MCQ analysis results
        """
        results = []

        for answer in answers:
            if answer.get("answer_type") != "MCQ":
                continue

            question_id = answer.get("question_id", "")
            submitted_value = answer.get("submitted_value")
            correct_answer = answer.get("correct_answer")

            # Check if the answer is correct
            is_correct = False
            correctness_score = 0.0

            if isinstance(submitted_value, list) and isinstance(correct_answer, list):
                # Multiple selection
                if set(submitted_value) == set(correct_answer):
                    is_correct = True
                    correctness_score = 1.0
                else:
                    # Partial credit for partially correct answers
                    correct_count = len(set(submitted_value).intersection(set(correct_answer)))
                    total_count = len(set(correct_answer))
                    correctness_score = correct_count / total_count if total_count > 0 else 0.0
            else:
                # Single selection
                if str(submitted_value) == str(correct_answer):
                    is_correct = True
                    correctness_score = 1.0

            # Create analysis result
            analysis_result = {
                "question_id": question_id,
                "correctness_score": correctness_score,
                "is_correct": is_correct
            }

            results.append(analysis_result)

        return results

    def _analyze_open_ended_answers(self, answers: List[Dict]) -> List[Dict]:
        """Analyze open-ended answers.

        Args:
            answers: List of answers

        Returns:
            List of open-ended analysis results
        """
        results = []

        for answer in answers:
            if answer.get("answer_type") != "OPEN_ENDED":
                continue

            question_id = answer.get("question_id", "")

            # For open-ended questions, we would need more sophisticated analysis
            # Here we just use placeholder values
            analysis_result = {
                "question_id": question_id,
                "relevance_score": 0.7,  # Placeholder
                "clarity_score": 0.7,    # Placeholder
                "overall_score": 0.7     # Placeholder
            }

            results.append(analysis_result)

        return results

    def _calculate_coding_score(self, analysis_result: Dict) -> float:
        """Calculate overall score for a coding answer.

        Args:
            analysis_result: Analysis result for a coding answer

        Returns:
            Overall score
        """
        # Weights for different aspects
        weights = {
            "correctness": 0.4,
            "code_quality": 0.2,
            "ai_detection": 0.1,
            "style": 0.1,
            "performance": 0.2
        }

        # Extract scores
        correctness_score = analysis_result.get("correctness_score", 0.0)
        code_quality = analysis_result.get("code_quality", {})
        ai_detection = analysis_result.get("ai_detection", {})
        style_analysis = analysis_result.get("style_analysis", {})
        performance_analysis = analysis_result.get("performance_analysis", {})

        # Calculate weighted score
        # Handle the case where code_quality is a dict or a float
        code_quality_score = 0.0
        if isinstance(code_quality, dict):
            maintainability_index = code_quality.get("maintainability_index", 0.0)
            if isinstance(maintainability_index, (int, float)):
                code_quality_score = float(maintainability_index) / 100.0
            else:
                code_quality_score = 0.8  # Default value if maintainability_index is not a number

        # Handle the case where ai_detection is a dict or a float
        ai_detection_score = 0.0
        if isinstance(ai_detection, dict):
            ai_detection_score = 1.0 - ai_detection.get("ai_generated_probability", 0.0)

        # Handle the case where style_analysis is a dict or a float
        style_score = 0.0
        if isinstance(style_analysis, dict):
            style_score = style_analysis.get("style_score", 0.0)

        # Handle the case where performance_analysis is a dict or a float
        performance_score = 0.0
        if isinstance(performance_analysis, dict):
            performance_score = performance_analysis.get("efficiency_score", 0.0)

        # Calculate weighted score
        overall_score = (
            correctness_score * weights["correctness"] +
            code_quality_score * weights["code_quality"] +
            ai_detection_score * weights["ai_detection"] +
            style_score * weights["style"] +
            performance_score * weights["performance"]
        )

        return overall_score

    def _calculate_overall_score(self, coding_results: List[Dict], mcq_results: List[Dict], open_ended_results: List[Dict]) -> float:
        """Calculate overall score for a solution.

        Args:
            coding_results: List of coding analysis results
            mcq_results: List of MCQ analysis results
            open_ended_results: List of open-ended analysis results

        Returns:
            Overall score
        """
        # Calculate average scores for each question type
        coding_score = sum(result.get("overall_score", 0.0) for result in coding_results) / len(coding_results) if coding_results else 0.0
        mcq_score = sum(result.get("correctness_score", 0.0) for result in mcq_results) / len(mcq_results) if mcq_results else 0.0
        open_ended_score = sum(result.get("overall_score", 0.0) for result in open_ended_results) / len(open_ended_results) if open_ended_results else 0.0

        # Weights for different question types
        type_weights = {
            "coding": 0.6,
            "mcq": 0.3,
            "open_ended": 0.1
        }

        # Calculate weighted overall score
        overall_score = 0.0
        total_weight = 0.0

        if coding_results:
            overall_score += coding_score * type_weights["coding"]
            total_weight += type_weights["coding"]

        if mcq_results:
            overall_score += mcq_score * type_weights["mcq"]
            total_weight += type_weights["mcq"]

        if open_ended_results:
            overall_score += open_ended_score * type_weights["open_ended"]
            total_weight += type_weights["open_ended"]

        overall_score = overall_score / total_weight if total_weight > 0 else 0.0

        return overall_score
