"""
Analyzer for code performance.
"""
import re
from typing import Dict, Any, List

from server.services.analyzers.base_analyzer import BaseAnalyzer


class PerformanceAnalysisResult:
    """Performance analysis result."""

    def __init__(self, efficiency_score: float, time_complexity_score: float,
                 space_complexity_score: float, time_complexity: str = "Unknown",
                 space_complexity: str = "Unknown", optimization_suggestions: List[str] = None):
        """Initialize a performance analysis result.

        Args:
            efficiency_score: Overall efficiency score
            time_complexity_score: Score for time complexity
            space_complexity_score: Score for space complexity
            time_complexity: Estimated time complexity
            space_complexity: Estimated space complexity
            optimization_suggestions: List of optimization suggestions
        """
        self.efficiency_score = efficiency_score
        self.time_complexity_score = time_complexity_score
        self.space_complexity_score = space_complexity_score
        self.time_complexity = time_complexity
        self.space_complexity = space_complexity
        self.optimization_suggestions = optimization_suggestions or []

    def model_dump(self) -> Dict[str, Any]:
        """Convert the result to a dictionary.

        Returns:
            Dictionary representation of the result
        """
        return {
            "efficiency_score": self.efficiency_score,
            "time_complexity_score": self.time_complexity_score,
            "space_complexity_score": self.space_complexity_score,
            "time_complexity": self.time_complexity,
            "space_complexity": self.space_complexity,
            "optimization_suggestions": self.optimization_suggestions
        }


