"""
Main application entry point.
"""
import json
import uuid
from datetime import datetime
import argparse
import os
import sys

from app.database.mongodb import MongoDB
from app.database.repositories import AssessmentRepository, SolutionRepository, AnalysisRepository
from app.models.assessment import Assessment
from app.models.solution import Solution
from app.transformers.solution_transformer import SolutionTransformer
from app.analyzers.base_analyzer import AnalyzerPipeline
from app.analyzers.correctness_analyzer import CorrectnessAnalyzer
from app.analyzers.code_quality_analyzer import CodeQualityAnalyzer
from app.analyzers.ai_detection_analyzer import AIDetectionAnalyzer
from app.analyzers.style_analyzer import StyleAnalyzer
from app.analyzers.performance_analyzer import PerformanceAnalyzer
from app.ranking.ranking_service import RankingService
from app.reporting.report_generator import ReportGenerator
from app.models.analysis import SolutionAnalysis, CodingQuestionAnalysis, MCQQuestionAnalysis, OpenEndedQuestionAnalysis


def setup_mongodb():
    """Set up MongoDB connection."""
    try:
        db = MongoDB()
        print("MongoDB connection established successfully.")
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        sys.exit(1)


def load_assessment(file_path):
    """Load assessment from a JSON file.

    Args:
        file_path: Path to the assessment JSON file

    Returns:
        Assessment object
    """
    try:
        with open(file_path, 'r') as f:
            assessment_data = json.load(f)

        assessment = Assessment(**assessment_data)
        return assessment
    except Exception as e:
        print(f"Error loading assessment: {str(e)}")
        sys.exit(1)


def load_solution(file_path):
    """Load solution from a JSON file.

    Args:
        file_path: Path to the solution JSON file

    Returns:
        Solution object
    """
    try:
        with open(file_path, 'r') as f:
            solution_data = json.load(f)

        solution = Solution(**solution_data)
        return solution
    except Exception as e:
        print(f"Error loading solution: {str(e)}")
        sys.exit(1)


def store_assessment(assessment):
    """Store assessment in the database.

    Args:
        assessment: Assessment object

    Returns:
        Assessment ID
    """
    try:
        repo = AssessmentRepository()
        assessment_id = repo.create_assessment(assessment)
        print(f"Assessment stored with ID: {assessment_id}")
        return assessment_id
    except Exception as e:
        print(f"Error storing assessment: {str(e)}")
        sys.exit(1)


def store_solution(solution):
    """Store solution in the database.

    Args:
        solution: Solution object

    Returns:
        Solution ID
    """
    try:
        repo = SolutionRepository()
        solution_id = repo.create_solution(solution)
        print(f"Solution stored with ID: {solution_id}")
        return solution_id
    except Exception as e:
        print(f"Error storing solution: {str(e)}")
        sys.exit(1)


def transform_solution(solution, assessment):
    """Transform solution into analyzable format.

    Args:
        solution: Solution object
        assessment: Assessment object

    Returns:
        Transformed solution data
    """
    try:
        transformer = SolutionTransformer()
        transformed_data = transformer.transform_to_analyzable_format(solution, assessment)
        print("Solution transformed successfully.")
        return transformed_data
    except Exception as e:
        print(f"Error transforming solution: {str(e)}")
        sys.exit(1)


