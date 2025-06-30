import os
import re
import json
import tempfile
import subprocess
import logging
import shutil
import stat
from typing import Dict, Any, List, Optional, Tuple

# Import additional test runners

logger = logging.getLogger(__name__)

class CodeExecutionService:
    """Service for executing code in a secure Docker environment."""

    # Default timeout for code execution in seconds
    DEFAULT_TIMEOUT = 10

    # Maximum memory limit for containers (in MB)
    MEMORY_LIMIT = "256m"

    # Base Docker images for each language
    DOCKER_IMAGES = {
        "python": "python:3.9-slim",
        "javascript": "node:16-alpine",
        "java": "openjdk:11-jdk-slim",
        "go": "golang:1.19-alpine",
        "ruby": "ruby:3.1-alpine",
        "cpp": "gcc:11",
    }

    def __init__(self):
        """Initialize the code execution service."""
        # Check if Docker is available
        try:
            subprocess.run(["docker", "--version"], check=True, capture_output=True)
            self.docker_available = True
        except (subprocess.SubprocessError, FileNotFoundError):
            logger.error("Docker is not available. Code execution requires Docker for security.")
            self.docker_available = False

    def _handle_error_readonly_files(self, func, path, exc_info):
        """Handle permission errors when removing temporary files.

        This is a custom error handler for shutil.rmtree that handles permission errors
        by making the files writable and then retrying the operation.

        Args:
            func: The function that failed
            path: The path that was being processed
            exc_info: The exception information
        """
        # Check if the error is a permission error
        if isinstance(exc_info[1], PermissionError):
            try:
                # Make the file or directory writable
                os.chmod(path, stat.S_IWRITE)
                # Try the function again
                func(path)
            except Exception as e:
                logger.warning(f"Failed to remove temporary file {path}: {e}")
        else:
            logger.warning(f"Failed to remove temporary file {path}: {exc_info[1]}")

    def _safe_temp_dir(self):
        """Create a temporary directory with safe cleanup.

        Returns:
            A context manager for a temporary directory that handles permission errors.
        """
        class SafeTempDir:
            def __init__(self, prefix=None):
                self.name = tempfile.mkdtemp(prefix=prefix)

            def __enter__(self):
                return self.name

            def __exit__(self, exc_type, exc_val, exc_tb):
                try:
                    shutil.rmtree(self.name, onerror=self._handle_error_readonly_files)
                except Exception as e:
                    logger.warning(f"Failed to remove temporary directory {self.name}: {e}")

            def _handle_error_readonly_files(self, func, path, exc_info):
                # Check if the error is a permission error
                if isinstance(exc_info[1], PermissionError):
                    try:
                        # Make the file or directory writable
                        os.chmod(path, stat.S_IWRITE)
                        # Try the function again
                        func(path)
                    except Exception as e:
                        logger.warning(f"Failed to remove temporary file {path}: {e}")
                else:
                    logger.warning(f"Failed to remove temporary file {path}: {exc_info[1]}")

        return SafeTempDir(prefix="code_execution_")

    def execute_code_with_tests(self, code: str, language: str, test_cases: List[Dict],
                               timeout: int = DEFAULT_TIMEOUT) -> Dict[str, Any]:
        """Execute code with test cases and return formatted results for API.

        Args:
            code: The code to execute
            language: The programming language
            test_cases: List of test cases with input and expected output
            timeout: Maximum execution time in seconds

        Returns:
            Dictionary with success status and test results
        """
        # Validate that we have actual code to execute
        if not code or code.strip() == "":
            return {
                "success": False,
                "error": "No code provided for execution",
                "test_results": []
            }

        # Check if code is just starter code (contains only comments and function signature)
        if self._is_starter_code_only(code, language):
            return {
                "success": False,
                "error": "Code appears to contain only starter template without implementation",
                "test_results": []
            }

        test_results = self.execute_code(code, language, test_cases, timeout)

        # Check if there was an error
        if len(test_results) == 1 and test_results[0].get("test_case_id") == "error":
            return {
                "success": False,
                "error": test_results[0].get("error_message", "Unknown error"),
                "test_results": []
            }

        # Calculate overall success
        passed_tests = sum(1 for result in test_results if result.get("passed", False))
        total_tests = len(test_results)
        overall_success = passed_tests == total_tests

        return {
            "success": overall_success,
            "test_results": test_results,
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "execution_summary": {
                "total_execution_time": sum(result.get("execution_time", 0) for result in test_results),
                "average_execution_time": sum(result.get("execution_time", 0) for result in test_results) / max(1, total_tests),
                "total_memory_usage": sum(result.get("memory_usage", 0) for result in test_results)
            }
        }

    def _is_starter_code_only(self, code: str, language: str) -> bool:
        """Check if the code contains only starter template without actual implementation.

        Args:
            code: The code to check
            language: The programming language

        Returns:
            True if code appears to be only starter template
        """
        # Remove comments and whitespace
        lines = code.strip().split('\n')
        non_comment_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Skip comment lines based on language
            if language == "python" and line.startswith('#'):
                continue
            elif language == "javascript" and (line.startswith('//') or line.startswith('/*') or line.startswith('*')):
                continue
            elif language == "java" and (line.startswith('//') or line.startswith('/*') or line.startswith('*')):
                continue
            elif language in ["cpp", "c++"] and (line.startswith('//') or line.startswith('/*') or line.startswith('*')):
                continue
            elif language == "go" and line.startswith('//'):
                continue
            elif language == "ruby" and line.startswith('#'):
                continue

            non_comment_lines.append(line)

        # Check if we only have function signatures and placeholder comments
        code_content = '\n'.join(non_comment_lines)

        # Common patterns that indicate starter code
        starter_patterns = [
            "// Your code here",
            "# Your code here",
            "/* Your code here */",
            "// TODO:",
            "# TODO:",
            "pass",  # Python placeholder
            "return null;",  # JavaScript placeholder
            "return 0;",  # C++ placeholder
            "return nil",  # Go placeholder
        ]

        # If the code contains only function signatures and placeholders
        has_implementation = False
        for line in non_comment_lines:
            # Skip function signatures, class declarations, imports, etc.
            if any(keyword in line for keyword in ['def ', 'function ', 'class ', 'public ', 'private ', 'import ', 'package ', 'func ', 'var ', 'const ']):
                continue
            if line in ['{', '}', '(', ')', ';']:
                continue
            if any(pattern in line for pattern in starter_patterns):
                continue
            if line.strip():
                has_implementation = True
                break

        return not has_implementation

    def execute_code(self, code: str, language: str, test_cases: List[Dict],
                     timeout: int = DEFAULT_TIMEOUT) -> List[Dict]:
        """Execute code with the given test cases in a secure Docker environment.

        Args:
            code: The code to execute
            language: The programming language (python, javascript, java, go, ruby, cpp, etc.)
            test_cases: List of test cases with input and expected output
            timeout: Maximum execution time in seconds

        Returns:
            List of test case results
        """
        language = language.lower()

        # Allow new languages to work without Docker (simulated execution)
        if not self.docker_available and language not in ["go", "ruby", "cpp"]:
            logger.error("Docker is not available. Code execution requires Docker for security.")
            return [{
                "test_case_id": "error",
                "passed": False,
                "actual_output": "",
                "expected_output": "",
                "execution_time": 0.0,
                "error_message": "Docker is not available. Code execution requires Docker for security."
            }]

        if language not in self.DOCKER_IMAGES:
            logger.warning(f"Language {language} not supported. Supported languages: {', '.join(self.DOCKER_IMAGES.keys())}")
            return [{
                "test_case_id": "error",
                "passed": False,
                "actual_output": "",
                "expected_output": "",
                "execution_time": 0.0,
                "error_message": f"Language {language} not supported. Supported languages: {', '.join(self.DOCKER_IMAGES.keys())}"
            }]

        try:
            # Create temporary directory for code and test files with safe cleanup
            with self._safe_temp_dir() as temp_dir:
                try:
                    # Write code to file
                    code_file_path, code_file_name = self._write_code_file(code, language, temp_dir)

                    # Write test cases to file
                    test_file_path = os.path.join(temp_dir, "test_cases.json")
                    with open(test_file_path, "w") as f:
                        json.dump(test_cases, f)

                    # Write test runner script
                    runner_path = self._write_test_runner(language, temp_dir, code_file_name)

                    # Run the code in Docker
                    results = self._run_in_docker(language, temp_dir, timeout)

                    return results
                except Exception as e:
                    logger.error(f"Error executing code: {e}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": f"Error executing code: {str(e)}"
                    }]
        except Exception as e:
            logger.error(f"Error creating temporary directory: {e}")
            return [{
                "test_case_id": "error",
                "passed": False,
                "actual_output": "",
                "expected_output": "",
                "execution_time": 0.0,
                "error_message": f"Error creating temporary directory: {str(e)}"
            }]

    def _write_code_file(self, code: str, language: str, temp_dir: str) -> Tuple[str, str]:
        """Write code to a file with the appropriate extension.

        Args:
            code: The code to write
            language: The programming language
            temp_dir: The temporary directory

        Returns:
            Tuple of (file path, file name)
        """
        extensions = {
            "python": ".py",
            "javascript": ".js",
            "java": ".java",
            "cpp": ".cpp",
            "csharp": ".cs",
            "go": ".go",
            "ruby": ".rb"
        }

        ext = extensions.get(language, ".txt")
        file_name = f"solution{ext}"
        file_path = os.path.join(temp_dir, file_name)

        with open(file_path, "w") as f:
            f.write(code)

        return file_path, file_name

    def _write_test_runner(self, language: str, temp_dir: str, code_file_name: str) -> str:
        """Write a test runner script for the specified language.

        Args:
            language: The programming language
            temp_dir: The temporary directory
            code_file_name: The name of the code file

        Returns:
            Path to the test runner script
        """
        if language == "python":
            return self._write_python_test_runner(temp_dir, code_file_name)
        elif language == "javascript":
            return self._write_javascript_test_runner(temp_dir, code_file_name)
        elif language == "java":
            return self._write_java_test_runner(temp_dir, code_file_name)
        elif language in ["go", "ruby", "cpp"]:
            # For new languages, we use simulated execution, so just create a dummy file
            dummy_runner = os.path.join(temp_dir, "dummy_runner.txt")
            with open(dummy_runner, "w") as f:
                f.write(f"Dummy runner for {language} - using simulated execution")
            return dummy_runner
        else:
            # Default to Python
            logger.warning(f"No specific test runner for {language}, defaulting to Python")
            return self._write_python_test_runner(temp_dir, code_file_name)

    def _write_python_test_runner(self, temp_dir: str, code_file_name: str) -> str:
        """Write a Python test runner script.

        Args:
            temp_dir: The temporary directory
            code_file_name: The name of the code file

        Returns:
            Path to the test runner script
        """
        runner_path = os.path.join(temp_dir, "run_tests.py")

        # Create the Python test runner script
        python_test_runner = f"""
import json
import time
import sys
import importlib.util
import traceback

# Load the test cases
with open('test_cases.json', 'r') as f:
    test_cases = json.load(f)

# Import the solution module
spec = importlib.util.spec_from_file_location("solution", "{code_file_name}")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

# Get all functions from the solution module
solution_functions = {{name: func for name, func in solution.__dict__.items()
                     if callable(func) and not name.startswith('__')}}

print(f"Found {{len(solution_functions)}} functions: {{list(solution_functions.keys())}}")

results = []

for i, test_case in enumerate(test_cases):
    test_id = f"test_{{i}}"
    input_value = test_case.get("input", "")
    expected_output = test_case.get("expected_output", "")
    function_name = test_case.get("function_name", "")

    print(f"Running test {{test_id}} with input: {{input_value}}, expected output: {{expected_output}}")

    # Find the function to test
    func = None
    func_name = None

    # Common function names to look for
    common_functions = ['reverse_string', 'reverseString', 'two_sum', 'twoSum', 'is_valid', 'isValid',
                       'is_palindrome', 'isPalindrome', 'max_sub_array', 'maxSubArray', 'merge',
                       'climb_stairs', 'climbStairs', 'rob', 'coin_change', 'coinChange',
                       'length_of_lis', 'lengthOfLIS']

    if function_name and function_name in solution_functions:
        func = solution_functions[function_name]
        func_name = function_name
        print(f"Using specified function: {{function_name}}")
    elif len(solution_functions) == 1:
        # If only one function, use that
        func = next(iter(solution_functions.values()))
        func_name = next(iter(solution_functions.keys()))
        print(f"Using the only available function: {{func_name}}")
    else:
        # Try to find a function by common names
        for name in common_functions:
            if name in solution_functions:
                func = solution_functions[name]
                func_name = name
                print(f"Found function by common name: {{name}}")
                break
        else:
            # Default to the first function
            if solution_functions:
                func = next(iter(solution_functions.values()))
                func_name = next(iter(solution_functions.keys()))
                print(f"Defaulting to first function: {{func_name}}")

    if not func:
        print("No suitable function found")
        results.append({{
            "test_case_id": test_id,
            "passed": False,
            "actual_output": "",
            "expected_output": expected_output,
            "execution_time": 0.0,
            "error_message": "No suitable function found"
        }})
        continue

    try:
        # Parse input based on type
        import inspect
        sig = inspect.signature(func)
        num_params = len(sig.parameters)

        # Handle different input formats
        if isinstance(input_value, str):
            print(f"Processing string input: {{input_value}}")

            # Check if input contains comma-separated values (like "[2,7,11,15], 9")
            if ',' in input_value and '[' in input_value and not (input_value.startswith('[') and input_value.endswith(']')):
                print("Detected multi-argument input format")
                # Split by comma and parse each part
                parts = []
                current_part = ""
                bracket_count = 0

                for char in input_value:
                    if char == '[':
                        bracket_count += 1
                    elif char == ']':
                        bracket_count -= 1
                    elif char == ',' and bracket_count == 0:
                        # This comma is a separator between arguments
                        parts.append(current_part.strip())
                        current_part = ""
                        continue
                    current_part += char

                # Add the last part
                if current_part.strip():
                    parts.append(current_part.strip())

                print(f"Split into parts: {{parts}}")

                # Parse each part
                parsed_args = []
                for part in parts:
                    if part.startswith('[') and part.endswith(']'):
                        try:
                            parsed_args.append(json.loads(part))
                            print(f"Parsed array part: {{part}}")
                        except json.JSONDecodeError:
                            parsed_args.append(part)
                            print(f"Failed to parse array, keeping as string: {{part}}")
                    else:
                        # Try to parse as number, boolean, or keep as string
                        try:
                            # Try integer first
                            parsed_args.append(int(part))
                            print(f"Parsed as int: {{part}}")
                        except ValueError:
                            try:
                                # Try float
                                parsed_args.append(float(part))
                                print(f"Parsed as float: {{part}}")
                            except ValueError:
                                # Try boolean
                                if part.lower() in ['true', 'false']:
                                    parsed_args.append(part.lower() == 'true')
                                    print(f"Parsed as boolean: {{part}}")
                                else:
                                    # Keep as string, remove quotes if present
                                    if part.startswith('"') and part.endswith('"'):
                                        parsed_args.append(part[1:-1])
                                        print(f"Parsed as quoted string: {{part}}")
                                    else:
                                        parsed_args.append(part)
                                        print(f"Keeping as string: {{part}}")

                parsed_input = parsed_args
            elif input_value.startswith('[') and input_value.endswith(']'):
                # Single JSON array
                try:
                    parsed_input = json.loads(input_value)
                    print(f"Parsed as JSON array: {{parsed_input}}")
                except json.JSONDecodeError:
                    parsed_input = input_value
                    print(f"Failed to parse as JSON, keeping as string: {{input_value}}")
            else:
                # Single value - try to parse as JSON first, then as string
                try:
                    parsed_input = json.loads(input_value)
                    print(f"Parsed as JSON: {{parsed_input}}")
                except json.JSONDecodeError:
                    parsed_input = input_value
                    print(f"Keeping as string: {{input_value}}")
        else:
            parsed_input = input_value
            print(f"Non-string input: {{parsed_input}}")

        # Execute the function
        start_time = time.time()
        print(f"Executing function {{func_name}} with {{num_params}} parameters")

        # Determine how to call the function based on parsed input and function signature
        if isinstance(parsed_input, list) and ',' in input_value and '[' in input_value and not input_value.startswith('['):
            # We parsed multiple arguments from a string (like "[2,7,11,15], 9")
            print(f"Calling function with multiple arguments: {{parsed_input}}")
            result = func(*parsed_input)
        elif isinstance(parsed_input, list) and num_params == 1:
            # Single list argument for a function that expects one parameter
            print(f"Calling function with single list argument: {{parsed_input}}")
            result = func(parsed_input)
        elif isinstance(parsed_input, list) and len(parsed_input) == num_params:
            # Multiple arguments from a list
            print(f"Calling function with unpacked list arguments: {{parsed_input}}")
            result = func(*parsed_input)
        else:
            # Single argument
            print(f"Calling function with single argument: {{parsed_input}}")
            result = func(parsed_input)

        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to ms

        print(f"Function returned: {{result}} (type: {{type(result)}})")

        # Convert result to string for comparison
        if isinstance(result, list):
            # For lists, use JSON format without spaces for consistent comparison
            actual_output = json.dumps(result, separators=(',', ':'))
        elif isinstance(result, bool):
            # For booleans, use lowercase string representation
            actual_output = str(result).lower()
        else:
            actual_output = str(result)

        # Normalize expected output for comparison
        expected_str = str(expected_output).strip()
        if expected_str.startswith('[') and expected_str.endswith(']'):
            try:
                # Try to parse and reformat expected output for consistent comparison
                expected_parsed = json.loads(expected_str)
                expected_normalized = json.dumps(expected_parsed, separators=(',', ':'))
            except json.JSONDecodeError:
                expected_normalized = expected_str
        elif expected_str.lower() in ['true', 'false']:
            # Normalize boolean expected output
            expected_normalized = expected_str.lower()
        else:
            expected_normalized = expected_str

        # Check if the output matches the expected output
        passed = actual_output.strip() == expected_normalized.strip()
        print(f"Test {{passed and 'PASSED' or 'FAILED'}}: actual='{{actual_output}}', expected='{{expected_normalized}}'")

        results.append({{
            "test_case_id": test_id,
            "passed": passed,
            "actual_output": actual_output,
            "expected_output": expected_output,
            "execution_time": execution_time,
            "memory_usage": 0.0,  # Memory profiling not implemented
            "error_message": None
        }})
    except Exception as e:
        results.append({{
            "test_case_id": test_id,
            "passed": False,
            "actual_output": "",
            "expected_output": expected_output,
            "execution_time": 0.0,
            "memory_usage": 0.0,
            "error_message": str(e) + "\\n" + traceback.format_exc()
        }})

# Write results to file
with open('results.json', 'w') as f:
    json.dump(results, f)
"""

        with open(runner_path, "w") as f:
            f.write(python_test_runner)

        return runner_path

    def _write_javascript_test_runner(self, temp_dir: str, code_file_name: str) -> str:
        """Write a JavaScript test runner script.

        Args:
            temp_dir: The temporary directory
            code_file_name: The name of the code file

        Returns:
            Path to the test runner script
        """
        runner_path = os.path.join(temp_dir, "run_tests.js")

        # Create a more robust JavaScript test runner script
        js_test_runner = f"""
const fs = require('fs');

// Try to load the solution code by evaluating it
let solutionCode;
try {{
    solutionCode = fs.readFileSync('./{code_file_name}', 'utf8');
    console.log('Successfully loaded solution code');
}} catch (e) {{
    console.error('Error loading solution code:', e);
    const errorResults = [{{
        test_case_id: "error",
        passed: false,
        actual_output: "",
        expected_output: "",
        execution_time: 0.0,
        error_message: `Error loading solution code: ${{e.toString()}}`
    }}];
    fs.writeFileSync('./results.json', JSON.stringify(errorResults, null, 2));
    process.exit(1);
}}

// Evaluate the solution code in the global context
try {{
    eval(solutionCode);
    console.log('Successfully evaluated solution code');
}} catch (e) {{
    console.error('Error evaluating solution code:', e);
    const errorResults = [{{
        test_case_id: "error",
        passed: false,
        actual_output: "",
        expected_output: "",
        execution_time: 0.0,
        error_message: `Error evaluating solution code: ${{e.toString()}}`
    }}];
    fs.writeFileSync('./results.json', JSON.stringify(errorResults, null, 2));
    process.exit(1);
}}

// Try to load test cases
let testCases;
try {{
    const testCasesData = fs.readFileSync('./test_cases.json', 'utf8');
    testCases = JSON.parse(testCasesData);
    console.log(`Loaded ${{testCases.length}} test cases`);
}} catch (e) {{
    console.error('Error loading test cases:', e);
    const errorResults = [{{
        test_case_id: "error",
        passed: false,
        actual_output: "",
        expected_output: "",
        execution_time: 0.0,
        error_message: `Error loading test cases: ${{e.toString()}}`
    }}];
    fs.writeFileSync('./results.json', JSON.stringify(errorResults, null, 2));
    process.exit(1);
}}

// Find available functions in global scope
const availableFunctions = [];
const functionNames = ['reverseString', 'twoSum', 'isValid', 'isPalindrome', 'maxSubArray', 'merge', 'climbStairs', 'rob', 'coinChange', 'lengthOfLIS'];
for (const name of functionNames) {{
    if (typeof global[name] === 'function' || typeof this[name] === 'function' || typeof eval(name) === 'function') {{
        availableFunctions.push(name);
    }}
}}

console.log(`Found ${{availableFunctions.length}} functions: ${{availableFunctions.join(', ')}}`);

const results = [];

for (let i = 0; i < testCases.length; i++) {{
    const testCase = testCases[i];
    const testId = `test_${{i}}`;
    const inputValue = testCase.input || "";
    const expectedOutput = testCase.expected_output || "";

    console.log(`Running test ${{testId}} with input: ${{inputValue}}, expected output: ${{expectedOutput}}`);

    // Find the function to test
    let func = null;
    let funcName = null;

    // Try to find the function by name
    for (const name of availableFunctions) {{
        try {{
            func = eval(name);
            if (typeof func === 'function') {{
                funcName = name;
                break;
            }}
        }} catch (e) {{
            // Continue to next function
        }}
    }}

    if (!func) {{
        console.log('No suitable function found');
        results.push({{
            test_case_id: testId,
            passed: false,
            actual_output: "",
            expected_output: expectedOutput,
            execution_time: 0.0,
            error_message: "No suitable function found"
        }});
        continue;
    }}

    console.log(`Using function: ${{funcName}}`);

    try {{
        // Parse input based on type
        let parsedInput = inputValue;

        // Handle different input formats
        if (typeof inputValue === 'string') {{
            if (inputValue.startsWith('[') && inputValue.endsWith(']')) {{
                try {{
                    parsedInput = JSON.parse(inputValue);
                    console.log(`Parsed input as array: ${{JSON.stringify(parsedInput)}}`);
                }} catch (e) {{
                    console.log(`Failed to parse input as array, using as string: ${{e.message}}`);
                }}
            }} else if (inputValue.includes(',') && inputValue.includes('[')) {{
                // Handle cases like "[2,7,11,15], 9"
                const parts = inputValue.split(',');
                const arrayPart = parts.slice(0, -1).join(',').trim();
                const lastPart = parts[parts.length - 1].trim();

                try {{
                    const array = JSON.parse(arrayPart);
                    const target = parseInt(lastPart);
                    parsedInput = [array, target];
                    console.log(`Parsed input as array with target: ${{JSON.stringify(parsedInput)}}`);
                }} catch (e) {{
                    console.log(`Failed to parse complex input, using as string: ${{e.message}}`);
                }}
            }}
        }}

        // Execute the function
        const startTime = Date.now();
        let result;

        if (Array.isArray(parsedInput) && parsedInput.length > 1 && !inputValue.startsWith('[')) {{
            // Multiple arguments case (like twoSum with array and target)
            console.log(`Calling function with multiple arguments`);
            result = func(...parsedInput);
        }} else if (Array.isArray(parsedInput) && inputValue.startsWith('[')) {{
            // Single array argument case (like reverseString)
            console.log(`Calling function with single array argument`);
            result = func(parsedInput);
        }} else {{
            // Single argument case
            console.log(`Calling function with single argument`);
            result = func(parsedInput);
        }}

        const endTime = Date.now();
        const executionTime = endTime - startTime;

        // Convert result to string for comparison
        let actualOutput;
        if (Array.isArray(result)) {{
            actualOutput = JSON.stringify(result);
        }} else {{
            actualOutput = String(result);
        }}

        console.log(`Function returned: ${{actualOutput}}`);

        // Normalize expected output for comparison
        let normalizedExpected = String(expectedOutput);
        if (normalizedExpected.startsWith('[') && normalizedExpected.endsWith(']')) {{
            try {{
                const parsed = JSON.parse(normalizedExpected);
                normalizedExpected = JSON.stringify(parsed);
            }} catch (e) {{
                // Keep as string if parsing fails
            }}
        }}

        // Check if the output matches the expected output
        const passed = actualOutput === normalizedExpected;
        console.log(`Test ${{passed ? 'PASSED' : 'FAILED'}} (actual: ${{actualOutput}}, expected: ${{normalizedExpected}})`);

        results.push({{
            test_case_id: testId,
            passed: passed,
            actual_output: actualOutput,
            expected_output: expectedOutput,
            execution_time: executionTime,
            memory_usage: 0.0,
            error_message: null
        }});
    }} catch (e) {{
        console.error(`Error executing function:`, e);
        results.push({{
            test_case_id: testId,
            passed: false,
            actual_output: "",
            expected_output: expectedOutput,
            execution_time: 0.0,
            memory_usage: 0.0,
            error_message: e.toString() + "\\n" + e.stack
        }});
    }}
}}

// Write results to file
console.log(`Writing results to file`);
fs.writeFileSync('./results.json', JSON.stringify(results, null, 2));
console.log(`Test execution complete`);
"""

        with open(runner_path, "w") as f:
            f.write(js_test_runner)

        return runner_path

    def _write_java_test_runner(self, temp_dir: str, code_file_name: str) -> str:
        """Write a Java test runner script.

        Args:
            temp_dir: The temporary directory
            code_file_name: The name of the code file

        Returns:
            Path to the test runner script
        """
        # Extract class name from Java file
        class_name = "Solution"  # Default class name
        try:
            with open(os.path.join(temp_dir, code_file_name), "r") as f:
                java_code = f.read()
                class_match = re.search(r"public\s+class\s+(\w+)", java_code)
                if class_match:
                    class_name = class_match.group(1)
        except Exception as e:
            logger.warning(f"Error extracting class name from Java file: {e}")

        # Create test runner Java file
        runner_path = os.path.join(temp_dir, "TestRunner.java")

        # Create a more robust Java test runner script
        java_test_runner = f"""
import java.io.FileReader;
import java.io.FileWriter;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.io.PrintWriter;
import java.io.StringWriter;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class TestRunner {{
    public static void main(String[] args) {{
        System.out.println("Starting test runner");

        try {{
            // Load test cases
            System.out.println("Loading test cases");
            JSONParser parser = new JSONParser();
            JSONArray testCases;
            try {{
                testCases = (JSONArray) parser.parse(new FileReader("test_cases.json"));
                System.out.println("Loaded " + testCases.size() + " test cases");
            }} catch (Exception e) {{
                System.err.println("Error loading test cases: " + e.getMessage());
                e.printStackTrace();

                // Create error result
                JSONArray errorResults = new JSONArray();
                JSONObject errorResult = new JSONObject();
                errorResult.put("test_case_id", "error");
                errorResult.put("passed", false);
                errorResult.put("actual_output", "");
                errorResult.put("expected_output", "");
                errorResult.put("execution_time", 0.0);
                errorResult.put("error_message", "Error loading test cases: " + e.toString());
                errorResults.add(errorResult);

                // Write error results to file
                FileWriter file = new FileWriter("results.json");
                file.write(errorResults.toJSONString());
                file.flush();
                file.close();

                return;
            }}

            // Create instance of solution class
            System.out.println("Loading solution class: {class_name}");
            Class<?> solutionClass;
            Object solutionInstance;
            Method[] methods;

            try {{
                solutionClass = Class.forName("{class_name}");
                solutionInstance = solutionClass.getDeclaredConstructor().newInstance();
                methods = solutionClass.getDeclaredMethods();
                System.out.println("Found " + methods.length + " methods in solution class");

                // Print method names for debugging
                for (Method method : methods) {{
                    System.out.println("  Method: " + method.getName() + ", Parameters: " + method.getParameterCount());
                }}
            }} catch (Exception e) {{
                System.err.println("Error loading solution class: " + e.getMessage());
                e.printStackTrace();

                // Create error result
                JSONArray errorResults = new JSONArray();
                JSONObject errorResult = new JSONObject();
                errorResult.put("test_case_id", "error");
                errorResult.put("passed", false);
                errorResult.put("actual_output", "");
                errorResult.put("expected_output", "");
                errorResult.put("execution_time", 0.0);
                errorResult.put("error_message", "Error loading solution class: " + e.toString());
                errorResults.add(errorResult);

                // Write error results to file
                FileWriter file = new FileWriter("results.json");
                file.write(errorResults.toJSONString());
                file.flush();
                file.close();

                return;
            }}

            JSONArray results = new JSONArray();

            for (int i = 0; i < testCases.size(); i++) {{
                JSONObject testCase = (JSONObject) testCases.get(i);
                String testId = "test_" + i;
                String inputValue = testCase.containsKey("input") ? testCase.get("input").toString() : "";
                String expectedOutput = testCase.containsKey("expected_output") ? testCase.get("expected_output").toString() : "";
                String functionName = testCase.containsKey("function_name") ? testCase.get("function_name").toString() : "";

                System.out.println("Running test " + testId + " with input: " + inputValue + ", expected output: " + expectedOutput);

                // Find the method to test
                Method methodToTest = null;

                if (!functionName.isEmpty()) {{
                    // Try to find by name
                    for (Method method : methods) {{
                        if (method.getName().equals(functionName)) {{
                            methodToTest = method;
                            System.out.println("Found method by name: " + functionName);
                            break;
                        }}
                    }}
                }}

                if (methodToTest == null && methods.length == 1) {{
                    // If only one method, use that
                    methodToTest = methods[0];
                    System.out.println("Using the only available method: " + methodToTest.getName());
                }}

                if (methodToTest == null && testCase.containsKey("description")) {{
                    // Try to find a method with a name that matches the test case
                    String description = testCase.get("description").toString().toLowerCase();
                    for (Method method : methods) {{
                        if (description.contains(method.getName().toLowerCase())) {{
                            methodToTest = method;
                            System.out.println("Found method by description match: " + method.getName());
                            break;
                        }}
                    }}
                }}

                if (methodToTest == null && methods.length > 0) {{
                    // Default to the first method
                    methodToTest = methods[0];
                    System.out.println("Defaulting to first method: " + methodToTest.getName());
                }}

                if (methodToTest == null) {{
                    System.out.println("No suitable method found");
                    JSONObject result = new JSONObject();
                    result.put("test_case_id", testId);
                    result.put("passed", false);
                    result.put("actual_output", "");
                    result.put("expected_output", expectedOutput);
                    result.put("execution_time", 0.0);
                    result.put("error_message", "No suitable method found");
                    results.add(result);
                    continue;
                }}

                try {{
                    // Parse input based on parameter type
                    Object parsedInput = inputValue;
                    Class<?>[] paramTypes = methodToTest.getParameterTypes();

                    System.out.println("Method expects " + paramTypes.length + " parameters");
                    if (paramTypes.length > 0) {{
                        System.out.println("First parameter type: " + paramTypes[0].getName());
                    }}

                    if (paramTypes.length == 1) {{
                        // Handle single parameter
                        if (paramTypes[0] == int.class || paramTypes[0] == Integer.class) {{
                            System.out.println("Converting input to int: " + inputValue);
                            parsedInput = Integer.parseInt(inputValue);
                        }} else if (paramTypes[0] == double.class || paramTypes[0] == Double.class) {{
                            System.out.println("Converting input to double: " + inputValue);
                            parsedInput = Double.parseDouble(inputValue);
                        }} else if (paramTypes[0] == boolean.class || paramTypes[0] == Boolean.class) {{
                            System.out.println("Converting input to boolean: " + inputValue);
                            parsedInput = Boolean.parseBoolean(inputValue);
                        }} else if (paramTypes[0] == String.class) {{
                            System.out.println("Using input as string: " + inputValue);
                            // Already a string
                        }} else if (paramTypes[0].isArray()) {{
                            System.out.println("Parameter is an array type: " + paramTypes[0].getComponentType().getName());
                        }}
                    }}

                    // Execute the method
                    System.out.println("Executing method: " + methodToTest.getName());
                    long startTime = System.currentTimeMillis();
                    Object result;

                    // Check if the input is a JSON array and the method expects an array
                    if (inputValue.startsWith("[") && inputValue.endsWith("]") &&
                        methodToTest.getParameterTypes().length == 1 &&
                        methodToTest.getParameterTypes()[0].isArray()) {{
                        // Parse the JSON array into a Java array
                        try {{
                            System.out.println("Parsing input as JSON array: " + inputValue);
                            org.json.simple.JSONArray jsonArray = (org.json.simple.JSONArray) new org.json.simple.parser.JSONParser().parse(inputValue);
                            Object[] array = jsonArray.toArray();
                            System.out.println("Parsed array with " + array.length + " elements");

                            // Create an array of the correct type
                            Class<?> componentType = methodToTest.getParameterTypes()[0].getComponentType();
                            Object typedArray = java.lang.reflect.Array.newInstance(componentType, array.length);
                            System.out.println("Created typed array of " + componentType.getName());

                            // Convert and copy elements
                            for (int j = 0; j < array.length; j++) {{
                                if (componentType == int.class || componentType == Integer.class) {{
                                    java.lang.reflect.Array.set(typedArray, j, ((Number)array[j]).intValue());
                                }} else if (componentType == double.class || componentType == Double.class) {{
                                    java.lang.reflect.Array.set(typedArray, j, ((Number)array[j]).doubleValue());
                                }} else if (componentType == boolean.class || componentType == Boolean.class) {{
                                    java.lang.reflect.Array.set(typedArray, j, (Boolean)array[j]);
                                }} else if (componentType == String.class) {{
                                    java.lang.reflect.Array.set(typedArray, j, array[j].toString());
                                }}
                            }}

                            // Invoke the method with the typed array
                            System.out.println("Invoking method with typed array");
                            result = methodToTest.invoke(solutionInstance, typedArray);
                        }} catch (Exception e) {{
                            System.err.println("Error parsing array, falling back to original approach: " + e.getMessage());
                            // If parsing fails, fall back to the original approach
                            result = methodToTest.invoke(solutionInstance, parsedInput);
                        }}
                    }} else {{
                        // Use the original approach
                        System.out.println("Invoking method with original input: " + parsedInput);
                        result = methodToTest.invoke(solutionInstance, parsedInput);
                    }}

                    long endTime = System.currentTimeMillis();
                    long executionTime = endTime - startTime;

                    // Convert result to string for comparison
                    String actualOutput = result != null ? result.toString() : "null";
                    System.out.println("Method returned: " + actualOutput);

                    // Check if the output matches the expected output
                    boolean passed = actualOutput.trim().equals(expectedOutput.trim());
                    System.out.println("Test " + (passed ? "PASSED" : "FAILED"));

                    JSONObject resultObj = new JSONObject();
                    resultObj.put("test_case_id", testId);
                    resultObj.put("passed", passed);
                    resultObj.put("actual_output", actualOutput);
                    resultObj.put("expected_output", expectedOutput);
                    resultObj.put("execution_time", (double) executionTime);
                    resultObj.put("memory_usage", 0.0);
                    resultObj.put("error_message", null);

                    results.add(resultObj);
                }} catch (Exception e) {{
                    System.err.println("Error executing method: " + e.getMessage());
                    e.printStackTrace();

                    StringWriter sw = new StringWriter();
                    PrintWriter pw = new PrintWriter(sw);
                    e.printStackTrace(pw);

                    JSONObject resultObj = new JSONObject();
                    resultObj.put("test_case_id", testId);
                    resultObj.put("passed", false);
                    resultObj.put("actual_output", "");
                    resultObj.put("expected_output", expectedOutput);
                    resultObj.put("execution_time", 0.0);
                    resultObj.put("memory_usage", 0.0);
                    resultObj.put("error_message", e.toString() + "\\n" + sw.toString());

                    results.add(resultObj);
                }}
            }}

            // Write results to file
            System.out.println("Writing results to file");
            FileWriter file = new FileWriter("results.json");
            file.write(results.toJSONString());
            file.flush();
            file.close();
            System.out.println("Test execution complete");

        }} catch (Exception e) {{
            System.err.println("Unhandled exception in test runner: " + e.getMessage());
            e.printStackTrace();

            try {{
                // Create error result
                JSONArray errorResults = new JSONArray();
                JSONObject errorResult = new JSONObject();
                errorResult.put("test_case_id", "error");
                errorResult.put("passed", false);
                errorResult.put("actual_output", "");
                errorResult.put("expected_output", "");
                errorResult.put("execution_time", 0.0);
                errorResult.put("error_message", "Unhandled exception in test runner: " + e.toString());
                errorResults.add(errorResult);

                // Write error results to file
                FileWriter file = new FileWriter("results.json");
                file.write(errorResults.toJSONString());
                file.flush();
                file.close();
            }} catch (Exception ex) {{
                System.err.println("Failed to write error results: " + ex.getMessage());
                ex.printStackTrace();
            }}
        }}
    }}
}}
"""

        with open(runner_path, "w") as f:
            f.write(java_test_runner)

        # Create a Dockerfile to compile and run the Java code
        dockerfile_path = os.path.join(temp_dir, "Dockerfile")
        with open(dockerfile_path, "w") as f:
            f.write(f"""
FROM openjdk:11-jdk-slim

WORKDIR /app

# Copy the solution and test files
COPY {code_file_name} /app/
COPY TestRunner.java /app/
COPY test_cases.json /app/

# Install JSON Simple for parsing test cases
RUN apt-get update && apt-get install -y wget
RUN wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/json-simple/json-simple-1.1.1.jar

# Compile the solution and test runner
RUN javac -cp json-simple-1.1.1.jar {code_file_name} TestRunner.java

# Run the tests
CMD ["java", "-cp", ".:json-simple-1.1.1.jar", "TestRunner"]
""")

        return runner_path

    def _write_go_test_runner(self, temp_dir: str, code_file_name: str) -> str:
        """Write a Go test runner script.

        Args:
            temp_dir: The temporary directory
            code_file_name: The name of the code file

        Returns:
            Path to the test runner script
        """
        runner_path = os.path.join(temp_dir, "main.go")

        # Create the Go test runner script
        with open(runner_path, "w") as f:
            f.write(f"""package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "log"
    "os"
    "reflect"
    "strconv"
    "strings"
    "time"
)

type TestCase struct {{
    Input          string  `json:"input"`
    ExpectedOutput string  `json:"expected_output"`
    Weight         float64 `json:"weight"`
}}

type TestResult struct {{
    TestCaseID     string  `json:"test_case_id"`
    Passed         bool    `json:"passed"`
    ActualOutput   string  `json:"actual_output"`
    ExpectedOutput string  `json:"expected_output"`
    ExecutionTime  float64 `json:"execution_time"`
    MemoryUsage    float64 `json:"memory_usage"`
    ErrorMessage   *string `json:"error_message"`
}}

func main() {{
    // Read test cases
    testData, err := ioutil.ReadFile("test_cases.json")
    if err != nil {{
        log.Fatal("Error reading test cases:", err)
    }}

    var testCases []TestCase
    err = json.Unmarshal(testData, &testCases)
    if err != nil {{
        log.Fatal("Error parsing test cases:", err)
    }}

    var results []TestResult

    for i, testCase := range testCases {{
        testID := fmt.Sprintf("test_%d", i)

        start := time.Now()

        // Parse input
        input := testCase.Input
        var result interface{{}}
        var errorMsg *string

        // Execute the function based on input format
        if strings.Contains(input, ",") && strings.Contains(input, "[") {{
            // Two sum case: "[2,7,11,15], 9"
            parts := strings.Split(input, ",")
            if len(parts) >= 2 {{
                // Parse array part
                arrayPart := strings.TrimSpace(parts[0])
                for j := 1; j < len(parts)-1; j++ {{
                    arrayPart += "," + strings.TrimSpace(parts[j])
                }}

                // Parse target part
                targetPart := strings.TrimSpace(parts[len(parts)-1])

                // Convert array string to slice
                arrayStr := strings.Trim(arrayPart, "[]")
                if arrayStr != "" {{
                    numStrs := strings.Split(arrayStr, ",")
                    nums := make([]int, len(numStrs))
                    for k, numStr := range numStrs {{
                        nums[k], _ = strconv.Atoi(strings.TrimSpace(numStr))
                    }}

                    target, _ := strconv.Atoi(targetPart)
                    result = twoSum(nums, target)
                }}
            }}
        }} else {{
            // Single string input
            cleanInput := strings.Trim(input, `"`)
            if strings.HasPrefix(input, `"`) && strings.HasSuffix(input, `"`) {{
                // String function
                result = reverseString(cleanInput)
            }} else {{
                // Boolean function
                result = isValid(cleanInput)
            }}
        }}

        duration := time.Since(start)

        // Convert result to string
        var actualOutput string
        if result != nil {{
            if reflect.TypeOf(result).Kind() == reflect.Slice {{
                jsonBytes, _ := json.Marshal(result)
                actualOutput = string(jsonBytes)
            }} else {{
                actualOutput = fmt.Sprintf("%v", result)
            }}
        }}

        // Check if test passed
        passed := actualOutput == testCase.ExpectedOutput

        results = append(results, TestResult{{
            TestCaseID:     testID,
            Passed:         passed,
            ActualOutput:   actualOutput,
            ExpectedOutput: testCase.ExpectedOutput,
            ExecutionTime:  float64(duration.Nanoseconds()) / 1e6, // Convert to milliseconds
            MemoryUsage:    0.0,
            ErrorMessage:   errorMsg,
        }})
    }}

    // Output results as JSON
    output, err := json.Marshal(results)
    if err != nil {{
        log.Fatal("Error marshaling results:", err)
    }}

    fmt.Println(string(output))
}}

// Include the user's code here
""")

        # Read and append the user's code
        code_file_path = os.path.join(temp_dir, code_file_name)
        if os.path.exists(code_file_path):
            with open(code_file_path, "r") as code_file:
                user_code = code_file.read()
                f.write(user_code)

        return runner_path

    def _write_ruby_test_runner(self, temp_dir: str, code_file_name: str) -> str:
        """Write a Ruby test runner script.

        Args:
            temp_dir: The temporary directory
            code_file_name: The name of the code file

        Returns:
            Path to the test runner script
        """
        runner_path = os.path.join(temp_dir, "run_tests.rb")

        # Create the Ruby test runner script
        with open(runner_path, "w") as f:
            f.write(f"""require 'json'
require 'time'

# Load the user's code
require_relative '{code_file_name.replace('.rb', '')}'

# Read test cases
test_cases = JSON.parse(File.read('test_cases.json'))

results = []

test_cases.each_with_index do |test_case, index|
  test_id = "test_#{{index}}"

  start_time = Time.now

  begin
    input = test_case['input']
    expected_output = test_case['expected_output']

    # Parse input and call appropriate function
    result = nil

    if input.include?(',') && input.include?('[')
      # Two sum case: "[2,7,11,15], 9"
      parts = input.split(',')
      array_part = parts[0..-2].join(',').strip
      target_part = parts[-1].strip

      # Parse array
      array_str = array_part.tr('[]', '')
      nums = array_str.split(',').map(&:to_i) unless array_str.empty?
      target = target_part.to_i

      result = two_sum(nums, target)
    elsif input.start_with?('"') && input.end_with?('"')
      # String input
      clean_input = input[1..-2]  # Remove quotes
      result = reverse_string(clean_input)
    else
      # Boolean function
      result = is_valid(input)
    end

    end_time = Time.now
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds

    # Convert result to string for comparison
    actual_output = result.is_a?(Array) ? result.to_json.gsub(' ', '') : result.to_s

    # Check if test passed
    passed = actual_output == expected_output

    results << {{
      test_case_id: test_id,
      passed: passed,
      actual_output: actual_output,
      expected_output: expected_output,
      execution_time: execution_time,
      memory_usage: 0.0,
      error_message: nil
    }}

  rescue => e
    results << {{
      test_case_id: test_id,
      passed: false,
      actual_output: "",
      expected_output: test_case['expected_output'],
      execution_time: 0.0,
      memory_usage: 0.0,
      error_message: e.message + "\\n" + e.backtrace.join("\\n")
    }}
  end
end

# Output results as JSON
puts JSON.generate(results)
""")

        return runner_path

    def _write_cpp_test_runner(self, temp_dir: str, code_file_name: str) -> str:
        """Write a C++ test runner script.

        Args:
            temp_dir: The temporary directory
            code_file_name: The name of the code file

        Returns:
            Path to the test runner script
        """
        # Create the main test runner
        runner_path = os.path.join(temp_dir, "test_runner.cpp")

        with open(runner_path, "w") as f:
            f.write(f"""#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <chrono>
#include <algorithm>
#include <unordered_map>
#include <stack>

// JSON parsing helper functions
std::vector<int> parseIntArray(const std::string& str) {{
    std::vector<int> result;
    std::string cleaned = str;
    cleaned.erase(std::remove(cleaned.begin(), cleaned.end(), '['), cleaned.end());
    cleaned.erase(std::remove(cleaned.begin(), cleaned.end(), ']'), cleaned.end());
    cleaned.erase(std::remove(cleaned.begin(), cleaned.end(), ' '), cleaned.end());

    std::stringstream ss(cleaned);
    std::string item;
    while (std::getline(ss, item, ',')) {{
        if (!item.empty()) {{
            result.push_back(std::stoi(item));
        }}
    }}
    return result;
}}

std::string vectorToString(const std::vector<int>& vec) {{
    std::string result = "[";
    for (size_t i = 0; i < vec.size(); ++i) {{
        result += std::to_string(vec[i]);
        if (i < vec.size() - 1) result += ",";
    }}
    result += "]";
    return result;
}}

std::string boolToString(bool value) {{
    return value ? "true" : "false";
}}

// Include user's solution
""")

        # Read and append the user's code
        code_file_path = os.path.join(temp_dir, code_file_name)
        if os.path.exists(code_file_path):
            with open(code_file_path, "r") as code_file:
                user_code = code_file.read()
                f.write(user_code)

        f.write("""

int main() {
    std::ifstream file("test_cases.json");
    std::string line;
    std::vector<std::string> results;

    // Simple JSON parsing (assumes specific format)
    bool inTestCases = false;
    int testIndex = 0;

    while (std::getline(file, line)) {
        if (line.find("input") != std::string::npos) {
            // Extract input value
            size_t start = line.find(": \"") + 3;
            size_t end = line.find("\",", start);
            if (end == std::string::npos) end = line.find("\"", start);
            std::string input = line.substr(start, end - start);

            // Get expected output from next line
            std::getline(file, line);
            start = line.find(": \"") + 3;
            end = line.find("\",", start);
            if (end == std::string::npos) end = line.find("\"", start);
            std::string expected = line.substr(start, end - start);

            auto startTime = std::chrono::high_resolution_clock::now();

            std::string actual;
            bool passed = false;

            try {
                Solution solution;

                if (input.find(',') != std::string::npos && input.find('[') != std::string::npos) {
                    // Two sum case
                    size_t commaPos = input.rfind(',');
                    std::string arrayPart = input.substr(0, commaPos);
                    std::string targetPart = input.substr(commaPos + 1);

                    // Remove spaces
                    targetPart.erase(std::remove(targetPart.begin(), targetPart.end(), ' '), targetPart.end());

                    std::vector<int> nums = parseIntArray(arrayPart);
                    int target = std::stoi(targetPart);

                    std::vector<int> result = solution.twoSum(nums, target);
                    actual = vectorToString(result);
                } else if (input.front() == '(' || input.front() == '[' || input.front() == '{') {
                    // Valid parentheses case
                    bool result = solution.isValid(input);
                    actual = boolToString(result);
                } else {
                    // String case
                    std::string result = solution.reverseString(input);
                    actual = result;
                }

                passed = (actual == expected);

            } catch (const std::exception& e) {
                actual = "";
                passed = false;
            }

            auto endTime = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime);

            // Output result in JSON format
            std::cout << "{";
            std::cout << "\\"test_case_id\\": \\"test_" << testIndex << "\\", ";
            std::cout << "\\"passed\\": " << (passed ? "true" : "false") << ", ";
            std::cout << "\\"actual_output\\": \\"" << actual << "\\", ";
            std::cout << "\\"expected_output\\": \\"" << expected << "\\", ";
            std::cout << "\\"execution_time\\": " << duration.count() << ", ";
            std::cout << "\\"memory_usage\\": 0.0, ";
            std::cout << "\\"error_message\\": null";
            std::cout << "}";

            testIndex++;

            // Add comma if not last test
            std::streampos pos = file.tellg();
            std::string nextLine;
            if (std::getline(file, nextLine) && nextLine.find("input") != std::string::npos) {
                std::cout << ",";
                file.seekg(pos);
            }
        }
    }

    return 0;
}
""")

        # Create build script
        build_script_path = os.path.join(temp_dir, "build_and_run.sh")
        with open(build_script_path, "w") as f:
            f.write("""#!/bin/bash
echo "["
g++ -std=c++17 -o test_runner test_runner.cpp
./test_runner
echo "]"
""")

        # Make build script executable
        os.chmod(build_script_path, 0o755)

        return runner_path

    def _run_in_docker(self, language: str, temp_dir: str, timeout: int) -> List[Dict]:
        """Run code in a Docker container.

        Args:
            language: The programming language
            temp_dir: The temporary directory containing code and test files
            timeout: Maximum execution time in seconds

        Returns:
            List of test case results
        """
        # Create a unique container name
        container_name = f"code_execution_{os.path.basename(temp_dir)}"

        # Get the Docker image for the language
        docker_image = self.DOCKER_IMAGES.get(language, "python:3.9-slim")

        # For Python, use the standard approach
        if language == "python":
            try:
                cmd = ["python", "run_tests.py"]

                # Log the command for debugging
                logger.info(f"Running Docker command for {language}: {cmd}")

                # Run the container
                run_cmd = [
                    "docker", "run",
                    "--name", container_name,
                    "--memory", self.MEMORY_LIMIT,
                    "-v", f"{os.path.abspath(temp_dir)}:/app",
                    "-w", "/app",
                    "--rm",
                    docker_image,
                    *cmd
                ]

                # Log the full Docker command
                logger.info(f"Full Docker command: {' '.join(run_cmd)}")

                # Run with a reasonable timeout
                actual_timeout = max(timeout, 10)
                subprocess.run(run_cmd, check=True, capture_output=True, timeout=actual_timeout)

                # Read the results
                results_path = os.path.join(temp_dir, "results.json")
                if os.path.exists(results_path):
                    with open(results_path, "r") as f:
                        return json.load(f)
                else:
                    logger.error(f"Results file not found at {results_path}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": "Failed to get results from Docker container"
                    }]
            except subprocess.TimeoutExpired:
                logger.error(f"Python Docker execution timed out after {actual_timeout} seconds")
                return [{
                    "test_case_id": "timeout",
                    "passed": False,
                    "actual_output": "",
                    "expected_output": "",
                    "execution_time": actual_timeout * 1000,
                    "error_message": f"Execution timed out after {actual_timeout} seconds"
                }]
            except subprocess.SubprocessError as e:
                logger.error(f"Python Docker execution error: {str(e)}")
                return [{
                    "test_case_id": "error",
                    "passed": False,
                    "actual_output": "",
                    "expected_output": "",
                    "execution_time": 0.0,
                    "error_message": f"Docker execution error: {str(e)}"
                }]

        # For JavaScript, try to run with Docker if available, otherwise simulate
        elif language == "javascript":
            if self.docker_available:
                try:
                    cmd = ["node", "run_tests.js"]

                    # Log the command for debugging
                    logger.info(f"Running Docker command for {language}: {cmd}")

                    # Run the container
                    run_cmd = [
                        "docker", "run",
                        "--name", container_name,
                        "--memory", self.MEMORY_LIMIT,
                        "-v", f"{os.path.abspath(temp_dir)}:/app",
                        "-w", "/app",
                        "--rm",
                        docker_image,
                        *cmd
                    ]

                    # Log the full Docker command
                    logger.info(f"Full Docker command: {' '.join(run_cmd)}")

                    # Run with a reasonable timeout
                    actual_timeout = max(timeout, 10)
                    result = subprocess.run(run_cmd, check=True, capture_output=True, timeout=actual_timeout, text=True)

                    # Read the results
                    results_path = os.path.join(temp_dir, "results.json")
                    if os.path.exists(results_path):
                        with open(results_path, "r") as f:
                            return json.load(f)
                    else:
                        logger.error(f"Results file not found at {results_path}")
                        logger.error(f"Docker stdout: {result.stdout}")
                        logger.error(f"Docker stderr: {result.stderr}")
                        return [{
                            "test_case_id": "error",
                            "passed": False,
                            "actual_output": "",
                            "expected_output": "",
                            "execution_time": 0.0,
                            "error_message": f"Failed to get results from Docker container. Stdout: {result.stdout}, Stderr: {result.stderr}"
                        }]
                except subprocess.TimeoutExpired:
                    logger.error(f"JavaScript Docker execution timed out after {actual_timeout} seconds")
                    return [{
                        "test_case_id": "timeout",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": actual_timeout * 1000,
                        "error_message": f"Execution timed out after {actual_timeout} seconds"
                    }]
                except subprocess.SubprocessError as e:
                    logger.error(f"JavaScript Docker execution error: {str(e)}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": f"Docker execution error: {str(e)}"
                    }]
            else:
                # Fallback: return failure results indicating Docker is needed
                try:
                    test_file_path = os.path.join(temp_dir, "test_cases.json")
                    with open(test_file_path, "r") as f:
                        test_cases = json.load(f)

                    results = []
                    for i, test_case in enumerate(test_cases):
                        test_id = f"test_{i}"
                        results.append({
                            "test_case_id": test_id,
                            "passed": False,
                            "actual_output": "",
                            "expected_output": test_case.get("expected_output", ""),
                            "execution_time": 0.0,
                            "memory_usage": 0.0,
                            "error_message": "Docker is required for JavaScript code execution but is not available"
                        })

                    logger.info(f"Created failure results for JavaScript code (Docker not available)")
                    return results

                except Exception as e:
                    logger.error(f"JavaScript execution error: {str(e)}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": f"JavaScript execution error: {str(e)}"
                    }]

        # For Java, try to run with Docker if available, otherwise simulate
        elif language == "java":
            if self.docker_available:
                try:
                    # For Java, we need to build first, then run
                    cmd = ["bash", "-c", "javac -cp json-simple-1.1.1.jar *.java && java -cp .:json-simple-1.1.1.jar TestRunner"]

                    # Log the command for debugging
                    logger.info(f"Running Docker command for {language}: {cmd}")

                    # Run the container
                    run_cmd = [
                        "docker", "run",
                        "--name", container_name,
                        "--memory", self.MEMORY_LIMIT,
                        "-v", f"{os.path.abspath(temp_dir)}:/app",
                        "-w", "/app",
                        "--rm",
                        docker_image,
                        *cmd
                    ]

                    # Log the full Docker command
                    logger.info(f"Full Docker command: {' '.join(run_cmd)}")

                    # Run with a reasonable timeout
                    actual_timeout = max(timeout, 30)  # Java needs more time for compilation
                    result = subprocess.run(run_cmd, check=True, capture_output=True, timeout=actual_timeout, text=True)

                    # Read the results
                    results_path = os.path.join(temp_dir, "results.json")
                    if os.path.exists(results_path):
                        with open(results_path, "r") as f:
                            return json.load(f)
                    else:
                        logger.error(f"Results file not found at {results_path}")
                        logger.error(f"Docker stdout: {result.stdout}")
                        logger.error(f"Docker stderr: {result.stderr}")
                        return [{
                            "test_case_id": "error",
                            "passed": False,
                            "actual_output": "",
                            "expected_output": "",
                            "execution_time": 0.0,
                            "error_message": f"Failed to get results from Docker container. Stdout: {result.stdout}, Stderr: {result.stderr}"
                        }]
                except subprocess.TimeoutExpired:
                    logger.error(f"Java Docker execution timed out after {actual_timeout} seconds")
                    return [{
                        "test_case_id": "timeout",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": actual_timeout * 1000,
                        "error_message": f"Execution timed out after {actual_timeout} seconds"
                    }]
                except subprocess.SubprocessError as e:
                    logger.error(f"Java Docker execution error: {str(e)}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": f"Docker execution error: {str(e)}"
                    }]
            else:
                # Fallback: return failure results indicating Docker is needed
                try:
                    test_file_path = os.path.join(temp_dir, "test_cases.json")
                    with open(test_file_path, "r") as f:
                        test_cases = json.load(f)

                    results = []
                    for i, test_case in enumerate(test_cases):
                        test_id = f"test_{i}"
                        results.append({
                            "test_case_id": test_id,
                            "passed": False,
                            "actual_output": "",
                            "expected_output": test_case.get("expected_output", ""),
                            "execution_time": 0.0,
                            "memory_usage": 0.0,
                            "error_message": "Docker is required for Java code execution but is not available"
                        })

                    logger.info(f"Created failure results for Java code (Docker not available)")
                    return results

                except Exception as e:
                    logger.error(f"Java execution error: {str(e)}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": f"Java execution error: {str(e)}"
                    }]

        # For Go, Ruby, and C++, try Docker if available, otherwise indicate Docker is needed
        elif language in ["go", "ruby", "cpp"]:
            if self.docker_available:
                try:
                    cmd = []
                    if language == "go":
                        cmd = ["go", "run", "main.go"]
                    elif language == "ruby":
                        cmd = ["ruby", "run_tests.rb"]
                    elif language == "cpp":
                        cmd = ["bash", "build_and_run.sh"]

                    # Log the command for debugging
                    logger.info(f"Running Docker command for {language}: {cmd}")

                    # Run the container
                    run_cmd = [
                        "docker", "run",
                        "--name", container_name,
                        "--memory", self.MEMORY_LIMIT,
                        "-v", f"{os.path.abspath(temp_dir)}:/app",
                        "-w", "/app",
                        "--rm",
                        docker_image,
                        *cmd
                    ]

                    # Log the full Docker command
                    logger.info(f"Full Docker command: {' '.join(run_cmd)}")

                    # Run with a reasonable timeout
                    actual_timeout = max(timeout, 15)
                    result = subprocess.run(run_cmd, check=True, capture_output=True, timeout=actual_timeout, text=True)

                    # Read the results
                    results_path = os.path.join(temp_dir, "results.json")
                    if os.path.exists(results_path):
                        with open(results_path, "r") as f:
                            return json.load(f)
                    else:
                        logger.error(f"Results file not found at {results_path}")
                        logger.error(f"Docker stdout: {result.stdout}")
                        logger.error(f"Docker stderr: {result.stderr}")
                        return [{
                            "test_case_id": "error",
                            "passed": False,
                            "actual_output": "",
                            "expected_output": "",
                            "execution_time": 0.0,
                            "error_message": f"Failed to get results from Docker container. Stdout: {result.stdout}, Stderr: {result.stderr}"
                        }]
                except subprocess.TimeoutExpired:
                    logger.error(f"{language} Docker execution timed out after {actual_timeout} seconds")
                    return [{
                        "test_case_id": "timeout",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": actual_timeout * 1000,
                        "error_message": f"Execution timed out after {actual_timeout} seconds"
                    }]
                except subprocess.SubprocessError as e:
                    logger.error(f"{language} Docker execution error: {str(e)}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": f"Docker execution error: {str(e)}"
                    }]
            else:
                # Fallback: return failure results indicating Docker is needed
                try:
                    test_file_path = os.path.join(temp_dir, "test_cases.json")
                    with open(test_file_path, "r") as f:
                        test_cases = json.load(f)

                    results = []
                    for i, test_case in enumerate(test_cases):
                        test_id = f"test_{i}"
                        results.append({
                            "test_case_id": test_id,
                            "passed": False,
                            "actual_output": "",
                            "expected_output": test_case.get("expected_output", ""),
                            "execution_time": 0.0,
                            "memory_usage": 0.0,
                            "error_message": f"Docker is required for {language} code execution but is not available"
                        })

                    logger.info(f"Created failure results for {language} code (Docker not available)")
                    return results

                except Exception as e:
                    logger.error(f"{language} execution error: {e}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": f"{language} execution error: {str(e)}"
                    }]

        # For other languages, use the standard approach
        else:
            try:
                cmd = []
                if language == "go":
                    cmd = ["go", "run", "main.go"]
                elif language == "ruby":
                    cmd = ["ruby", "run_tests.rb"]
                elif language == "cpp":
                    cmd = ["bash", "build_and_run.sh"]
                else:
                    # Default to Python
                    cmd = ["python", "run_tests.py"]

                # Log the command for debugging
                logger.info(f"Running Docker command for {language}: {cmd}")

                # Run the container
                run_cmd = [
                    "docker", "run",
                    "--name", container_name,
                    "--memory", self.MEMORY_LIMIT,
                    "-v", f"{os.path.abspath(temp_dir)}:/app",
                    "-w", "/app",
                    "--rm",
                    docker_image,
                    *cmd
                ]

                # Log the full Docker command
                logger.info(f"Full Docker command: {' '.join(run_cmd)}")

                # Run with a reasonable timeout
                actual_timeout = max(timeout, 10)
                subprocess.run(run_cmd, check=True, capture_output=True, timeout=actual_timeout)

                # Read the results
                results_path = os.path.join(temp_dir, "results.json")
                if os.path.exists(results_path):
                    with open(results_path, "r") as f:
                        return json.load(f)
                else:
                    logger.error(f"Results file not found at {results_path}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": "Failed to get results from Docker container"
                    }]
            except subprocess.TimeoutExpired:
                logger.error(f"Docker execution timed out after {actual_timeout} seconds")
                return [{
                    "test_case_id": "timeout",
                    "passed": False,
                    "actual_output": "",
                    "expected_output": "",
                    "execution_time": actual_timeout * 1000,
                    "error_message": f"Execution timed out after {actual_timeout} seconds"
                }]
            except subprocess.SubprocessError as e:
                logger.error(f"Docker execution error: {str(e)}")
                return [{
                    "test_case_id": "error",
                    "passed": False,
                    "actual_output": "",
                    "expected_output": "",
                    "execution_time": 0.0,
                    "error_message": f"Docker execution error: {str(e)}"
                }]
