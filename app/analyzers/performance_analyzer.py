"""
Analyzer for code performance.
"""
import re
from typing import Dict, Any, List

from app.analyzers.base_analyzer import BaseAnalyzer
from app.models.analysis import PerformanceAnalysisResult


class PerformanceAnalyzer(BaseAnalyzer):
    """Analyzer for code performance."""

    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze code performance.

        Args:
            data: Data to analyze, including code and test results

        Returns:
            Analysis results with performance metrics
        """
        language = data.get("language", "").lower()
        code = data.get("submitted_code", "")
        test_case_results = data.get("test_case_results", [])
        expected_time_complexity = data.get("time_complexity", "O(n)")
        expected_space_complexity = data.get("space_complexity", "O(n)")
        
        if not code:
            return {
                "performance_analysis": PerformanceAnalysisResult(
                    time_complexity_score=0.0,
                    space_complexity_score=0.0,
                    efficiency_score=0.0,
                    optimization_suggestions=[]
                ).model_dump()
            }
        
        # Analyze code performance based on language
        if language == "python":
            result = self._analyze_python_performance(code, test_case_results, expected_time_complexity, expected_space_complexity)
        elif language == "javascript":
            result = self._analyze_javascript_performance(code, test_case_results, expected_time_complexity, expected_space_complexity)
        elif language == "java":
            result = self._analyze_java_performance(code, test_case_results, expected_time_complexity, expected_space_complexity)
        else:
            # Default to Python if language not supported
            result = self._analyze_python_performance(code, test_case_results, expected_time_complexity, expected_space_complexity)
        
        return {
            "performance_analysis": result.model_dump()
        }

    def _analyze_python_performance(self, code: str, test_results: List[Dict], expected_time_complexity: str, expected_space_complexity: str) -> PerformanceAnalysisResult:
        """Analyze Python code performance.

        Args:
            code: Python code to analyze
            test_results: Test case results with execution times
            expected_time_complexity: Expected time complexity
            expected_space_complexity: Expected space complexity

        Returns:
            Performance analysis result
        """
        # Estimate time complexity from code patterns
        estimated_time_complexity = self._estimate_time_complexity(code)
        time_complexity_score = self._compare_complexity(estimated_time_complexity, expected_time_complexity)
        
        # Estimate space complexity from code patterns
        estimated_space_complexity = self._estimate_space_complexity(code)
        space_complexity_score = self._compare_complexity(estimated_space_complexity, expected_space_complexity)
        
        # Analyze execution times from test results
        execution_times = [result.get("execution_time", 0) for result in test_results if result.get("passed", False)]
        avg_execution_time = sum(execution_times) / len(execution_times) if execution_times else 0
        
        # Generate optimization suggestions
        optimization_suggestions = []
        
        # Check for inefficient patterns
        if re.search(r"for\s+\w+\s+in\s+range\(.*\):\s+for\s+\w+\s+in\s+range\(.*\):", code):
            optimization_suggestions.append("Consider optimizing nested loops to reduce time complexity")
        
        if re.search(r"\.append\(.*\).*for\s+\w+\s+in", code) and not re.search(r"\[\w+\s+for\s+\w+\s+in", code):
            optimization_suggestions.append("Consider using list comprehensions instead of append in loops")
        
        if re.search(r"sorted\(.*\).*sorted\(", code):
            optimization_suggestions.append("Multiple sorting operations detected - consider combining or optimizing")
        
        # Calculate overall efficiency score
        efficiency_score = (time_complexity_score + space_complexity_score) / 2
        
        return PerformanceAnalysisResult(
            time_complexity_score=time_complexity_score,
            space_complexity_score=space_complexity_score,
            efficiency_score=efficiency_score,
            optimization_suggestions=optimization_suggestions
        )

    def _analyze_javascript_performance(self, code: str, test_results: List[Dict], expected_time_complexity: str, expected_space_complexity: str) -> PerformanceAnalysisResult:
        """Analyze JavaScript code performance.

        Args:
            code: JavaScript code to analyze
            test_results: Test case results with execution times
            expected_time_complexity: Expected time complexity
            expected_space_complexity: Expected space complexity

        Returns:
            Performance analysis result
        """
        # Estimate time complexity from code patterns
        estimated_time_complexity = self._estimate_time_complexity(code)
        time_complexity_score = self._compare_complexity(estimated_time_complexity, expected_time_complexity)
        
        # Estimate space complexity from code patterns
        estimated_space_complexity = self._estimate_space_complexity(code)
        space_complexity_score = self._compare_complexity(estimated_space_complexity, expected_space_complexity)
        
        # Generate optimization suggestions
        optimization_suggestions = []
        
        # Check for inefficient patterns
        if re.search(r"for\s*\(\s*\w+\s*=.*;\s*\w+\s*<.*;\s*\w+\+\+\s*\)\s*{\s*for\s*\(", code):
            optimization_suggestions.append("Consider optimizing nested loops to reduce time complexity")
        
        if re.search(r"\.push\(.*\).*for\s*\(", code) and not re.search(r"\.map\(", code):
            optimization_suggestions.append("Consider using map/filter/reduce instead of push in loops")
        
        if re.search(r"\.sort\(.*\).*\.sort\(", code):
            optimization_suggestions.append("Multiple sorting operations detected - consider combining or optimizing")
        
        # Calculate overall efficiency score
        efficiency_score = (time_complexity_score + space_complexity_score) / 2
        
        return PerformanceAnalysisResult(
            time_complexity_score=time_complexity_score,
            space_complexity_score=space_complexity_score,
            efficiency_score=efficiency_score,
            optimization_suggestions=optimization_suggestions
        )

    def _analyze_java_performance(self, code: str, test_results: List[Dict], expected_time_complexity: str, expected_space_complexity: str) -> PerformanceAnalysisResult:
        """Analyze Java code performance.

        Args:
            code: Java code to analyze
            test_results: Test case results with execution times
            expected_time_complexity: Expected time complexity
            expected_space_complexity: Expected space complexity

        Returns:
            Performance analysis result
        """
        # Estimate time complexity from code patterns
        estimated_time_complexity = self._estimate_time_complexity(code)
        time_complexity_score = self._compare_complexity(estimated_time_complexity, expected_time_complexity)
        
        # Estimate space complexity from code patterns
        estimated_space_complexity = self._estimate_space_complexity(code)
        space_complexity_score = self._compare_complexity(estimated_space_complexity, expected_space_complexity)
        
        # Generate optimization suggestions
        optimization_suggestions = []
        
        # Check for inefficient patterns
        if re.search(r"for\s*\(\s*\w+\s+\w+\s*=.*;\s*\w+\s*<.*;\s*\w+\+\+\s*\)\s*{\s*for\s*\(", code):
            optimization_suggestions.append("Consider optimizing nested loops to reduce time complexity")
        
        if re.search(r"\.add\(.*\).*for\s*\(", code) and not re.search(r"\.stream\(", code):
            optimization_suggestions.append("Consider using streams instead of add in loops")
        
        if re.search(r"Collections\.sort\(.*\).*Collections\.sort\(", code):
            optimization_suggestions.append("Multiple sorting operations detected - consider combining or optimizing")
        
        # Calculate overall efficiency score
        efficiency_score = (time_complexity_score + space_complexity_score) / 2
        
        return PerformanceAnalysisResult(
            time_complexity_score=time_complexity_score,
            space_complexity_score=space_complexity_score,
            efficiency_score=efficiency_score,
            optimization_suggestions=optimization_suggestions
        )

    def _estimate_time_complexity(self, code: str) -> str:
        """Estimate time complexity from code patterns.

        Args:
            code: Code to analyze

        Returns:
            Estimated time complexity
        """
        # Check for common patterns that indicate different time complexities
        if re.search(r"for\s+\w+\s+in\s+range\(.*\):\s+for\s+\w+\s+in\s+range\(.*\):\s+for\s+\w+\s+in\s+range\(.*\):", code) or \
           re.search(r"for\s*\(\s*\w+\s*=.*;\s*\w+\s*<.*;\s*\w+\+\+\s*\)\s*{\s*for\s*\(\s*\w+\s*=.*;\s*\w+\s*<.*;\s*\w+\+\+\s*\)\s*{\s*for\s*\(", code):
            return "O(n^3)"
        
        if re.search(r"for\s+\w+\s+in\s+range\(.*\):\s+for\s+\w+\s+in\s+range\(.*\):", code) or \
           re.search(r"for\s*\(\s*\w+\s*=.*;\s*\w+\s*<.*;\s*\w+\+\+\s*\)\s*{\s*for\s*\(", code):
            return "O(n^2)"
        
        if re.search(r"while\s+\w+\s*<\s*\w+:", code) and re.search(r"\w+\s*=\s*\w+\s*\*\s*2", code):
            return "O(log n)"
        
        if re.search(r"for\s+\w+\s+in\s+range\(.*\):", code) or \
           re.search(r"for\s*\(\s*\w+\s*=.*;\s*\w+\s*<.*;\s*\w+\+\+\s*\)", code):
            return "O(n)"
        
        return "O(1)"

    def _estimate_space_complexity(self, code: str) -> str:
        """Estimate space complexity from code patterns.

        Args:
            code: Code to analyze

        Returns:
            Estimated space complexity
        """
        # Check for common patterns that indicate different space complexities
        if re.search(r"\[\s*\[\s*\w+\s*for\s+\w+\s+in\s+range\(.*\)\s*\]\s*for\s+\w+\s+in\s+range\(.*\)\s*\]", code) or \
           re.search(r"new\s+\w+\[\s*\w+\s*\]\[\s*\w+\s*\]", code):
            return "O(n^2)"
        
        if re.search(r"\[\s*\w+\s*for\s+\w+\s+in\s+range\(.*\)\s*\]", code) or \
           re.search(r"new\s+\w+\[\s*\w+\s*\]", code) or \
           re.search(r"new\s+ArrayList<>\(\)", code):
            return "O(n)"
        
        return "O(1)"

    def _compare_complexity(self, estimated: str, expected: str) -> float:
        """Compare estimated complexity with expected complexity.

        Args:
            estimated: Estimated complexity
            expected: Expected complexity

        Returns:
            Score between 0.0 and 1.0
        """
        # Map complexities to numeric values for comparison
        complexity_map = {
            "O(1)": 1,
            "O(log n)": 2,
            "O(n)": 3,
            "O(n log n)": 4,
            "O(n^2)": 5,
            "O(n^3)": 6,
            "O(2^n)": 7,
            "O(n!)": 8
        }
        
        estimated_value = complexity_map.get(estimated, 3)  # Default to O(n)
        expected_value = complexity_map.get(expected, 3)  # Default to O(n)
        
        # Calculate score based on difference
        if estimated_value <= expected_value:
            # If estimated is better or equal to expected, give full score
            return 1.0
        else:
            # If estimated is worse than expected, reduce score based on difference
            difference = estimated_value - expected_value
            return max(0.0, 1.0 - (difference * 0.25))
