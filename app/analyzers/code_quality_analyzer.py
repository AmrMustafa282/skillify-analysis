"""
Analyzer for code quality.
"""
import re
import tempfile
import os
import subprocess
from typing import Dict, Any, List

from app.analyzers.base_analyzer import BaseAnalyzer
from app.models.analysis import CodeQualityMetrics


class CodeQualityAnalyzer(BaseAnalyzer):
    """Analyzer for code quality."""

    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze code quality using various metrics.

        Args:
            data: Data to analyze, including code

        Returns:
            Analysis results with code quality metrics
        """
        language = data.get("language", "").lower()
        code = data.get("submitted_code", "")
        
        if not code:
            return {
                "code_quality": CodeQualityMetrics(
                    cyclomatic_complexity=0.0,
                    maintainability_index=0.0,
                    comment_ratio=0.0,
                    function_count=0,
                    line_count=0
                ).model_dump()
            }
        
        # Analyze code quality based on language
        if language == "python":
            metrics = self._analyze_python_code(code)
        elif language == "javascript":
            metrics = self._analyze_javascript_code(code)
        elif language == "java":
            metrics = self._analyze_java_code(code)
        else:
            # Default to Python if language not supported
            metrics = self._analyze_python_code(code)
        
        return {
            "code_quality": metrics.model_dump()
        }

    def _analyze_python_code(self, code: str) -> CodeQualityMetrics:
        """Analyze Python code quality.

        Args:
            code: Python code to analyze

        Returns:
            Code quality metrics
        """
        # Count lines and functions
        line_count = len(code.strip().split("\n"))
        function_count = len(re.findall(r"def\s+\w+\s*\(", code))
        
        # Count comments
        comment_lines = len(re.findall(r"^\s*#.*$", code, re.MULTILINE))
        comment_ratio = comment_lines / line_count if line_count > 0 else 0.0
        
        # Create a temporary file for the code
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
            temp_file_path = temp_file.name
            temp_file.write(code.encode())
        
        try:
            # Use radon to calculate cyclomatic complexity and maintainability index
            try:
                cc_process = subprocess.run(
                    ["radon", "cc", temp_file_path, "--json"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                mi_process = subprocess.run(
                    ["radon", "mi", temp_file_path, "--json"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                # Parse the output
                import json
                
                cc_output = cc_process.stdout
                mi_output = mi_process.stdout
                
                try:
                    cc_data = json.loads(cc_output)
                    mi_data = json.loads(mi_output)
                    
                    # Calculate average cyclomatic complexity
                    cc_values = []
                    for file_data in cc_data.values():
                        for func_data in file_data:
                            cc_values.append(func_data.get("complexity", 0))
                    
                    avg_cc = sum(cc_values) / len(cc_values) if cc_values else 1.0
                    
                    # Get maintainability index
                    mi_value = list(mi_data.values())[0] if mi_data else 100.0
                    
                except (json.JSONDecodeError, IndexError, KeyError):
                    avg_cc = 1.0
                    mi_value = 100.0
            
            except (subprocess.SubprocessError, FileNotFoundError):
                # If radon fails, use default values
                avg_cc = 1.0
                mi_value = 100.0
            
            # Create metrics object
            metrics = CodeQualityMetrics(
                cyclomatic_complexity=avg_cc,
                maintainability_index=mi_value,
                halstead_volume=None,  # Not calculated
                comment_ratio=comment_ratio,
                function_count=function_count,
                line_count=line_count
            )
            
        finally:
            # Clean up the code file
            os.unlink(temp_file_path)
        
        return metrics

    def _analyze_javascript_code(self, code: str) -> CodeQualityMetrics:
        """Analyze JavaScript code quality.

        Args:
            code: JavaScript code to analyze

        Returns:
            Code quality metrics
        """
        # Count lines and functions
        line_count = len(code.strip().split("\n"))
        function_count = len(re.findall(r"function\s+\w+\s*\(", code)) + len(re.findall(r"=>\s*{", code))
        
        # Count comments
        comment_lines = len(re.findall(r"^\s*//.*$", code, re.MULTILINE)) + len(re.findall(r"/\*.*?\*/", code, re.DOTALL))
        comment_ratio = comment_lines / line_count if line_count > 0 else 0.0
        
        # Create metrics object with default values
        metrics = CodeQualityMetrics(
            cyclomatic_complexity=1.0,
            maintainability_index=100.0,
            halstead_volume=None,
            comment_ratio=comment_ratio,
            function_count=function_count,
            line_count=line_count
        )
        
        return metrics

    def _analyze_java_code(self, code: str) -> CodeQualityMetrics:
        """Analyze Java code quality.

        Args:
            code: Java code to analyze

        Returns:
            Code quality metrics
        """
        # Count lines and methods
        line_count = len(code.strip().split("\n"))
        function_count = len(re.findall(r"(public|private|protected)?\s+\w+\s+\w+\s*\(", code))
        
        # Count comments
        comment_lines = len(re.findall(r"^\s*//.*$", code, re.MULTILINE)) + len(re.findall(r"/\*.*?\*/", code, re.DOTALL))
        comment_ratio = comment_lines / line_count if line_count > 0 else 0.0
        
        # Create metrics object with default values
        metrics = CodeQualityMetrics(
            cyclomatic_complexity=1.0,
            maintainability_index=100.0,
            halstead_volume=None,
            comment_ratio=comment_ratio,
            function_count=function_count,
            line_count=line_count
        )
        
        return metrics
