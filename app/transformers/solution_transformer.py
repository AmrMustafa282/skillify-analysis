"""
Transformers for solution data.
"""
from typing import Dict, List, Any, Optional
import json
from datetime import datetime

from app.models.assessment import Assessment, CodingQuestion, Question
from app.models.solution import Solution, QuestionAnswer, CodingAnswer


class SolutionTransformer:
    """Transformer for solution data."""

    @staticmethod
    def transform_raw_solution(raw_solution: Dict, assessment: Assessment) -> Solution:
        """Transform raw solution data into a Solution model.

        Args:
            raw_solution: Raw solution data
            assessment: Assessment data

        Returns:
            Transformed Solution
        """
        # Extract basic solution info
        solution_id = raw_solution.get("solution_id", "")
        test_id = raw_solution.get("test_id", "")
        candidate_id = raw_solution.get("candidate_id", "")

        # Parse timestamps
        started_at = datetime.fromisoformat(raw_solution.get("started_at", ""))
        completed_at = datetime.fromisoformat(raw_solution.get("completed_at", ""))

        # Calculate time taken
        time_taken = (completed_at - started_at).total_seconds()

        # Process regular question answers
        answers = []
        for answer_data in raw_solution.get("answers", []):
            answer = QuestionAnswer(
                question_id=answer_data.get("question_id", ""),
                answer_type=answer_data.get("type", ""),
                value=answer_data.get("value", None),
                values=answer_data.get("values", None),
                submitted_at=datetime.fromisoformat(answer_data.get("submitted_at", ""))
            )
            answers.append(answer)

        # Process coding question answers
        coding_answers = []
        for coding_answer_data in raw_solution.get("coding_answers", []):
            coding_answer = CodingAnswer(
                question_id=coding_answer_data.get("question_id", ""),
                code=coding_answer_data.get("code", ""),
                language=coding_answer_data.get("language", ""),
                execution_time=coding_answer_data.get("execution_time", None),
                memory_usage=coding_answer_data.get("memory_usage", None),
                submitted_at=datetime.fromisoformat(coding_answer_data.get("submitted_at", ""))
            )
            coding_answers.append(coding_answer)

        # Create and return the Solution model
        return Solution(
            solution_id=solution_id,
            test_id=test_id,
            candidate_id=candidate_id,
            answers=answers,
            coding_answers=coding_answers,
            started_at=started_at,
            completed_at=completed_at,
            time_taken=time_taken
        )

    @staticmethod
    def transform_to_analyzable_format(solution: Solution, assessment: Assessment) -> Dict:
        """Transform a solution into a format suitable for analysis.

        Args:
            solution: Solution data
            assessment: Assessment data

        Returns:
            Transformed data for analysis
        """
        # Create a mapping of question IDs to questions for easy lookup
        question_map = {}
        for question in assessment.questions:
            question_map[str(question.order)] = question

        coding_question_map = {}
        for coding_question in assessment.coding_questions:
            coding_question_map[str(coding_question.metadata.order)] = coding_question

        # Transform regular answers
        transformed_answers = []
        for answer in solution.answers:
            question_id = answer.question_id
            question = question_map.get(question_id)

            if not question:
                continue

            transformed_answer = {
                "question_id": question_id,
                "question_type": question.type,
                "question_text": question.text,
                "answer_type": answer.answer_type,
                "submitted_value": answer.value if answer.value else answer.values,
                "correct_answer": question.correct_answer.value if question.correct_answer and hasattr(question.correct_answer, 'value') and question.correct_answer.value is not None else
                                 question.correct_answer.values if question.correct_answer and hasattr(question.correct_answer, 'values') and question.correct_answer.values is not None else None,
                "difficulty": question.difficulty,
                "submitted_at": answer.submitted_at.isoformat()
            }
            transformed_answers.append(transformed_answer)

        # Transform coding answers
        transformed_coding_answers = []
        for coding_answer in solution.coding_answers:
            question_id = coding_answer.question_id
            coding_question = coding_question_map.get(question_id)

            if not coding_question:
                continue

            transformed_coding_answer = {
                "question_id": question_id,
                "question_text": coding_question.text,
                "language": coding_answer.language,
                "submitted_code": coding_answer.code,
                "solution_code": coding_question.solution_code,
                "starter_code": coding_question.starter_code,
                "test_cases": [tc.model_dump() for tc in coding_question.evaluation_criteria.test_cases],
                "time_complexity": coding_question.evaluation_criteria.time_complexity,
                "space_complexity": coding_question.evaluation_criteria.space_complexity,
                "constraints": coding_question.evaluation_criteria.constraints,
                "grading_rules": coding_question.grading_rules.model_dump(),
                "difficulty": coding_question.metadata.difficulty,
                "tags": coding_question.metadata.tags,
                "execution_time": coding_answer.execution_time,
                "memory_usage": coding_answer.memory_usage,
                "submitted_at": coding_answer.submitted_at.isoformat()
            }
            transformed_coding_answers.append(transformed_coding_answer)

        # Create the final transformed data
        transformed_data = {
            "solution_id": solution.solution_id,
            "test_id": solution.test_id,
            "candidate_id": solution.candidate_id,
            "answers": transformed_answers,
            "coding_answers": transformed_coding_answers,
            "started_at": solution.started_at.isoformat(),
            "completed_at": solution.completed_at.isoformat(),
            "time_taken": solution.time_taken
        }

        return transformed_data
