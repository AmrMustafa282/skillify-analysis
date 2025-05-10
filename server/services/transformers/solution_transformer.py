"""
Transformer for converting solutions to analyzable format.
"""
import logging
from typing import Dict, Any, List

# Configure logging
logger = logging.getLogger(__name__)


class SolutionTransformer:
    """Transformer for converting solutions to analyzable format."""

    def transform_to_analyzable_format(self, solution: Dict[str, Any], assessment: Dict[str, Any]) -> Dict[str, Any]:
        """Transform a solution to an analyzable format.

        Args:
            solution: Solution document from MongoDB
            assessment: Assessment document from MongoDB

        Returns:
            Transformed solution data
        """
        # Extract basic information
        transformed_data = {
            "solution_id": solution.get("solution_id", ""),
            "test_id": solution.get("test_id", ""),
            "candidate_id": solution.get("candidate_id", ""),
            "started_at": solution.get("started_at", ""),
            "completed_at": solution.get("completed_at", ""),
            "time_taken": solution.get("time_taken", 0),
            "answers": [],
            "coding_answers": []
        }
        
        # Transform MCQ and open-ended answers
        answers = solution.get("answers", [])
        for answer in answers:
            transformed_answer = self._transform_answer(answer, assessment)
            transformed_data["answers"].append(transformed_answer)
        
        # Transform coding answers
        coding_answers = solution.get("coding_answers", [])
        for coding_answer in coding_answers:
            transformed_coding_answer = self._transform_coding_answer(coding_answer, assessment)
            transformed_data["coding_answers"].append(transformed_coding_answer)
        
        return transformed_data

    def _transform_answer(self, answer: Dict[str, Any], assessment: Dict[str, Any]) -> Dict[str, Any]:
        """Transform an answer to an analyzable format.

        Args:
            answer: Answer data
            assessment: Assessment document

        Returns:
            Transformed answer data
        """
        question_id = answer.get("question_id", "")
        answer_type = answer.get("answer_type", "")
        
        # Find the corresponding question in the assessment
        question = self._find_question(question_id, assessment)
        
        transformed_answer = {
            "question_id": question_id,
            "answer_type": answer_type,
            "submitted_at": answer.get("submitted_at", "")
        }
        
        # Handle different answer types
        if answer_type == "MCQ":
            if "value" in answer:
                transformed_answer["submitted_value"] = answer["value"]
                transformed_answer["correct_answer"] = question.get("correctAnswer", {}).get("value", "")
            elif "values" in answer:
                transformed_answer["submitted_value"] = answer["values"]
                transformed_answer["correct_answer"] = question.get("correctAnswer", {}).get("values", [])
        elif answer_type == "OPEN_ENDED":
            transformed_answer["submitted_value"] = answer.get("value", "")
            transformed_answer["expected_answer"] = question.get("expectedAnswer", "")
        
        return transformed_answer

    def _transform_coding_answer(self, coding_answer: Dict[str, Any], assessment: Dict[str, Any]) -> Dict[str, Any]:
        """Transform a coding answer to an analyzable format.

        Args:
            coding_answer: Coding answer data
            assessment: Assessment document

        Returns:
            Transformed coding answer data
        """
        question_id = coding_answer.get("question_id", "")
        
        # Find the corresponding coding question in the assessment
        coding_question = self._find_coding_question(question_id, assessment)
        
        transformed_coding_answer = {
            "question_id": question_id,
            "language": coding_answer.get("language", ""),
            "submitted_code": coding_answer.get("code", ""),
            "execution_time": coding_answer.get("execution_time", 0.0),
            "memory_usage": coding_answer.get("memory_usage", 0.0),
            "submitted_at": coding_answer.get("submitted_at", "")
        }
        
        # Add test cases from the assessment
        if coding_question:
            transformed_coding_answer["starter_code"] = coding_question.get("starterCode", "")
            transformed_coding_answer["solution_code"] = coding_question.get("solutionCode", "")
            transformed_coding_answer["test_cases"] = coding_question.get("testCases", [])
        
        return transformed_coding_answer

    def _find_question(self, question_id: str, assessment: Dict[str, Any]) -> Dict[str, Any]:
        """Find a question in the assessment.

        Args:
            question_id: Question ID
            assessment: Assessment document

        Returns:
            Question data or empty dict if not found
        """
        questions = assessment.get("questions", [])
        
        for question in questions:
            if str(question.get("order", "")) == question_id:
                return question
        
        return {}

    def _find_coding_question(self, question_id: str, assessment: Dict[str, Any]) -> Dict[str, Any]:
        """Find a coding question in the assessment.

        Args:
            question_id: Question ID
            assessment: Assessment document

        Returns:
            Coding question data or empty dict if not found
        """
        coding_questions = assessment.get("codingQuestions", [])
        
        for question in coding_questions:
            if str(question.get("order", "")) == question_id:
                return question
        
        return {}
