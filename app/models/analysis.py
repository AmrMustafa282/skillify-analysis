"""
Analysis data models.
"""
from typing import List, Dict, Optional, Any, Union
from datetime import datetime
from pydantic import BaseModel, Field


class TestCaseResult(BaseModel):
    """Test case execution result."""
    
    test_case_id: str
    passed: bool
    actual_output: str
    expected_output: str
    execution_time: float  # in milliseconds
    memory_usage: Optional[float] = None  # in KB
    error_message: Optional[str] = None


class CodeQualityMetrics(BaseModel):
    """Code quality metrics."""
    
    cyclomatic_complexity: float
    maintainability_index: float
    halstead_volume: Optional[float] = None
    comment_ratio: float
    function_count: int
    line_count: int


class AIDetectionResult(BaseModel):
    """AI detection result."""
    
    ai_generated_probability: float
    detection_method: str
    flagged_patterns: List[str] = []


class StyleAnalysisResult(BaseModel):
    """Code style analysis result."""
    
    style_score: float
    style_issues: List[str] = []
    naming_convention_score: float
    naming_issues: List[str] = []


class PerformanceAnalysisResult(BaseModel):
    """Performance analysis result."""
    
    time_complexity_score: float
    space_complexity_score: float
    efficiency_score: float
    optimization_suggestions: List[str] = []


class CodingQuestionAnalysis(BaseModel):
    """Analysis for a coding question."""
    
    question_id: str
    correctness_score: float  # 0.0 to 1.0
    test_case_results: List[TestCaseResult]
    code_quality: CodeQualityMetrics
    ai_detection: AIDetectionResult
    style_analysis: StyleAnalysisResult
    performance_analysis: PerformanceAnalysisResult
    overall_score: float  # 0.0 to 1.0


class MCQQuestionAnalysis(BaseModel):
    """Analysis for an MCQ question."""
    
    question_id: str
    correctness_score: float  # 0.0 to 1.0
    is_correct: bool


class OpenEndedQuestionAnalysis(BaseModel):
    """Analysis for an open-ended question."""
    
    question_id: str
    relevance_score: float  # 0.0 to 1.0
    clarity_score: float  # 0.0 to 1.0
    overall_score: float  # 0.0 to 1.0


class SolutionAnalysis(BaseModel):
    """Complete analysis for a solution."""
    
    analysis_id: str
    solution_id: str
    test_id: str
    candidate_id: str
    coding_analyses: List[CodingQuestionAnalysis]
    mcq_analyses: List[MCQQuestionAnalysis]
    open_ended_analyses: List[OpenEndedQuestionAnalysis]
    overall_score: float  # 0.0 to 1.0
    analyzed_at: datetime = Field(default_factory=datetime.now)
