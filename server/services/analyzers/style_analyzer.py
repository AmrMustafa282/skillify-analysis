"""
Analyzer for code style.
"""
import re
import tempfile
import os
import subprocess
from typing import Dict, Any, List

from server.services.analyzers.base_analyzer import BaseAnalyzer


class StyleIssue:
    """Style issue found in code."""

    def __init__(self, issue_type: str, line_number: int, message: str, severity: str = "warning"):
        """Initialize a style issue.

        Args:
            issue_type: Type of issue
            line_number: Line number where the issue was found
            message: Description of the issue
            severity: Severity of the issue (error, warning, info)
        """
        self.issue_type = issue_type
        self.line_number = line_number
        self.message = message
        self.severity = severity

    def model_dump(self) -> Dict[str, Any]:
        """Convert the issue to a dictionary.

        Returns:
            Dictionary representation of the issue
        """
        return {
            "issue_type": self.issue_type,
            "line_number": self.line_number,
            "message": self.message,
            "severity": self.severity
        }


class StyleAnalysisResult:
    """Style analysis result."""

    def __init__(self, style_score: float, naming_convention_score: float, style_issues: List[StyleIssue] = None):
        """Initialize a style analysis result.

        Args:
            style_score: Overall style score
            naming_convention_score: Score for naming conventions
            style_issues: List of style issues found
        """
        self.style_score = style_score
        self.naming_convention_score = naming_convention_score
        self.style_issues = style_issues or []

    def model_dump(self) -> Dict[str, Any]:
        """Convert the result to a dictionary.

        Returns:
            Dictionary representation of the result
        """
        return {
            "style_score": self.style_score,
            "naming_convention_score": self.naming_convention_score,
            "style_issues": [issue.model_dump() for issue in self.style_issues]
        }


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
                    naming_convention_score=0.0,
                    style_issues=[]
                ).model_dump()
            }

        # Analyze style based on language
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

        style_issues = []

        try:
            # Use pylint to check style
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
                    issues_data = json.loads(output)

                    for issue in issues_data:
                        style_issues.append(StyleIssue(
                            issue_type=issue.get("symbol", "unknown"),
                            line_number=issue.get("line", 0),
                            message=issue.get("message", ""),
                            severity=issue.get("type", "warning")
                        ))

                except json.JSONDecodeError:
                    # If JSON parsing fails, try to extract issues using regex
                    for line in process.stdout.split("\n"):
                        if ":" in line:
                            parts = line.split(":")
                            if len(parts) >= 3:
                                try:
                                    line_number = int(parts[1].strip())
                                    message = parts[2].strip()
                                    style_issues.append(StyleIssue(
                                        issue_type="style",
                                        line_number=line_number,
                                        message=message,
                                        severity="warning"
                                    ))
                                except ValueError:
                                    pass

            except (subprocess.SubprocessError, FileNotFoundError):
                # If pylint fails, use a simple regex-based approach
                style_issues = self._check_python_style_with_regex(code)

            # Calculate style score based on issues
            issue_count = len(style_issues)
            line_count = len(code.strip().split("\n"))

            # Calculate style score (1.0 is perfect, 0.0 is worst)
            # We use a formula that decreases the score as the issue density increases
            issue_density = issue_count / line_count if line_count > 0 else 0
            style_score = max(0.0, 1.0 - min(issue_density * 2, 1.0))

            # Calculate naming convention score
            naming_convention_score = self._calculate_python_naming_score(code)

            # Create result object
            result = StyleAnalysisResult(
                style_score=style_score,
                naming_convention_score=naming_convention_score,
                style_issues=style_issues
            )

        finally:
            # Clean up the code file
            os.unlink(temp_file_path)

        return result

    def _check_python_style_with_regex(self, code: str) -> List[StyleIssue]:
        """Check Python code style using regex patterns.

        Args:
            code: Python code to analyze

        Returns:
            List of style issues
        """
        issues = []
        lines = code.split("\n")

        # Check line length
        for i, line in enumerate(lines):
            if len(line) > 100:
                issues.append(StyleIssue(
                    issue_type="line-too-long",
                    line_number=i + 1,
                    message=f"Line too long ({len(line)} > 100 characters)",
                    severity="warning"
                ))

        # Check indentation
        indent_pattern = r"^(\s*)\S"
        prev_indent = 0

        for i, line in enumerate(lines):
            if not line.strip():
                continue

            match = re.match(indent_pattern, line)
            if match:
                indent = len(match.group(1))

                # Check if indentation is a multiple of 4
                if indent % 4 != 0:
                    issues.append(StyleIssue(
                        issue_type="bad-indentation",
                        line_number=i + 1,
                        message=f"Indentation is not a multiple of 4",
                        severity="warning"
                    ))

                # Check for sudden large indentation changes
                if indent > prev_indent + 4 and not lines[i-1].strip().endswith(":"):
                    issues.append(StyleIssue(
                        issue_type="unexpected-indentation",
                        line_number=i + 1,
                        message=f"Unexpected indentation",
                        severity="warning"
                    ))

                prev_indent = indent

        # Check for missing whitespace
        for i, line in enumerate(lines):
            if re.search(r"[,=+\-*/%&|^][\w(]", line):
                issues.append(StyleIssue(
                    issue_type="missing-whitespace",
                    line_number=i + 1,
                    message=f"Missing whitespace after operator",
                    severity="warning"
                ))

        return issues

    def _calculate_python_naming_score(self, code: str) -> float:
        """Calculate Python naming convention score.

        Args:
            code: Python code to analyze

        Returns:
            Naming convention score
        """
        # Check function names (should be snake_case)
        function_pattern = r"def\s+(\w+)\s*\("
        function_names = re.findall(function_pattern, code)

        # Check variable names
        variable_pattern = r"(\w+)\s*="
        variable_names = re.findall(variable_pattern, code)

        # Check class names (should be PascalCase)
        class_pattern = r"class\s+(\w+)"
        class_names = re.findall(class_pattern, code)

        # Count correctly named identifiers
        correct_count = 0
        total_count = 0

        # Check function names (should be snake_case)
        for name in function_names:
            total_count += 1
            if re.match(r"^[a-z][a-z0-9_]*$", name):
                correct_count += 1

        # Check variable names (should be snake_case)
        for name in variable_names:
            if name in ["i", "j", "k", "x", "y", "z"]:
                # Common short names are fine
                correct_count += 1
                total_count += 1
            elif re.match(r"^[a-z][a-z0-9_]*$", name):
                correct_count += 1
                total_count += 1
            else:
                total_count += 1

        # Check class names (should be PascalCase)
        for name in class_names:
            total_count += 1
            if re.match(r"^[A-Z][a-zA-Z0-9]*$", name):
                correct_count += 1

        # Calculate naming score
        naming_score = correct_count / total_count if total_count > 0 else 1.0

        return naming_score

    def _analyze_javascript_style(self, code: str) -> StyleAnalysisResult:
        """Analyze JavaScript code style.

        Args:
            code: JavaScript code to analyze

        Returns:
            Style analysis result
        """
        # This is a simplified implementation
        # In a real system, you'd use ESLint or similar

        style_issues = []
        lines = code.split("\n")

        # Check line length
        for i, line in enumerate(lines):
            if len(line) > 100:
                style_issues.append(StyleIssue(
                    issue_type="line-too-long",
                    line_number=i + 1,
                    message=f"Line too long ({len(line)} > 100 characters)",
                    severity="warning"
                ))

        # Check for missing semicolons
        for i, line in enumerate(lines):
            line = line.strip()
            if line and not line.endswith(";") and not line.endswith("{") and not line.endswith("}") and not line.endswith(":"):
                style_issues.append(StyleIssue(
                    issue_type="missing-semicolon",
                    line_number=i + 1,
                    message="Missing semicolon",
                    severity="warning"
                ))

        # Calculate style score
        issue_count = len(style_issues)
        line_count = len(lines)

        issue_density = issue_count / line_count if line_count > 0 else 0
        style_score = max(0.0, 1.0 - min(issue_density * 2, 1.0))

        # Calculate naming convention score
        naming_score = 1.0  # Simplified

        return StyleAnalysisResult(
            style_score=style_score,
            naming_convention_score=naming_score,
            style_issues=style_issues
        )

    def _analyze_java_style(self, code: str) -> StyleAnalysisResult:
        """Analyze Java code style.

        Args:
            code: Java code to analyze

        Returns:
            Style analysis result
        """
        # This is a simplified implementation
        # In a real system, you'd use Checkstyle or similar

        style_issues = []
        lines = code.split("\n")

        # Check line length
        for i, line in enumerate(lines):
            if len(line) > 100:
                style_issues.append(StyleIssue(
                    issue_type="line-too-long",
                    line_number=i + 1,
                    message=f"Line too long ({len(line)} > 100 characters)",
                    severity="warning"
                ))

        # Check for missing braces
        for i, line in enumerate(lines):
            if re.search(r"(if|for|while)\s*\([^)]*\)\s*[^{]", line) and not re.search(r"(if|for|while)\s*\([^)]*\)\s*;", line):
                style_issues.append(StyleIssue(
                    issue_type="missing-braces",
                    line_number=i + 1,
                    message="Missing braces for control statement",
                    severity="warning"
                ))

        # Calculate style score
        issue_count = len(style_issues)
        line_count = len(lines)

        issue_density = issue_count / line_count if line_count > 0 else 0
        style_score = max(0.0, 1.0 - min(issue_density * 2, 1.0))

        # Calculate naming convention score
        naming_score = 1.0  # Simplified

        return StyleAnalysisResult(
            style_score=style_score,
            naming_convention_score=naming_score,
            style_issues=style_issues
        )
