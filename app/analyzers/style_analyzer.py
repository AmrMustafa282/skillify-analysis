"""
Analyzer for code style.
"""
import re
import tempfile
import os
import subprocess
from typing import Dict, Any, List, Tuple

from app.analyzers.base_analyzer import BaseAnalyzer
from app.models.analysis import StyleAnalysisResult


class StyleAnalyzer(BaseAnalyzer):
    """Analyzer for code style."""

    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze code style.

        Args:
            data: Data to analyze, including code

        Returns:
            Analysis results with style score and issues
        """
        language = data.get("language", "").lower()
        code = data.get("submitted_code", "")
        
        if not code:
            return {
                "style_analysis": StyleAnalysisResult(
                    style_score=0.0,
                    style_issues=[],
                    naming_convention_score=0.0,
                    naming_issues=[]
                ).model_dump()
            }
        
        # Analyze code style based on language
        if language == "python":
            result = self._analyze_python_style(code)
        elif language == "javascript":
            result = self._analyze_javascript_style(code)
        elif language == "java":
            result = self._analyze_java_style(code)
        else:
            # Default to Python if language not supported
            result = self._analyze_python_style(code)
        
        return {
            "style_analysis": result.model_dump()
        }

    def _analyze_python_style(self, code: str) -> StyleAnalysisResult:
        """Analyze Python code style.

        Args:
            code: Python code to analyze

        Returns:
            Style analysis result
        """
        # Create a temporary file for the code
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
            temp_file_path = temp_file.name
            temp_file.write(code.encode())
        
        try:
            # Use pylint to check code style
            try:
                process = subprocess.run(
                    ["pylint", "--output-format=json", temp_file_path],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                # Parse the output
                import json
                
                output = process.stdout
                
                try:
                    lint_data = json.loads(output)
                    
                    # Extract style issues
                    style_issues = []
                    naming_issues = []
                    
                    for issue in lint_data:
                        message = issue.get("message", "")
                        if "naming" in message.lower() or "name" in message.lower():
                            naming_issues.append(message)
                        else:
                            style_issues.append(message)
                    
                    # Calculate scores
                    total_issues = len(style_issues) + len(naming_issues)
                    line_count = len(code.strip().split("\n"))
                    
                    # Normalize scores (higher is better)
                    style_score = max(0.0, 1.0 - (len(style_issues) / (line_count * 0.5) if line_count > 0 else 0))
                    naming_score = max(0.0, 1.0 - (len(naming_issues) / (line_count * 0.2) if line_count > 0 else 0))
                    
                except (json.JSONDecodeError, IndexError, KeyError):
                    style_issues = ["Failed to parse pylint output"]
                    naming_issues = []
                    style_score = 0.5
                    naming_score = 0.5
            
            except (subprocess.SubprocessError, FileNotFoundError):
                # If pylint fails, use regex-based analysis
                style_issues, naming_issues, style_score, naming_score = self._analyze_python_style_regex(code)
            
            # Create result object
            result = StyleAnalysisResult(
                style_score=style_score,
                style_issues=style_issues,
                naming_convention_score=naming_score,
                naming_issues=naming_issues
            )
            
        finally:
            # Clean up the code file
            os.unlink(temp_file_path)
        
        return result

    def _analyze_python_style_regex(self, code: str) -> Tuple[List[str], List[str], float, float]:
        """Analyze Python code style using regex patterns.

        Args:
            code: Python code to analyze

        Returns:
            Tuple of (style_issues, naming_issues, style_score, naming_score)
        """
        style_issues = []
        naming_issues = []
        
        # Check line length
        lines = code.strip().split("\n")
        for i, line in enumerate(lines):
            if len(line) > 100:
                style_issues.append(f"Line {i+1} is too long ({len(line)} > 100 characters)")
        
        # Check indentation
        indent_pattern = r"^( +)[^ ]"
        indents = [len(match.group(1)) for line in lines if (match := re.match(indent_pattern, line))]
        if indents and (min(indents) % 4 != 0 or max(indents) % 4 != 0):
            style_issues.append("Inconsistent indentation (not using 4 spaces)")
        
        # Check variable naming
        camel_case_vars = re.findall(r"\b[a-z]+[A-Z][a-zA-Z]*\b", code)
        if camel_case_vars:
            naming_issues.append(f"Found {len(camel_case_vars)} camelCase variable names (use snake_case)")
        
        # Check function naming
        non_snake_funcs = re.findall(r"def\s+([A-Z][a-zA-Z]*|[a-z]+[A-Z][a-zA-Z]*)\s*\(", code)
        if non_snake_funcs:
            naming_issues.append(f"Found {len(non_snake_funcs)} non-snake_case function names")
        
        # Check class naming
        non_camel_classes = re.findall(r"class\s+([a-z][a-zA-Z]*_|[A-Z][a-zA-Z]*_|_[a-zA-Z]+)\s*[:\(]", code)
        if non_camel_classes:
            naming_issues.append(f"Found {len(non_camel_classes)} non-CamelCase class names")
        
        # Calculate scores
        line_count = len(lines)
        style_score = max(0.0, 1.0 - (len(style_issues) / (line_count * 0.5) if line_count > 0 else 0))
        naming_score = max(0.0, 1.0 - (len(naming_issues) / (line_count * 0.2) if line_count > 0 else 0))
        
        return style_issues, naming_issues, style_score, naming_score

    def _analyze_javascript_style(self, code: str) -> StyleAnalysisResult:
        """Analyze JavaScript code style.

        Args:
            code: JavaScript code to analyze

        Returns:
            Style analysis result
        """
        style_issues = []
        naming_issues = []
        
        # Check line length
        lines = code.strip().split("\n")
        for i, line in enumerate(lines):
            if len(line) > 100:
                style_issues.append(f"Line {i+1} is too long ({len(line)} > 100 characters)")
        
        # Check variable naming
        snake_case_vars = re.findall(r"\b(let|const|var)\s+([a-z]+_[a-z_]+)\b", code)
        if snake_case_vars:
            naming_issues.append(f"Found {len(snake_case_vars)} snake_case variable names (use camelCase)")
        
        # Check function naming
        non_camel_funcs = re.findall(r"function\s+([A-Z][a-zA-Z]*|[a-z]+_[a-z_]+)\s*\(", code)
        if non_camel_funcs:
            naming_issues.append(f"Found {len(non_camel_funcs)} non-camelCase function names")
        
        # Check class naming
        non_pascal_classes = re.findall(r"class\s+([a-z][a-zA-Z]*|[a-zA-Z]*_[a-zA-Z_]*)\s*[{\(]", code)
        if non_pascal_classes:
            naming_issues.append(f"Found {len(non_pascal_classes)} non-PascalCase class names")
        
        # Calculate scores
        line_count = len(lines)
        style_score = max(0.0, 1.0 - (len(style_issues) / (line_count * 0.5) if line_count > 0 else 0))
        naming_score = max(0.0, 1.0 - (len(naming_issues) / (line_count * 0.2) if line_count > 0 else 0))
        
        return StyleAnalysisResult(
            style_score=style_score,
            style_issues=style_issues,
            naming_convention_score=naming_score,
            naming_issues=naming_issues
        )

    def _analyze_java_style(self, code: str) -> StyleAnalysisResult:
        """Analyze Java code style.

        Args:
            code: Java code to analyze

        Returns:
            Style analysis result
        """
        style_issues = []
        naming_issues = []
        
        # Check line length
        lines = code.strip().split("\n")
        for i, line in enumerate(lines):
            if len(line) > 100:
                style_issues.append(f"Line {i+1} is too long ({len(line)} > 100 characters)")
        
        # Check variable naming
        non_camel_vars = re.findall(r"\b(int|String|boolean|double|float|long|char)\s+([A-Z][a-zA-Z]*|[a-z]+_[a-z_]+)\b", code)
        if non_camel_vars:
            naming_issues.append(f"Found {len(non_camel_vars)} non-camelCase variable names")
        
        # Check method naming
        non_camel_methods = re.findall(r"(public|private|protected)\s+[a-zA-Z<>[\]]+\s+([A-Z][a-zA-Z]*|[a-z]+_[a-z_]+)\s*\(", code)
        if non_camel_methods:
            naming_issues.append(f"Found {len(non_camel_methods)} non-camelCase method names")
        
        # Check class naming
        non_pascal_classes = re.findall(r"class\s+([a-z][a-zA-Z]*|[a-zA-Z]*_[a-zA-Z_]*)\s*[{\(]", code)
        if non_pascal_classes:
            naming_issues.append(f"Found {len(non_pascal_classes)} non-PascalCase class names")
        
        # Calculate scores
        line_count = len(lines)
        style_score = max(0.0, 1.0 - (len(style_issues) / (line_count * 0.5) if line_count > 0 else 0))
        naming_score = max(0.0, 1.0 - (len(naming_issues) / (line_count * 0.2) if line_count > 0 else 0))
        
        return StyleAnalysisResult(
            style_score=style_score,
            style_issues=style_issues,
            naming_convention_score=naming_score,
            naming_issues=naming_issues
        )