class PerformanceAnalyzer(BaseAnalyzer):
    """Analyzer for code performance."""

    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze code performance.

        Args:
            data: Data to analyze, including code and execution metrics

        Returns:
            Analysis results with performance metrics
        """
        language = data.get("language", "").lower()
        code = data.get("submitted_code", "")
        execution_time = data.get("execution_time", 0.0)
        memory_usage = data.get("memory_usage", 0.0)

        if not code:
            return {
                "performance_analysis": PerformanceAnalysisResult(
                    efficiency_score=0.0,
                    time_complexity_score=0.0,
                    space_complexity_score=0.0
                ).model_dump()
            }

        # Analyze performance based on language
        if language == "python":
            result = self._analyze_python_performance(code, execution_time, memory_usage)
        elif language == "javascript":
            result = self._analyze_javascript_performance(code, execution_time, memory_usage)
        elif language == "java":
            result = self._analyze_java_performance(code, execution_time, memory_usage)
        else:
            # Default to Python if language not supported
            result = self._analyze_python_performance(code, execution_time, memory_usage)

        return {
            "performance_analysis": result.model_dump()
        }

    def _analyze_python_performance(self, code: str, execution_time: float, memory_usage: float) -> PerformanceAnalysisResult:
        """Analyze Python code performance.

        Args:
            code: Python code to analyze
            execution_time: Execution time in milliseconds
            memory_usage: Memory usage in KB

        Returns:
            Performance analysis result
        """
        # Estimate time complexity
        time_complexity, time_complexity_score = self._estimate_time_complexity(code)

        # Estimate space complexity
        space_complexity, space_complexity_score = self._estimate_space_complexity(code)

        # Find optimization opportunities
        optimization_suggestions = self._find_python_optimizations(code)

        # Calculate overall efficiency score
        # We weight time complexity more heavily than space complexity
        efficiency_score = 0.7 * time_complexity_score + 0.3 * space_complexity_score

        # Adjust score based on optimization opportunities
        if optimization_suggestions:
            # Each suggestion reduces the score by a small amount
            efficiency_score = max(0.0, efficiency_score - len(optimization_suggestions) * 0.05)

        return PerformanceAnalysisResult(
            efficiency_score=efficiency_score,
            time_complexity_score=time_complexity_score,
            space_complexity_score=space_complexity_score,
            time_complexity=time_complexity,
            space_complexity=space_complexity,
            optimization_suggestions=optimization_suggestions
        )

    def _estimate_time_complexity(self, code: str) -> tuple:
        """Estimate time complexity of code.

        Args:
            code: Code to analyze

        Returns:
            Tuple of (complexity string, complexity score)
        """
        # Look for nested loops
        nested_loops = len(re.findall(r"for.*?for", code, re.DOTALL))

        # Look for single loops
        single_loops = len(re.findall(r"for\s+\w+\s+in", code)) - nested_loops

        # Look for recursive calls
        function_names = re.findall(r"def\s+(\w+)", code)
        recursive_calls = 0

        for name in function_names:
            if re.search(rf"{name}\s*\(", code):
                recursive_calls += 1

        # Determine complexity based on patterns
        if nested_loops > 1:
            complexity = "O(n^3)" if nested_loops > 2 else "O(n^2)"
            score = 0.3 if nested_loops > 2 else 0.5
        elif nested_loops == 1:
            complexity = "O(n^2)"
            score = 0.5
        elif single_loops > 0:
            complexity = "O(n)"
            score = 0.8
        elif recursive_calls > 0:
            complexity = "O(2^n)" if "fibonacci" in code.lower() else "O(log n)"
            score = 0.4 if "fibonacci" in code.lower() else 0.9
        else:
            complexity = "O(1)"
            score = 1.0

        return complexity, score

    def _estimate_space_complexity(self, code: str) -> tuple:
        """Estimate space complexity of code.

        Args:
            code: Code to analyze

        Returns:
            Tuple of (complexity string, complexity score)
        """
        # Look for data structures that grow with input
        lists = len(re.findall(r"\[\s*\]|\[\s*\w+\s*\]|list\(", code))
        dicts = len(re.findall(r"\{\s*\}|\{\s*\w+\s*:\s*\w+\s*\}|dict\(", code))
        sets = len(re.findall(r"set\(", code))

        # Look for recursive calls
        function_names = re.findall(r"def\s+(\w+)", code)
        recursive_calls = 0

        for name in function_names:
            if re.search(rf"{name}\s*\(", code):
                recursive_calls += 1

        # Determine complexity based on patterns
        if recursive_calls > 0:
            complexity = "O(n)"
            score = 0.7
        elif lists + dicts + sets > 3:
            complexity = "O(n)"
            score = 0.8
        elif lists + dicts + sets > 0:
            complexity = "O(n)"
            score = 0.9
        else:
            complexity = "O(1)"
            score = 1.0

        return complexity, score

    def _find_python_optimizations(self, code: str) -> List[str]:
        """Find optimization opportunities in Python code.

        Args:
            code: Python code to analyze

        Returns:
            List of optimization suggestions
        """
        suggestions = []

        # Check for inefficient list operations
        if re.search(r"\+\s*=\s*\[", code):
            suggestions.append("Use list.extend() instead of += for concatenating lists")

        # Check for inefficient string concatenation
        if re.search(r"for.*?\+\s*=\s*[\'\"]", code, re.DOTALL):
            suggestions.append("Use ''.join() instead of += for string concatenation in loops")

        # Check for inefficient list comprehensions
        if re.search(r"for\s+\w+\s+in\s+\w+\s*:\s*\w+\.append", code):
            suggestions.append("Consider using list comprehensions instead of append() in loops")

        # Check for inefficient dictionary operations
        if re.search(r"if\s+\w+\s+in\s+\w+\s*:\s*\w+\[\w+\]", code):
            suggestions.append("Consider using dict.get() with a default value instead of checking if key exists")

        # Check for inefficient sorting
        if re.search(r"sorted\(.*?key\s*=\s*lambda", code):
            suggestions.append("Consider using operator.itemgetter() instead of lambda for sorting")

        return suggestions

    def _analyze_javascript_performance(self, code: str, execution_time: float, memory_usage: float) -> PerformanceAnalysisResult:
        """Analyze JavaScript code performance.

        Args:
            code: JavaScript code to analyze
            execution_time: Execution time in milliseconds
            memory_usage: Memory usage in KB

        Returns:
            Performance analysis result
        """
        # This is a simplified implementation
        # In a real system, you'd use more sophisticated analysis

        # Estimate time complexity
        nested_loops = len(re.findall(r"for.*?for", code, re.DOTALL))
        single_loops = len(re.findall(r"for\s*\(", code)) - nested_loops

        if nested_loops > 1:
            time_complexity = "O(n^2)"
            time_score = 0.5
        elif nested_loops == 1 or single_loops > 0:
            time_complexity = "O(n)"
            time_score = 0.8
        else:
            time_complexity = "O(1)"
            time_score = 1.0

        # Estimate space complexity
        arrays = len(re.findall(r"\[\s*\]|\[\s*\w+\s*\]|Array\(", code))
        objects = len(re.findall(r"\{\s*\}|\{\s*\w+\s*:\s*\w+\s*\}|Object\(", code))

        if arrays + objects > 3:
            space_complexity = "O(n)"
            space_score = 0.8
        elif arrays + objects > 0:
            space_complexity = "O(n)"
            space_score = 0.9
        else:
            space_complexity = "O(1)"
            space_score = 1.0

        # Calculate overall efficiency score
        efficiency_score = 0.7 * time_score + 0.3 * space_score

        # Find optimization opportunities
        optimization_suggestions = []

        if re.search(r"for\s*\(.*?\.push", code, re.DOTALL):
            optimization_suggestions.append("Consider using map() instead of for loop with push()")

        if re.search(r"\.indexOf\s*\(.*?\)\s*!=\s*-1", code):
            optimization_suggestions.append("Consider using includes() instead of indexOf() != -1")

        return PerformanceAnalysisResult(
            efficiency_score=efficiency_score,
            time_complexity_score=time_score,
            space_complexity_score=space_score,
            time_complexity=time_complexity,
            space_complexity=space_complexity,
            optimization_suggestions=optimization_suggestions
        )

    def _analyze_java_performance(self, code: str, execution_time: float, memory_usage: float) -> PerformanceAnalysisResult:
        """Analyze Java code performance.

        Args:
            code: Java code to analyze
            execution_time: Execution time in milliseconds
            memory_usage: Memory usage in KB

        Returns:
            Performance analysis result
        """
        # This is a simplified implementation
        # In a real system, you'd use more sophisticated analysis

        # Estimate time complexity
        nested_loops = len(re.findall(r"for.*?for", code, re.DOTALL))
        single_loops = len(re.findall(r"for\s*\(", code)) - nested_loops

        if nested_loops > 1:
            time_complexity = "O(n^2)"
            time_score = 0.5
        elif nested_loops == 1 or single_loops > 0:
            time_complexity = "O(n)"
            time_score = 0.8
        else:
            time_complexity = "O(1)"
            time_score = 1.0

        # Estimate space complexity
        arrays = len(re.findall(r"new\s+\w+\s*\[", code))
        collections = len(re.findall(r"new\s+(ArrayList|HashMap|HashSet)", code))

        if arrays + collections > 3:
            space_complexity = "O(n)"
            space_score = 0.8
        elif arrays + collections > 0:
            space_complexity = "O(n)"
            space_score = 0.9
        else:
            space_complexity = "O(1)"
            space_score = 1.0

        # Calculate overall efficiency score
        efficiency_score = 0.7 * time_score + 0.3 * space_score

        # Find optimization opportunities
        optimization_suggestions = []

        if re.search(r"for\s*\(.*?\.add", code, re.DOTALL):
            optimization_suggestions.append("Consider using a more efficient collection operation")

        if re.search(r"String.*?\+\s*=", code):
            optimization_suggestions.append("Consider using StringBuilder instead of String concatenation")

        return PerformanceAnalysisResult(
            efficiency_score=efficiency_score,
            time_complexity_score=time_score,
            space_complexity_score=space_score,
            time_complexity=time_complexity,
            space_complexity=space_complexity,
            optimization_suggestions=optimization_suggestions
        )
