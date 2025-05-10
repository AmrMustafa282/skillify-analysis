"""
Analyzer for code correctness.
"""
import re
import logging
from typing import Dict, Any, List
import subprocess
import tempfile
import os

from server.services.analyzers.base_analyzer import BaseAnalyzer
from server.services.code_execution_service import CodeExecutionService

logger = logging.getLogger(__name__)


class TestCaseResult:
    """Test case execution result."""

    def __init__(self, test_case_id: str, passed: bool, actual_output: str, expected_output: str,
                 execution_time: float, memory_usage: float = None, error_message: str = None):
        """Initialize a test case result.

        Args:
            test_case_id: ID of the test case
            passed: Whether the test passed
            actual_output: Actual output of the test
            expected_output: Expected output of the test
            execution_time: Execution time in milliseconds
            memory_usage: Memory usage in KB
            error_message: Error message if the test failed
        """
        self.test_case_id = test_case_id
        self.passed = passed
        self.actual_output = actual_output
        self.expected_output = expected_output
        self.execution_time = execution_time
        self.memory_usage = memory_usage
        self.error_message = error_message

    def model_dump(self) -> Dict[str, Any]:
        """Convert the test case result to a dictionary.

        Returns:
            Dictionary representation of the test case result
        """
        return {
            "test_case_id": self.test_case_id,
            "passed": self.passed,
            "actual_output": self.actual_output,
            "expected_output": self.expected_output,
            "execution_time": self.execution_time,
            "memory_usage": self.memory_usage,
            "error_message": self.error_message
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TestCaseResult':
        """Create a TestCaseResult from a dictionary.

        Args:
            data: Dictionary representation of a test case result

        Returns:
            TestCaseResult instance
        """
        return cls(
            test_case_id=data.get("test_case_id", ""),
            passed=data.get("passed", False),
            actual_output=data.get("actual_output", ""),
            expected_output=data.get("expected_output", ""),
            execution_time=data.get("execution_time", 0.0),
            memory_usage=data.get("memory_usage"),
            error_message=data.get("error_message")
        )


class CorrectnessAnalyzer(BaseAnalyzer):
    """Analyzer for code correctness."""

    def __init__(self):
        """Initialize the correctness analyzer."""
        super().__init__()
        self.code_execution_service = CodeExecutionService()

    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze code correctness by running test cases.

        Args:
            data: Data to analyze, including code and test cases

        Returns:
            Analysis results with test case results and correctness score
        """
        language = data.get("language", "").lower()
        code = data.get("submitted_code", "")
        test_cases = data.get("test_cases", [])

        if not code or not test_cases:
            logger.warning("No code or test cases provided for correctness analysis")
            return {
                "correctness_score": 0.0,
                "test_case_results": []
            }

        logger.info(f"Running correctness analysis for {language} code with {len(test_cases)} test cases")

        # Prepare test cases with function names if available
        prepared_test_cases = []
        for tc in test_cases:
            prepared_tc = dict(tc)
            # Extract function name from description or code if not provided
            if "function_name" not in prepared_tc:
                # Try to extract from description
                if "description" in prepared_tc:
                    desc = prepared_tc["description"].lower()
                    if "function" in desc:
                        # Extract function name from description
                        match = re.search(r"function\s+(\w+)", desc)
                        if match:
                            prepared_tc["function_name"] = match.group(1)

                # Try to extract from code if still not found
                if "function_name" not in prepared_tc and code:
                    if language == "python":
                        match = re.search(r"def\s+(\w+)\s*\(", code)
                        if match:
                            prepared_tc["function_name"] = match.group(1)
                    elif language == "javascript":
                        match = re.search(r"function\s+(\w+)\s*\(", code)
                        if match:
                            prepared_tc["function_name"] = match.group(1)
                    elif language == "java":
                        # Look for public methods
                        match = re.search(r"public\s+\w+\s+(\w+)\s*\(", code)
                        if match:
                            prepared_tc["function_name"] = match.group(1)

            prepared_test_cases.append(prepared_tc)

        # Execute code using the code execution service
        results = self.code_execution_service.execute_code(
            code=code,
            language=language,
            test_cases=prepared_test_cases,
            timeout=15  # 15 seconds timeout
        )

        # Convert results to TestCaseResult objects
        test_results = [TestCaseResult.from_dict(result) for result in results]

        # Calculate correctness score
        total_weight = sum(tc.get("weight", 1.0) for tc in test_cases)
        weighted_score = sum(
            tc.get("weight", 1.0) for tc, result in zip(test_cases, test_results) if result.passed
        )

        correctness_score = weighted_score / total_weight if total_weight > 0 else 0.0

        logger.info(f"Correctness analysis complete. Score: {correctness_score:.2f}")

        return {
            "correctness_score": correctness_score,
            "test_case_results": [result.model_dump() for result in test_results]
        }


