"""
Analyzer for code correctness.
"""
import re
from typing import Dict, Any, List
import subprocess
import tempfile
import os

from app.analyzers.base_analyzer import BaseAnalyzer
from app.models.analysis import TestCaseResult


class CorrectnessAnalyzer(BaseAnalyzer):
    """Analyzer for code correctness."""

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
            return {
                "correctness_score": 0.0,
                "test_case_results": []
            }

        # Run test cases based on language
        if language == "python":
            test_results = self._run_python_tests(code, test_cases)
        elif language == "javascript":
            test_results = self._run_javascript_tests(code, test_cases)
        elif language == "java":
            test_results = self._run_java_tests(code, test_cases)
        else:
            # Default to Python if language not supported
            test_results = self._run_python_tests(code, test_cases)

        # Calculate correctness score
        total_weight = sum(tc.get("weight", 1.0) for tc in test_cases)
        weighted_score = sum(
            tc.get("weight", 1.0) for tc, result in zip(test_cases, test_results) if result.passed
        )

        correctness_score = weighted_score / total_weight if total_weight > 0 else 0.0

        return {
            "correctness_score": correctness_score,
            "test_case_results": [result.model_dump() for result in test_results]
        }

    def _run_python_tests(self, code: str, test_cases: List[Dict]) -> List[TestCaseResult]:
        """Run Python test cases.

        Args:
            code: Python code to test
            test_cases: List of test cases

        Returns:
            List of test case results
        """
        results = []

        # Create a temporary file for the code
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
            temp_file_path = temp_file.name
            temp_file.write(code.encode())

        try:
            for i, test_case in enumerate(test_cases):
                test_id = f"test_{i}"
                input_value = test_case.get("input", "").strip('"')
                expected_output = test_case.get("expected_output", "").strip('"')

                # Create a test script
                test_script = f"""
import sys
import time
import traceback
import re
from memory_profiler import memory_usage
sys.path.append('{os.path.dirname(temp_file_path)}')
from {os.path.basename(temp_file_path)[:-3]} import *

try:
    # For the reverse_string example
    if 'reverse_string' in globals():
        # Clean the input value (remove quotes)
        input_value = "{input_value}".strip('"')

        start_time = time.time()
        result = reverse_string(input_value)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to ms

        print(f"RESULT: {{result}}")
        print(f"EXECUTION_TIME: {{execution_time}}")

        # Measure memory usage
        try:
            mem_usage = memory_usage((reverse_string, (input_value,)), max_usage=True)
            print(f"MEMORY_USAGE: {{mem_usage}}")
        except Exception as mem_err:
            print(f"MEMORY_USAGE: 0.0")
    else:
        print("ERROR: Function not found")
except Exception as e:
    print(f"ERROR: {{str(e)}}")
    print(traceback.format_exc())
"""

                # Write the test script to a temporary file
                with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as test_file:
                    test_file_path = test_file.name
                    test_file.write(test_script.encode())

                # Run the test
                try:
                    process = subprocess.run(
                        ["python", test_file_path],
                        capture_output=True,
                        text=True,
                        timeout=5  # 5 second timeout
                    )

                    output = process.stdout
                    error = process.stderr

                    # Parse the output
                    result_match = re.search(r"RESULT: (.*)", output)
                    time_match = re.search(r"EXECUTION_TIME: ([\d.]+)", output)
                    memory_match = re.search(r"MEMORY_USAGE: ([\d.]+)", output)
                    error_match = re.search(r"ERROR: (.*)", output)

                    if result_match:
                        actual_output = result_match.group(1)
                        execution_time = float(time_match.group(1)) if time_match else 0.0
                        memory_usage = float(memory_match.group(1)) if memory_match else None
                        error_message = error_match.group(1) if error_match else None

                        # Check if the output matches the expected output
                        # Remove any quotes from both outputs for comparison
                        actual_clean = actual_output.strip().strip('"\'')
                        expected_clean = expected_output.strip().strip('"\'')
                        passed = actual_clean == expected_clean

                        result = TestCaseResult(
                            test_case_id=test_id,
                            passed=passed,
                            actual_output=actual_output,
                            expected_output=expected_output,
                            execution_time=execution_time,
                            memory_usage=memory_usage,
                            error_message=error_message
                        )
                    else:
                        result = TestCaseResult(
                            test_case_id=test_id,
                            passed=False,
                            actual_output="",
                            expected_output=expected_output,
                            execution_time=0.0,
                            error_message=error or "Failed to execute test"
                        )
                except subprocess.TimeoutExpired:
                    result = TestCaseResult(
                        test_case_id=test_id,
                        passed=False,
                        actual_output="",
                        expected_output=expected_output,
                        execution_time=5000.0,  # 5 seconds in ms
                        error_message="Execution timed out"
                    )

                results.append(result)

                # Clean up the test file
                os.unlink(test_file_path)
        finally:
            # Clean up the code file
            os.unlink(temp_file_path)

        return results

    def _run_javascript_tests(self, code: str, test_cases: List[Dict]) -> List[TestCaseResult]:
        """Run JavaScript test cases.

        Args:
            code: JavaScript code to test
            test_cases: List of test cases

        Returns:
            List of test case results
        """
        # Similar implementation to Python but for JavaScript
        # This is a placeholder - would need Node.js installed
        return [
            TestCaseResult(
                test_case_id=f"test_{i}",
                passed=False,
                actual_output="",
                expected_output=tc.get("expected_output", ""),
                execution_time=0.0,
                error_message="JavaScript testing not implemented"
            )
            for i, tc in enumerate(test_cases)
        ]

    def _run_java_tests(self, code: str, test_cases: List[Dict]) -> List[TestCaseResult]:
        """Run Java test cases.

        Args:
            code: Java code to test
            test_cases: List of test cases

        Returns:
            List of test case results
        """
        # Similar implementation to Python but for Java
        # This is a placeholder - would need JDK installed
        return [
            TestCaseResult(
                test_case_id=f"test_{i}",
                passed=False,
                actual_output="",
                expected_output=tc.get("expected_output", ""),
                execution_time=0.0,
                error_message="Java testing not implemented"
            )
            for i, tc in enumerate(test_cases)
        ]
