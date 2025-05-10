"""
Report generator for assessment analysis.
"""
from typing import Dict, List, Any
import json
from datetime import datetime
import uuid

from app.database.repositories import AnalysisRepository, SolutionRepository, AssessmentRepository


class ReportGenerator:
    """Generator for assessment analysis reports."""

    def __init__(self):
        """Initialize the report generator."""
        self.analysis_repo = AnalysisRepository()
        self.solution_repo = SolutionRepository()
        self.assessment_repo = AssessmentRepository()

    def generate_individual_report(self, analysis_id: str) -> Dict[str, Any]:
        """Generate a report for an individual candidate.

        Args:
            analysis_id: Analysis ID

        Returns:
            Report data
        """
        # Get analysis data
        analysis = self.analysis_repo.get_analysis_by_id(analysis_id)
        
        if not analysis:
            return {"error": "Analysis not found"}
        
        # Get solution data
        solution = self.solution_repo.get_solution_by_id(analysis.get("solution_id", ""))
        
        if not solution:
            return {"error": "Solution not found"}
        
        # Get assessment data
        assessment = self.assessment_repo.get_assessment_by_id(analysis.get("test_id", ""))
        
        if not assessment:
            return {"error": "Assessment not found"}
        
        # Generate report
        report = {
            "report_id": str(uuid.uuid4()),
            "analysis_id": analysis_id,
            "solution_id": analysis.get("solution_id", ""),
            "test_id": analysis.get("test_id", ""),
            "candidate_id": analysis.get("candidate_id", ""),
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
        
        return report

    def generate_comparative_report(self, test_id: str, ranked_candidates: List[Dict]) -> Dict[str, Any]:
        """Generate a comparative report for all candidates in a test.

        Args:
            test_id: Test ID
            ranked_candidates: List of ranked candidates

        Returns:
            Report data
        """
        if not ranked_candidates:
            return {"error": "No candidates found"}
        
        # Get assessment data
        assessment = self.assessment_repo.get_assessment_by_id(test_id)
        
        if not assessment:
            return {"error": "Assessment not found"}
        
        # Generate report
        report = {
            "report_id": str(uuid.uuid4()),
            "test_id": test_id,
            "generated_at": datetime.now().isoformat(),
            "candidate_count": len(ranked_candidates),
            "top_candidates": ranked_candidates[:5] if len(ranked_candidates) > 5 else ranked_candidates,
            "average_score": sum(candidate["overall_score"] for candidate in ranked_candidates) / len(ranked_candidates),
            "score_distribution": self._calculate_score_distribution(ranked_candidates),
            "coding_performance": self._analyze_coding_performance(ranked_candidates),
            "mcq_performance": self._analyze_mcq_performance(ranked_candidates),
            "open_ended_performance": self._analyze_open_ended_performance(ranked_candidates)
        }
        
        return report

    def _generate_summary(self, analysis: Dict) -> str:
        """Generate a summary of the analysis.

        Args:
            analysis: Analysis data

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
                "overall_score": analysis.get("overall_score", 0.0)
            }
            
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
            analysis: Analysis data

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
            
            if avg_correctness >= 0.8:
                strengths.append("Strong problem-solving skills with high correctness in coding solutions")
            
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
            analysis: Analysis data

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
            
            if avg_correctness < 0.6:
                improvements.append("Needs improvement in problem-solving and solution correctness")
            
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
            analysis: Analysis data

        Returns:
            List of recommendations
        """
        recommendations = []
        
        # Check coding recommendations
        coding_analyses = analysis.get("coding_analyses", [])
        if coding_analyses:
            # Collect all optimization suggestions
            all_suggestions = []
            for analysis in coding_analyses:
                suggestions = analysis.get("performance_analysis", {}).get("optimization_suggestions", [])
                all_suggestions.extend(suggestions)
            
            # Add unique suggestions to recommendations
            unique_suggestions = list(set(all_suggestions))
            recommendations.extend(unique_suggestions)
            
            # Check for AI detection
            ai_probabilities = [a.get("ai_detection", {}).get("ai_generated_probability", 0.0) for a in coding_analyses]
            avg_ai_probability = sum(ai_probabilities) / len(ai_probabilities) if ai_probabilities else 0.0
            
            if avg_ai_probability > 0.7:
                recommendations.append("Candidate should demonstrate more original work in coding solutions")
        
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
        
        return {
            "average_score": avg_coding_score,
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
