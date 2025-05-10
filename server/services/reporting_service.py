"""
Reporting service for generating reports.
"""
import logging
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional
from bson import ObjectId

from server.services.database_service import DatabaseService
from server.services.ranking_service import RankingService

# Configure logging
logger = logging.getLogger(__name__)

class ReportingService:
    """Service for generating reports."""

    def __init__(self, db_service: DatabaseService):
        """Initialize the reporting service.

        Args:
            db_service: Database service
        """
        self.db_service = db_service
        self.ranking_service = RankingService(db_service)

    def generate_solution_report(self, solution_id: str) -> Dict:
        """Generate a report for a solution.

        Args:
            solution_id: Solution ID

        Returns:
            Report document
        """
        # Get the analysis for the solution
        analysis = self.db_service.get_analysis_by_solution_id(solution_id)

        if not analysis:
            logger.warning(f"Analysis not found for solution ID: {solution_id}")
            return {}

        # Get the solution
        solution = self.db_service.get_solution_by_id(solution_id)

        if not solution:
            logger.warning(f"Solution not found: {solution_id}")
            return {}

        # Get the assessment
        assessment = self.db_service.get_assessment_by_id(solution.get("test_id", ""))

        if not assessment:
            logger.warning(f"Assessment not found for test ID: {solution.get('test_id', '')}")
            return {}

        # Generate report
        report = {
            "report_id": str(uuid.uuid4()),
            "analysis_id": analysis.get("analysis_id", ""),
            "solution_id": solution_id,
            "test_id": solution.get("test_id", ""),
            "candidate_id": solution.get("candidate_id", ""),
            "generated_at": datetime.now().isoformat(),
            "overall_score": analysis.get("overall_score", 0.0),
            "summary": self._generate_summary(analysis),
            "coding_analysis": self._format_coding_analysis(analysis.get("coding_analyses", [])),
            "mcq_analysis": self._format_mcq_analysis(analysis.get("mcq_analyses", [])),
            "open_ended_analysis": self._format_open_ended_analysis(analysis.get("open_ended_analyses", [])),
            "strengths": self._identify_strengths(analysis),
            "areas_for_improvement": self._identify_improvements(analysis),
            "recommendations": self._generate_recommendations(analysis)
        }

        # Store the report
        report_id = self.db_service.store_report(report)
        logger.info(f"Report stored with ID: {report_id}")

        # Convert report_id to string if it's an ObjectId
        if isinstance(report_id, ObjectId):
            report_id = str(report_id)

        return report_id

    def generate_test_report(self, test_id: str) -> Dict:
        """Generate a report for a test.

        Args:
            test_id: Test ID

        Returns:
            Report document
        """
        # Get all analyses for the test
        analyses = self.db_service.get_analyses_by_test_id(test_id)

        if not analyses:
            logger.warning(f"No analyses found for test ID: {test_id}")
            return {}

        # Rank candidates
        ranked_candidates = self.ranking_service.rank_candidates(test_id)

        # Get the assessment
        assessment = self.db_service.get_assessment_by_id(test_id)

        if not assessment:
            logger.warning(f"Assessment not found for test ID: {test_id}")
            return {}

        # Generate report
        report = {
            "report_id": str(uuid.uuid4()),
            "test_id": test_id,
            "generated_at": datetime.now().isoformat(),
            "candidate_count": len(ranked_candidates),
            "top_candidates": ranked_candidates[:5] if len(ranked_candidates) > 5 else ranked_candidates,
            "average_score": sum(candidate.get("overall_score", 0.0) for candidate in ranked_candidates) / len(ranked_candidates),
            "score_distribution": self._calculate_score_distribution(ranked_candidates),
            "coding_performance": self._analyze_coding_performance(ranked_candidates),
            "mcq_performance": self._analyze_mcq_performance(ranked_candidates),
            "open_ended_performance": self._analyze_open_ended_performance(ranked_candidates)
        }

        # Store the report
        report_id = self.db_service.store_report(report)
        logger.info(f"Report stored with ID: {report_id}")

        # Convert report_id to string if it's an ObjectId
        if isinstance(report_id, ObjectId):
            report_id = str(report_id)

        return report_id

    def _generate_summary(self, analysis: Dict) -> str:
        """Generate a summary of the analysis.

        Args:
            analysis: Analysis document

        Returns:
            Summary text
        """
        overall_score = analysis.get("overall_score", 0.0)

        # Get average scores for different question types
        coding_scores = [a.get("overall_score", 0.0) for a in analysis.get("coding_analyses", [])]
        mcq_scores = [a.get("correctness_score", 0.0) for a in analysis.get("mcq_analyses", [])]
        open_ended_scores = [a.get("overall_score", 0.0) for a in analysis.get("open_ended_analyses", [])]

        avg_coding_score = sum(coding_scores) / len(coding_scores) if coding_scores else 0.0
        avg_mcq_score = sum(mcq_scores) / len(mcq_scores) if mcq_scores else 0.0
        avg_open_ended_score = sum(open_ended_scores) / len(open_ended_scores) if open_ended_scores else 0.0

        # Generate summary text
        if overall_score >= 0.8:
            performance_level = "excellent"
        elif overall_score >= 0.6:
            performance_level = "good"
        elif overall_score >= 0.4:
            performance_level = "average"
        else:
            performance_level = "below average"

        summary = f"The candidate demonstrated {performance_level} performance with an overall score of {overall_score:.2f}. "

        if coding_scores:
            summary += f"In coding questions, the candidate scored {avg_coding_score:.2f}. "

        if mcq_scores:
            summary += f"In multiple-choice questions, the candidate scored {avg_mcq_score:.2f}. "

        if open_ended_scores:
            summary += f"In open-ended questions, the candidate scored {avg_open_ended_score:.2f}. "

        return summary

    def _format_coding_analysis(self, coding_analyses: List[Dict]) -> List[Dict]:
        """Format coding analysis data for the report.

        Args:
            coding_analyses: List of coding analyses

        Returns:
            Formatted coding analysis data
        """
        formatted_analyses = []

        for analysis in coding_analyses:
            formatted_analysis = {
                "question_id": analysis.get("question_id", ""),
                "correctness_score": analysis.get("correctness_score", 0.0),
                "code_quality": {
                    "maintainability_index": analysis.get("code_quality", {}).get("maintainability_index", 0.0),
                    "cyclomatic_complexity": analysis.get("code_quality", {}).get("cyclomatic_complexity", 0.0),
                    "comment_ratio": analysis.get("code_quality", {}).get("comment_ratio", 0.0)
                },
                "ai_detection": {
                    "probability": analysis.get("ai_detection", {}).get("ai_generated_probability", 0.0),
                    "flagged_patterns": analysis.get("ai_detection", {}).get("flagged_patterns", [])
                },
                "style_analysis": {
                    "style_score": analysis.get("style_analysis", {}).get("style_score", 0.0),
                    "naming_convention_score": analysis.get("style_analysis", {}).get("naming_convention_score", 0.0),
                    "issues": analysis.get("style_analysis", {}).get("style_issues", [])
                },
                "performance_analysis": {
                    "efficiency_score": analysis.get("performance_analysis", {}).get("efficiency_score", 0.0),
                    "time_complexity_score": analysis.get("performance_analysis", {}).get("time_complexity_score", 0.0),
                    "space_complexity_score": analysis.get("performance_analysis", {}).get("space_complexity_score", 0.0),
                    "optimization_suggestions": analysis.get("performance_analysis", {}).get("optimization_suggestions", [])
                },
                "overall_score": analysis.get("overall_score", 0.0),
                "test_case_results": analysis.get("test_case_results", [])
            }

            # Calculate test pass rate
            test_results = analysis.get("test_case_results", [])
            passed_tests = sum(1 for test in test_results if test.get("passed", False))
            total_tests = len(test_results)

            formatted_analysis["passed_tests"] = passed_tests
            formatted_analysis["total_tests"] = total_tests
            formatted_analysis["test_pass_rate"] = passed_tests / total_tests if total_tests > 0 else 0.0

            formatted_analyses.append(formatted_analysis)

        return formatted_analyses

    def _format_mcq_analysis(self, mcq_analyses: List[Dict]) -> List[Dict]:
        """Format MCQ analysis data for the report.

        Args:
            mcq_analyses: List of MCQ analyses

        Returns:
            Formatted MCQ analysis data
        """
        formatted_analyses = []

        for analysis in mcq_analyses:
            formatted_analysis = {
                "question_id": analysis.get("question_id", ""),
                "correctness_score": analysis.get("correctness_score", 0.0),
                "is_correct": analysis.get("is_correct", False)
            }

            formatted_analyses.append(formatted_analysis)

        return formatted_analyses

    def _format_open_ended_analysis(self, open_ended_analyses: List[Dict]) -> List[Dict]:
        """Format open-ended analysis data for the report.

        Args:
            open_ended_analyses: List of open-ended analyses

        Returns:
            Formatted open-ended analysis data
        """
        formatted_analyses = []

        for analysis in open_ended_analyses:
            formatted_analysis = {
                "question_id": analysis.get("question_id", ""),
                "relevance_score": analysis.get("relevance_score", 0.0),
                "clarity_score": analysis.get("clarity_score", 0.0),
                "overall_score": analysis.get("overall_score", 0.0)
            }

            formatted_analyses.append(formatted_analysis)

        return formatted_analyses

    def _identify_strengths(self, analysis: Dict) -> List[str]:
        """Identify candidate strengths from the analysis.

        Args:
            analysis: Analysis document

        Returns:
            List of strengths
        """
        strengths = []

        # Check coding strengths
        coding_analyses = analysis.get("coding_analyses", [])
        if coding_analyses:
            avg_correctness = sum(a.get("correctness_score", 0.0) for a in coding_analyses) / len(coding_analyses)
            avg_code_quality = sum(a.get("code_quality", {}).get("maintainability_index", 0.0) / 100.0 for a in coding_analyses) / len(coding_analyses)
            avg_style = sum(a.get("style_analysis", {}).get("style_score", 0.0) for a in coding_analyses) / len(coding_analyses)
            avg_performance = sum(a.get("performance_analysis", {}).get("efficiency_score", 0.0) for a in coding_analyses) / len(coding_analyses)

            # Calculate test pass rate
            total_passed = 0
            total_tests = 0

            for analysis_item in coding_analyses:
                test_results = analysis_item.get("test_case_results", [])
                total_tests += len(test_results)
                total_passed += sum(1 for test in test_results if test.get("passed", False))

            test_pass_rate = total_passed / total_tests if total_tests > 0 else 0.0

            if avg_correctness >= 0.8:
                strengths.append("Strong problem-solving skills with high correctness in coding solutions")

            if test_pass_rate >= 0.8:
                strengths.append(f"Passed {total_passed} out of {total_tests} test cases ({test_pass_rate:.0%})")

            if avg_code_quality >= 0.8:
                strengths.append("Excellent code quality and maintainability")

            if avg_style >= 0.8:
                strengths.append("Good coding style and adherence to conventions")

            if avg_performance >= 0.8:
                strengths.append("Efficient code with good performance characteristics")

        # Check MCQ strengths
        mcq_analyses = analysis.get("mcq_analyses", [])
        if mcq_analyses:
            avg_mcq_score = sum(a.get("correctness_score", 0.0) for a in mcq_analyses) / len(mcq_analyses)

            if avg_mcq_score >= 0.8:
                strengths.append("Strong knowledge base demonstrated in multiple-choice questions")

        # Check open-ended strengths
        open_ended_analyses = analysis.get("open_ended_analyses", [])
        if open_ended_analyses:
            avg_relevance = sum(a.get("relevance_score", 0.0) for a in open_ended_analyses) / len(open_ended_analyses)
            avg_clarity = sum(a.get("clarity_score", 0.0) for a in open_ended_analyses) / len(open_ended_analyses)

            if avg_relevance >= 0.8:
                strengths.append("Excellent understanding of concepts in open-ended responses")

            if avg_clarity >= 0.8:
                strengths.append("Clear and concise communication in written responses")

        return strengths

    def _identify_improvements(self, analysis: Dict) -> List[str]:
        """Identify areas for improvement from the analysis.

        Args:
            analysis: Analysis document

        Returns:
            List of areas for improvement
        """
        improvements = []

        # Check coding improvements
        coding_analyses = analysis.get("coding_analyses", [])
        if coding_analyses:
            avg_correctness = sum(a.get("correctness_score", 0.0) for a in coding_analyses) / len(coding_analyses)
            avg_code_quality = sum(a.get("code_quality", {}).get("maintainability_index", 0.0) / 100.0 for a in coding_analyses) / len(coding_analyses)
            avg_style = sum(a.get("style_analysis", {}).get("style_score", 0.0) for a in coding_analyses) / len(coding_analyses)
            avg_performance = sum(a.get("performance_analysis", {}).get("efficiency_score", 0.0) for a in coding_analyses) / len(coding_analyses)

            # Calculate test pass rate
            total_passed = 0
            total_tests = 0

            for analysis_item in coding_analyses:
                test_results = analysis_item.get("test_case_results", [])
                total_tests += len(test_results)
                total_passed += sum(1 for test in test_results if test.get("passed", False))

            test_pass_rate = total_passed / total_tests if total_tests > 0 else 0.0

            if avg_correctness < 0.6:
                improvements.append("Needs improvement in problem-solving and solution correctness")

            if test_pass_rate < 0.6:
                improvements.append(f"Failed {total_tests - total_passed} out of {total_tests} test cases ({1 - test_pass_rate:.0%})")

            if avg_code_quality < 0.6:
                improvements.append("Code quality and maintainability could be improved")

            if avg_style < 0.6:
                improvements.append("Should focus on improving coding style and conventions")

            if avg_performance < 0.6:
                improvements.append("Code efficiency and performance need attention")

        # Check MCQ improvements
        mcq_analyses = analysis.get("mcq_analyses", [])
        if mcq_analyses:
            avg_mcq_score = sum(a.get("correctness_score", 0.0) for a in mcq_analyses) / len(mcq_analyses)

            if avg_mcq_score < 0.6:
                improvements.append("Knowledge gaps identified in multiple-choice questions")

        # Check open-ended improvements
        open_ended_analyses = analysis.get("open_ended_analyses", [])
        if open_ended_analyses:
            avg_relevance = sum(a.get("relevance_score", 0.0) for a in open_ended_analyses) / len(open_ended_analyses)
            avg_clarity = sum(a.get("clarity_score", 0.0) for a in open_ended_analyses) / len(open_ended_analyses)

            if avg_relevance < 0.6:
                improvements.append("Needs to improve understanding of concepts in open-ended responses")

            if avg_clarity < 0.6:
                improvements.append("Communication clarity in written responses could be improved")

        return improvements

    def _generate_recommendations(self, analysis: Dict) -> List[str]:
        """Generate recommendations based on the analysis.

        Args:
            analysis: Analysis document

        Returns:
            List of recommendations
        """
        recommendations = []

        # Check coding recommendations
        coding_analyses = analysis.get("coding_analyses", [])
        if coding_analyses:
            # Collect all optimization suggestions
            all_suggestions = []
            for analysis_item in coding_analyses:
                suggestions = analysis_item.get("performance_analysis", {}).get("optimization_suggestions", [])
                all_suggestions.extend(suggestions)

            # Add unique suggestions to recommendations
            unique_suggestions = list(set(all_suggestions))
            recommendations.extend(unique_suggestions)

            # Check for AI detection
            ai_probabilities = [a.get("ai_detection", {}).get("ai_generated_probability", 0.0) for a in coding_analyses]
            avg_ai_probability = sum(ai_probabilities) / len(ai_probabilities) if ai_probabilities else 0.0

            if avg_ai_probability > 0.7:
                recommendations.append("Candidate should demonstrate more original work in coding solutions")

            # Check for failed test cases
            for analysis_item in coding_analyses:
                test_results = analysis_item.get("test_case_results", [])
                failed_tests = [test for test in test_results if not test.get("passed", False)]

                if failed_tests:
                    question_id = analysis_item.get("question_id", "")
                    recommendations.append(f"Review failed test cases for question {question_id}")

        return recommendations

    def _calculate_score_distribution(self, ranked_candidates: List[Dict]) -> Dict[str, int]:
        """Calculate the distribution of scores.

        Args:
            ranked_candidates: List of ranked candidates

        Returns:
            Score distribution
        """
        distribution = {
            "excellent": 0,  # 0.8 - 1.0
            "good": 0,       # 0.6 - 0.8
            "average": 0,    # 0.4 - 0.6
            "poor": 0        # 0.0 - 0.4
        }

        for candidate in ranked_candidates:
            score = candidate.get("overall_score", 0.0)

            if score >= 0.8:
                distribution["excellent"] += 1
            elif score >= 0.6:
                distribution["good"] += 1
            elif score >= 0.4:
                distribution["average"] += 1
            else:
                distribution["poor"] += 1

        return distribution

    def _analyze_coding_performance(self, ranked_candidates: List[Dict]) -> Dict[str, Any]:
        """Analyze coding performance across all candidates.

        Args:
            ranked_candidates: List of ranked candidates

        Returns:
            Coding performance analysis
        """
        if not ranked_candidates:
            return {}

        coding_scores = [candidate.get("coding_score", 0.0) for candidate in ranked_candidates]
        avg_coding_score = sum(coding_scores) / len(coding_scores) if coding_scores else 0.0

        # Get detailed metrics
        correctness_scores = [candidate.get("coding_details", {}).get("correctness", 0.0) for candidate in ranked_candidates]
        originality_scores = [candidate.get("coding_details", {}).get("originality", 0.0) for candidate in ranked_candidates]
        code_quality_scores = [candidate.get("coding_details", {}).get("code_quality", 0.0) for candidate in ranked_candidates]
        performance_scores = [candidate.get("coding_details", {}).get("performance", 0.0) for candidate in ranked_candidates]
        style_scores = [candidate.get("coding_details", {}).get("style", 0.0) for candidate in ranked_candidates]

        # Get test pass rates
        test_pass_rates = [candidate.get("coding_details", {}).get("test_pass_rate", 0.0) for candidate in ranked_candidates]
        avg_test_pass_rate = sum(test_pass_rates) / len(test_pass_rates) if test_pass_rates else 0.0

        return {
            "average_score": avg_coding_score,
            "average_test_pass_rate": avg_test_pass_rate,
            "metrics": {
                "correctness": sum(correctness_scores) / len(correctness_scores) if correctness_scores else 0.0,
                "originality": sum(originality_scores) / len(originality_scores) if originality_scores else 0.0,
                "code_quality": sum(code_quality_scores) / len(code_quality_scores) if code_quality_scores else 0.0,
                "performance": sum(performance_scores) / len(performance_scores) if performance_scores else 0.0,
                "style": sum(style_scores) / len(style_scores) if style_scores else 0.0
            }
        }

    def _analyze_mcq_performance(self, ranked_candidates: List[Dict]) -> Dict[str, Any]:
        """Analyze MCQ performance across all candidates.

        Args:
            ranked_candidates: List of ranked candidates

        Returns:
            MCQ performance analysis
        """
        if not ranked_candidates:
            return {}

        mcq_scores = [candidate.get("mcq_score", 0.0) for candidate in ranked_candidates]
        avg_mcq_score = sum(mcq_scores) / len(mcq_scores) if mcq_scores else 0.0

        return {
            "average_score": avg_mcq_score
        }

    def _analyze_open_ended_performance(self, ranked_candidates: List[Dict]) -> Dict[str, Any]:
        """Analyze open-ended performance across all candidates.

        Args:
            ranked_candidates: List of ranked candidates

        Returns:
            Open-ended performance analysis
        """
        if not ranked_candidates:
            return {}

        open_ended_scores = [candidate.get("open_ended_score", 0.0) for candidate in ranked_candidates]
        avg_open_ended_score = sum(open_ended_scores) / len(open_ended_scores) if open_ended_scores else 0.0

        # Get detailed metrics
        relevance_scores = [candidate.get("open_ended_details", {}).get("relevance", 0.0) for candidate in ranked_candidates]
        clarity_scores = [candidate.get("open_ended_details", {}).get("clarity", 0.0) for candidate in ranked_candidates]

        return {
            "average_score": avg_open_ended_score,
            "metrics": {
                "relevance": sum(relevance_scores) / len(relevance_scores) if relevance_scores else 0.0,
                "clarity": sum(clarity_scores) / len(clarity_scores) if clarity_scores else 0.0
            }
        }
