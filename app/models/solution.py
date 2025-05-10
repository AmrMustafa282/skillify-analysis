"""
Solution data models.
"""
from typing import List, Dict, Optional, Any, Union
from datetime import datetime
from pydantic import BaseModel, Field


class QuestionAnswer(BaseModel):
    """Base answer model for non-coding questions."""
    
    question_id: str
    answer_type: str  # MCQ, OPEN_ENDED
    value: Optional[str] = None
    values: Optional[List[str]] = None
    submitted_at: datetime = Field(default_factory=datetime.now)


class CodingAnswer(BaseModel):
    """Coding answer model."""
    
    question_id: str
    answer_type: str = "CODING"
    code: str
    language: str
    execution_time: Optional[float] = None
    memory_usage: Optional[float] = None
    submitted_at: datetime = Field(default_factory=datetime.now)


class Solution(BaseModel):
    """Solution model for an assessment."""
    
    solution_id: str
    test_id: str
    candidate_id: str
    answers: List[QuestionAnswer]
    coding_answers: List[CodingAnswer]
    started_at: datetime
    completed_at: datetime
    time_taken: float  # in seconds
