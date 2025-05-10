"""
Assessment data models.
"""
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel, Field


class TestCase(BaseModel):
    """Test case model for coding questions."""

    input: str
    expected_output: str = Field(..., alias="expectedOutput")
    is_hidden: bool = Field(False, alias="isHidden")
    weight: float = 1.0


class EvaluationCriteria(BaseModel):
    """Evaluation criteria for coding questions."""

    test_cases: List[TestCase] = Field(..., alias="testCases")
    time_complexity: Optional[str] = Field(None, alias="timeComplexity")
    space_complexity: Optional[str] = Field(None, alias="spaceComplexity")
    constraints: List[str] = []


class GradingRules(BaseModel):
    """Grading rules for coding questions."""

    test_case_weight: float = Field(0.7, alias="testCaseWeight")
    code_quality_weight: float = Field(0.2, alias="codeQualityWeight")
    efficiency_weight: float = Field(0.1, alias="efficiencyWeight")
    partial_credit: bool = Field(True, alias="partialCredit")


class QuestionMetadata(BaseModel):
    """Metadata for questions."""

    difficulty: str
    tags: List[str] = []
    order: int
    estimated_duration: Optional[int] = None


class Choice(BaseModel):
    """Choice model for MCQ questions."""

    id: str
    text: str


class Options(BaseModel):
    """Options for MCQ questions."""

    choices: List[Choice]


class CorrectAnswer(BaseModel):
    """Correct answer model."""

    value: Optional[str] = None
    values: Optional[List[str]] = None


class Question(BaseModel):
    """Base question model."""

    type: str
    text: str
    options: Optional[Options] = None
    correct_answer: Optional[CorrectAnswer] = Field(None, alias="correctAnswer")
    difficulty: str
    order: int


class CodingQuestion(BaseModel):
    """Coding question model."""

    type: str = "CODING"
    text: str
    language: str
    starter_code: str = Field(..., alias="starterCode")
    solution_code: str = Field(..., alias="solutionCode")
    evaluation_criteria: EvaluationCriteria = Field(..., alias="evaluationCriteria")
    grading_rules: GradingRules = Field(..., alias="gradingRules")
    metadata: QuestionMetadata


class Assessment(BaseModel):
    """Assessment model."""

    test_id: str = Field(..., alias="testId")
    questions: List[Question]
    coding_questions: List[CodingQuestion] = Field(..., alias="codingQuestions")