def analyze_solution(transformed_data):
    """Analyze the transformed solution.

    Args:
        transformed_data: Transformed solution data

    Returns:
        Analysis results
    """
    try:
        # Create analyzers for coding questions
        coding_results = []

        for coding_answer in transformed_data.get("coding_answers", []):
            # Create analyzer pipeline
            analyzers = [
                CorrectnessAnalyzer(),
                CodeQualityAnalyzer(),
                AIDetectionAnalyzer(),
                StyleAnalyzer(),
                PerformanceAnalyzer()
            ]

            pipeline = AnalyzerPipeline(analyzers)

            # Run analysis
            analysis_result = pipeline.run(coding_answer)

            # Add question ID
            analysis_result["question_id"] = coding_answer.get("question_id", "")

            # Calculate overall score
            correctness_score = analysis_result.get("correctness_score", 0.0)
            code_quality = analysis_result.get("code_quality", {})
            ai_detection = analysis_result.get("ai_detection", {})
            style_analysis = analysis_result.get("style_analysis", {})
            performance_analysis = analysis_result.get("performance_analysis", {})

            # Weights for different aspects
            weights = {
                "correctness": 0.4,
                "code_quality": 0.2,
                "ai_detection": 0.1,
                "style": 0.1,
                "performance": 0.2
            }

            # Calculate weighted score
            overall_score = (
                correctness_score * weights["correctness"] +
                (code_quality.get("maintainability_index", 0.0) / 100.0) * weights["code_quality"] +
                (1.0 - ai_detection.get("ai_generated_probability", 0.0)) * weights["ai_detection"] +
                style_analysis.get("style_score", 0.0) * weights["style"] +
                performance_analysis.get("efficiency_score", 0.0) * weights["performance"]
            )

            analysis_result["overall_score"] = overall_score

            coding_results.append(analysis_result)

        # Create simple analyzers for MCQ and open-ended questions
        mcq_results = []
        open_ended_results = []

        for answer in transformed_data.get("answers", []):
            question_id = answer.get("question_id", "")
            question_type = answer.get("question_type", "")
            submitted_value = answer.get("submitted_value", "")
            correct_answer = answer.get("correct_answer", "")

            if question_type == "MCQ":
                # Check if the answer is correct
                is_correct = False
                correctness_score = 0.0

                print(f"MCQ Question: {question_id}")
                print(f"Submitted value: {submitted_value} (type: {type(submitted_value)})")
                print(f"Correct answer: {correct_answer} (type: {type(correct_answer)})")

                if isinstance(submitted_value, list) and isinstance(correct_answer, list):
                    # Multiple selection
                    print(f"Multiple selection: comparing {set(submitted_value)} with {set(correct_answer)}")
                    if set(submitted_value) == set(correct_answer):
                        is_correct = True
                        correctness_score = 1.0
                    else:
                        # Partial credit for partially correct answers
                        correct_count = len(set(submitted_value).intersection(set(correct_answer)))
                        total_count = len(set(correct_answer))
                        correctness_score = correct_count / total_count if total_count > 0 else 0.0
                        print(f"Partial credit: {correct_count}/{total_count} = {correctness_score}")
                else:
                    # Single selection
                    print(f"Single selection: comparing '{str(submitted_value)}' with '{str(correct_answer)}'")
                    if str(submitted_value) == str(correct_answer):
                        is_correct = True
                        correctness_score = 1.0

                print(f"Is correct: {is_correct}, Score: {correctness_score}")

                mcq_results.append({
                    "question_id": question_id,
                    "correctness_score": correctness_score,
                    "is_correct": is_correct
                })

            elif question_type == "OPEN_ENDED":
                # For open-ended questions, we would need more sophisticated analysis
                # Here we just use placeholder values
                open_ended_results.append({
                    "question_id": question_id,
                    "relevance_score": 0.7,  # Placeholder
                    "clarity_score": 0.7,    # Placeholder
                    "overall_score": 0.7     # Placeholder
                })

        # Calculate overall score
        coding_score = sum(result["overall_score"] for result in coding_results) / len(coding_results) if coding_results else 0.0
        mcq_score = sum(result["correctness_score"] for result in mcq_results) / len(mcq_results) if mcq_results else 0.0
        open_ended_score = sum(result["overall_score"] for result in open_ended_results) / len(open_ended_results) if open_ended_results else 0.0

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

        print("Solution analyzed successfully.")
        return analysis

    except Exception as e:
        print(f"Error analyzing solution: {str(e)}")
        sys.exit(1)


def store_analysis(analysis):
    """Store analysis in the database.

    Args:
        analysis: Analysis data

    Returns:
        Analysis ID
    """
    try:
        repo = AnalysisRepository()
        analysis_id = repo.create_analysis(SolutionAnalysis(**analysis))
        print(f"Analysis stored with ID: {analysis_id}")
        return analysis_id
    except Exception as e:
        print(f"Error storing analysis: {str(e)}")
        sys.exit(1)


def rank_candidates(test_id):
    """Rank candidates based on their assessment results.

    Args:
        test_id: Test ID

    Returns:
        Ranked candidates
    """
    try:
        ranking_service = RankingService()
        ranked_candidates = ranking_service.rank_candidates(test_id)
        print(f"Ranked {len(ranked_candidates)} candidates.")
        return ranked_candidates
    except Exception as e:
        print(f"Error ranking candidates: {str(e)}")
        sys.exit(1)


def generate_report(analysis_id, test_id, ranked_candidates):
    """Generate reports for the analysis.

    Args:
        analysis_id: Analysis ID
        test_id: Test ID
        ranked_candidates: Ranked candidates

    Returns:
        Individual and comparative reports
    """
    try:
        report_generator = ReportGenerator()

        # Generate individual report
        individual_report = report_generator.generate_individual_report(analysis_id)
        print(f"Generated individual report for analysis ID: {analysis_id}")

        # Generate comparative report
        comparative_report = report_generator.generate_comparative_report(test_id, ranked_candidates)
        print(f"Generated comparative report for test ID: {test_id}")

        return individual_report, comparative_report
    except Exception as e:
        print(f"Error generating reports: {str(e)}")
        sys.exit(1)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Assessment Analysis Server")
    parser.add_argument("--assessment", help="Path to assessment JSON file")
    parser.add_argument("--solution", help="Path to solution JSON file")
    args = parser.parse_args()

    # Set up MongoDB
    db = setup_mongodb()

    # Load assessment and solution
    if args.assessment and args.solution:
        assessment = load_assessment(args.assessment)
        solution = load_solution(args.solution)

        # Store assessment and solution
        assessment_id = store_assessment(assessment)
        solution_id = store_solution(solution)

        # Transform solution
        transformed_data = transform_solution(solution, assessment)

        # Analyze solution
        analysis = analyze_solution(transformed_data)

        # Store analysis
        analysis_id = store_analysis(analysis)

        # Rank candidates
        ranked_candidates = rank_candidates(assessment.test_id)

        # Generate reports
        individual_report, comparative_report = generate_report(analysis_id, assessment.test_id, ranked_candidates)

        # Print reports
        print("\n=== Individual Report ===")
        print(json.dumps(individual_report, indent=2))

        print("\n=== Comparative Report ===")
        print(json.dumps(comparative_report, indent=2))
    else:
        print("Please provide both assessment and solution files.")
        sys.exit(1)


if __name__ == "__main__":
    main()
