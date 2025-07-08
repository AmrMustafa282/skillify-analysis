import os
import re
import json
import tempfile
import subprocess
import logging
import shutil
import stat
from typing import Dict, Any, List, Optional, Tuple

logger = logging.getLogger(__name__)

class CodeExecutionService:
    """Service for executing code locally using installed compilers."""

    # Default timeout for code execution in seconds
    DEFAULT_TIMEOUT = 10

    def __init__(self):
        """Initialize the code execution service."""
        # Check if required compilers are available
        self.available_languages = {}

        # Check Python
        try:
            result = subprocess.run(["python3", "--version"], check=True, capture_output=True, text=True)
            self.available_languages["python"] = True
            logger.info(f"Python available: {result.stdout.strip()}")
        except (subprocess.SubprocessError, FileNotFoundError):
            logger.warning("Python3 is not available")
            self.available_languages["python"] = False

        # Check Node.js
        try:
            result = subprocess.run(["/home/loay-ahmed/.nvm/versions/node/v22.17.0/bin/node", "--version"], check=True, capture_output=True, text=True)
            self.available_languages["javascript"] = True
            logger.info(f"Node.js available: {result.stdout.strip()}")
        except (subprocess.SubprocessError, FileNotFoundError):
            logger.warning("Node.js is not available")
            self.available_languages["javascript"] = False

        # Check GCC
        try:
            result = subprocess.run(["gcc", "--version"], check=True, capture_output=True, text=True)
            self.available_languages["cpp"] = True
            logger.info(f"GCC available: {result.stdout.splitlines()[0]}")
        except (subprocess.SubprocessError, FileNotFoundError):
            logger.warning("GCC is not available")
            self.available_languages["cpp"] = False


    def _handle_error_readonly_files(self, func, path, exc_info):
        """Handle permission errors when removing temporary files."""
        if isinstance(exc_info[1], PermissionError):
            try:
                os.chmod(path, stat.S_IWRITE)
                func(path)
            except Exception as e:
                logger.warning(f"Failed to remove temporary file {path}: {e}")
        else:
            logger.warning(f"Failed to remove temporary file {path}: {exc_info[1]}")

    def _safe_temp_dir(self):
        """Create a temporary directory with safe cleanup."""
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
                if isinstance(exc_info[1], PermissionError):
                    try:
                        os.chmod(path, stat.S_IWRITE)
                        func(path)
                    except Exception as e:
                        logger.warning(f"Failed to remove temporary file {path}: {e}")
                else:
                    logger.warning(f"Failed to remove temporary file {path}: {exc_info[1]}")

        return SafeTempDir(prefix="code_execution_")

    def execute_code_with_tests(self, code: str, language: str, test_cases: List[Dict],
                               timeout: int = DEFAULT_TIMEOUT) -> Dict[str, Any]:
        """Execute code with test cases and return formatted results for API."""
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

    def execute_code(self, code: str, language: str, test_cases: List[Dict],
                     timeout: int = DEFAULT_TIMEOUT) -> List[Dict]:
        """Execute code with the given test cases locally."""
        language = language.lower()

        # Check if language is supported and available
        if language not in self.available_languages:
            return [{
                "test_case_id": "error",
                "passed": False,
                "actual_output": "",
                "expected_output": "",
                "execution_time": 0.0,
                "error_message": f"Language {language} not supported. Supported languages: {', '.join(self.available_languages.keys())}"
            }]

        if not self.available_languages[language]:
            return [{
                "test_case_id": "error",
                "passed": False,
                "actual_output": "",
                "expected_output": "",
                "execution_time": 0.0,
                "error_message": f"Compiler/interpreter for {language} is not available on this system"
            }]

        try:
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

                    # Run the code locally
                    results = self._run_locally(language, temp_dir, timeout)

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
        """Write code to a file with the appropriate extension."""
        extensions = {
            "python": ".py",
            "javascript": ".js",
            "cpp": ".cpp"
        }

        ext = extensions.get(language, ".txt")
        file_name = f"solution{ext}"
        file_path = os.path.join(temp_dir, file_name)

        # For JavaScript, ensure functions are exported
        if language == "javascript":
            modified_code = self._ensure_js_exports(code)
            with open(file_path, "w") as f:
                f.write(modified_code)
        else:
            with open(file_path, "w") as f:
                f.write(code)

        return file_path, file_name

    def _ensure_js_exports(self, code: str) -> str:
        """Ensure JavaScript functions are properly exported."""
        # Check if there are already exports
        if "module.exports" in code or "exports." in code or "export " in code:
            return code

        # Find function declarations and variable assignments to functions
        import re

        # Pattern to match function declarations and variable assignments to functions
        function_patterns = [
            r'function\s+(\w+)\s*\(',  # function name()
            r'var\s+(\w+)\s*=\s*function',  # var name = function
            r'let\s+(\w+)\s*=\s*function',  # let name = function
            r'const\s+(\w+)\s*=\s*function',  # const name = function
            r'(\w+)\s*=\s*function',  # name = function
            r'const\s+(\w+)\s*=\s*\([^)]*\)\s*=>', # const name = () =>
            r'let\s+(\w+)\s*=\s*\([^)]*\)\s*=>', # let name = () =>
            r'var\s+(\w+)\s*=\s*\([^)]*\)\s*=>', # var name = () =>
        ]

        function_names = []
        for pattern in function_patterns:
            matches = re.findall(pattern, code)
            function_names.extend(matches)

        # Remove duplicates while preserving order
        seen = set()
        unique_functions = []
        for name in function_names:
            if name not in seen:
                seen.add(name)
                unique_functions.append(name)

        if unique_functions:
            # Add exports at the end
            exports_code = "\n\n// Auto-generated exports\n"
            if len(unique_functions) == 1:
                exports_code += f"module.exports = {unique_functions[0]};\n"
            else:
                exports_code += "module.exports = {\n"
                for func_name in unique_functions:
                    exports_code += f"    {func_name},\n"
                exports_code += "};\n"

            return code + exports_code

        return code

    def _write_test_runner(self, language: str, temp_dir: str, code_file_name: str) -> str:
        """Write a test runner script for the specified language."""
        if language == "python":
            return self._write_python_test_runner(temp_dir, code_file_name)
        elif language == "javascript":
            return self._write_javascript_test_runner(temp_dir, code_file_name)
        elif language == "cpp":
            return self._write_cpp_test_runner(temp_dir, code_file_name)
        else:
            logger.warning(f"No specific test runner for {language}, defaulting to Python")
            return self._write_python_test_runner(temp_dir, code_file_name)

    def _write_python_test_runner(self, temp_dir: str, code_file_name: str) -> str:
        """Write a Python test runner script."""
        runner_path = os.path.join(temp_dir, "run_tests.py")

        python_test_runner = f"""
import json
import time
import sys
import importlib.util
import traceback
import inspect

# Load the test cases
with open('test_cases.json', 'r') as f:
    test_cases = json.load(f)

# Import the solution module
spec = importlib.util.spec_from_file_location("solution", "{code_file_name}")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

# Get all functions and classes from the solution module
solution_functions = {{name: func for name, func in solution.__dict__.items()
                     if callable(func) and not name.startswith('__')}}

# Separate functions and classes
functions = {{name: func for name, func in solution_functions.items() if inspect.isfunction(func)}}
classes = {{name: cls for name, cls in solution_functions.items() if inspect.isclass(cls)}}

results = []

for i, test_case in enumerate(test_cases):
    test_id = f"test_{{i}}"
    input_value = test_case.get("input", "")
    expected_output = test_case.get("expected_output", "")
    function_name = test_case.get("function_name", "")

    # Find the function to test
    func = None
    
    # First, try to find by function name
    if function_name and function_name in functions:
        func = functions[function_name]
    # If function name is specified but not found in functions, check classes
    elif function_name and function_name in classes:
        # Instantiate the class and look for the method
        try:
            cls = classes[function_name]
            instance = cls()
            # Look for common method names or the specified function name
            if hasattr(instance, function_name.lower()):
                func = getattr(instance, function_name.lower())
            elif hasattr(instance, 'solve'):
                func = getattr(instance, 'solve')
            elif hasattr(instance, 'solution'):
                func = getattr(instance, 'solution')
            else:
                # Get the first non-private method
                methods = [method for method in dir(instance) 
                          if callable(getattr(instance, method)) and not method.startswith('_')]
                if methods:
                    func = getattr(instance, methods[0])
        except Exception as e:
            pass
    # If we have exactly one function, use it
    elif len(functions) == 1:
        func = next(iter(functions.values()))
    # If we have exactly one class, instantiate it and find a method
    elif len(classes) == 1 and len(functions) == 0:
        try:
            cls = next(iter(classes.values()))
            instance = cls()
            # Look for common method names
            if hasattr(instance, 'solve'):
                func = getattr(instance, 'solve')
            elif hasattr(instance, 'solution'):
                func = getattr(instance, 'solution')
            else:
                # Get the first non-private method
                methods = [method for method in dir(instance) 
                          if callable(getattr(instance, method)) and not method.startswith('_')]
                if methods:
                    func = getattr(instance, methods[0])
        except Exception as e:
            pass
    # Try to match by description
    else:
        description = test_case.get("description", "").lower()
        for name, fn in functions.items():
            if name.lower() in description:
                func = fn
                break
        
        # If still not found, try classes
        if not func:
            for name, cls in classes.items():
                if name.lower() in description:
                    try:
                        instance = cls()
                        if hasattr(instance, 'solve'):
                            func = getattr(instance, 'solve')
                        elif hasattr(instance, 'solution'):
                            func = getattr(instance, 'solution')
                        else:
                            methods = [method for method in dir(instance) 
                                      if callable(getattr(instance, method)) and not method.startswith('_')]
                            if methods:
                                func = getattr(instance, methods[0])
                        break
                    except Exception as e:
                        continue
        
        # Last resort: use the first available function or class method
        if not func:
            if functions:
                func = next(iter(functions.values()))
            elif classes:
                try:
                    cls = next(iter(classes.values()))
                    instance = cls()
                    if hasattr(instance, 'solve'):
                        func = getattr(instance, 'solve')
                    elif hasattr(instance, 'solution'):
                        func = getattr(instance, 'solution')
                    else:
                        methods = [method for method in dir(instance) 
                                  if callable(getattr(instance, method)) and not method.startswith('_')]
                        if methods:
                            func = getattr(instance, methods[0])
                except Exception as e:
                    pass

    if not func:
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
        sig = inspect.signature(func)
        num_params = len(sig.parameters)

        # Handle different input formats
        if isinstance(input_value, str):
            if ',' in input_value and not (input_value.startswith('[') and input_value.endswith(']')):
                parts = []
                current_part = ""
                bracket_count = 0

                for char in input_value:
                    if char == '[':
                        bracket_count += 1
                    elif char == ']':
                        bracket_count -= 1
                    elif char == ',' and bracket_count == 0:
                        parts.append(current_part.strip())
                        current_part = ""
                        continue
                    current_part += char

                if current_part.strip():
                    parts.append(current_part.strip())

                parsed_args = []
                for part in parts:
                    if part.startswith('[') and part.endswith(']'):
                        try:
                            parsed_args.append(json.loads(part))
                        except json.JSONDecodeError:
                            parsed_args.append(part)
                    else:
                        try:
                            parsed_args.append(int(part))
                        except ValueError:
                            try:
                                parsed_args.append(float(part))
                            except ValueError:
                                if part.lower() in ['true', 'false']:
                                    parsed_args.append(part.lower() == 'true')
                                else:
                                    if part.startswith('"') and part.endswith('"'):
                                        parsed_args.append(part[1:-1])
                                    else:
                                        parsed_args.append(part)

                parsed_input = parsed_args
            elif input_value.startswith('[') and input_value.endswith(']'):
                try:
                    parsed_input = json.loads(input_value)
                except json.JSONDecodeError:
                    parsed_input = input_value
            else:
                parsed_input = input_value
        else:
            parsed_input = input_value

        # Execute the function
        start_time = time.time()

        if isinstance(parsed_input, list) and not isinstance(input_value, list):
            if len(parsed_input) == num_params:
                result = func(*parsed_input)
            elif num_params == 1:
                result = func(parsed_input)
            else:
                result = func(*parsed_input)
        elif isinstance(parsed_input, list) and num_params == 1:
            result = func(parsed_input)
        elif isinstance(parsed_input, list):
            result = func(*parsed_input)
        else:
            result = func(parsed_input)

        end_time = time.time()
        execution_time = (end_time - start_time) * 1000

        if isinstance(result, list):
            actual_output = json.dumps(result, separators=(',', ':'))
        else:
            actual_output = str(result)

        expected_str = str(expected_output).strip()
        if expected_str.startswith('[') and expected_str.endswith(']'):
            try:
                expected_parsed = json.loads(expected_str)
                expected_normalized = json.dumps(expected_parsed, separators=(',', ':'))
            except json.JSONDecodeError:
                expected_normalized = expected_str
        else:
            expected_normalized = expected_str

        passed = actual_output.strip() == expected_normalized.strip()

        results.append({{
            "test_case_id": test_id,
            "passed": passed,
            "actual_output": actual_output,
            "expected_output": expected_output,
            "execution_time": execution_time,
            "memory_usage": 0.0,
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
        """Write a JavaScript test runner script."""
        runner_path = os.path.join(temp_dir, "run_tests.js")

        js_test_runner = f"""
const fs = require('fs');
let solution;

try {{
    solution = require(`./{code_file_name}`);
}} catch (e) {{
    const errorResults = [{{
        test_case_id: "error",
        passed: false,
        actual_output: "",
        expected_output: "",
        execution_time: 0.0,
        error_message: `Error loading solution module: ${{e.toString()}}`
    }}];

    fs.writeFileSync('./results.json', JSON.stringify(errorResults, null, 2));
    process.exit(1);
}}

let testCases;
try {{
    const testCasesData = fs.readFileSync('./test_cases.json', 'utf8');
    testCases = JSON.parse(testCasesData);
}} catch (e) {{
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

// Enhanced function discovery
const solutionFunctions = [];

// Check if solution is a function itself
if (typeof solution === 'function') {{
    solutionFunctions.push({{ name: 'default', func: solution }});
}}

// Check for exported functions
if (typeof solution === 'object' && solution !== null) {{
    Object.keys(solution).forEach(key => {{
        if (typeof solution[key] === 'function') {{
            solutionFunctions.push({{ name: key, func: solution[key] }});
        }}
    }});
}}

// Check for module.exports patterns
if (solution.default && typeof solution.default === 'function') {{
    solutionFunctions.push({{ name: 'default', func: solution.default }});
}}

const results = [];

for (let i = 0; i < testCases.length; i++) {{
    const testCase = testCases[i];
    const testId = `test_${{i}}`;
    const inputValue = testCase.input || "";
    const expectedOutput = testCase.expected_output || "";
    const functionName = testCase.function_name || "";

    let func;
    let funcName = "";

    // Function discovery strategy
    if (functionName) {{
        // Try exact match first
        const exactMatch = solutionFunctions.find(f => f.name === functionName);
        if (exactMatch) {{
            func = exactMatch.func;
            funcName = exactMatch.name;
        }}
        // Try case-insensitive match
        if (!func) {{
            const caseMatch = solutionFunctions.find(f => 
                f.name.toLowerCase() === functionName.toLowerCase());
            if (caseMatch) {{
                func = caseMatch.func;
                funcName = caseMatch.name;
            }}
        }}
    }}

    // If no specific function name or not found, use heuristics
    if (!func && solutionFunctions.length === 1) {{
        func = solutionFunctions[0].func;
        funcName = solutionFunctions[0].name;
    }} else if (!func && solutionFunctions.length > 1) {{
        // Try to find by description
        if (testCase.description) {{
            const descMatch = solutionFunctions.find(f =>
                testCase.description.toLowerCase().includes(f.name.toLowerCase()));
            if (descMatch) {{
                func = descMatch.func;
                funcName = descMatch.name;
            }}
        }}
        
        // Default to first function if still not found
        if (!func) {{
            func = solutionFunctions[0].func;
            funcName = solutionFunctions[0].name;
        }}
    }}

    if (!func) {{
        const availableFunctions = solutionFunctions.map(f => f.name).join(', ');
        results.push({{
            test_case_id: testId,
            passed: false,
            actual_output: "",
            expected_output: "",
            execution_time: 0.0,
            error_message: `No suitable function found. Available functions: [${{availableFunctions}}]. Looking for: ${{functionName || 'any function'}}`
        }});
        continue;
    }}

    try {{
        let parsedInput = inputValue;
        if (typeof inputValue === 'string' && inputValue.startsWith('[') && inputValue.endsWith(']')) {{
            try {{
                parsedInput = JSON.parse(inputValue);
            }} catch (e) {{
                // Keep as string if parsing fails
            }}
        }}

        const startTime = Date.now();

        let result;
        let actualOutput;
        
        if (Array.isArray(parsedInput)) {{
            // Create a copy of the input for in-place modification functions
            const inputCopy = JSON.parse(JSON.stringify(parsedInput));
            
            if (func.length === 1) {{
                result = func(inputCopy);
            }} else {{
                result = func(...inputCopy);
            }}
            
            // If the function returns undefined but we have an array input,
            // the function might be modifying the array in-place
            if (result === undefined && Array.isArray(inputCopy)) {{
                actualOutput = JSON.stringify(inputCopy);
            }} else {{
                actualOutput = String(result);
            }}
        }} else {{
            result = func(parsedInput);
            actualOutput = String(result);
        }}

        const endTime = Date.now();
        const executionTime = endTime - startTime;

        const passed = actualOutput.trim() === String(expectedOutput).trim();

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

fs.writeFileSync('./results.json', JSON.stringify(results, null, 2));
"""

        with open(runner_path, "w") as f:
            f.write(js_test_runner)

        return runner_path

    def _write_cpp_test_runner(self, temp_dir: str, code_file_name: str) -> str:
        """Write a C++ test runner script."""
        runner_path = os.path.join(temp_dir, "test_runner.cpp")

        cpp_test_runner = f"""#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <chrono>
#include <algorithm>

// Simple JSON parsing helpers
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

// Include user's solution
"""

        # Read and append the user's code
        code_file_path = os.path.join(temp_dir, code_file_name)
        if os.path.exists(code_file_path):
            with open(code_file_path, "r") as code_file:
                user_code = code_file.read()
                cpp_test_runner += user_code

        cpp_test_runner += """
int main() {
    std::ifstream file("test_cases.json");
    std::string content((std::istreambuf_iterator<char>(file)),
                        std::istreambuf_iterator<char>());
    
    std::cout << "[" << std::endl;
    
    // Simple test case execution (you'll need to customize this based on your test format)
    // This is a basic example - you may need to enhance JSON parsing
    
    std::cout << "]" << std::endl;
    
    return 0;
}
"""

        with open(runner_path, "w") as f:
            f.write(cpp_test_runner)

        return runner_path

    def _run_locally(self, language: str, temp_dir: str, timeout: int) -> List[Dict]:
        """Run code locally using installed compilers/interpreters."""
        try:
            if language == "python":
                cmd = ["python3", "run_tests.py"]
            elif language == "javascript":
                cmd = ["/home/loay-ahmed/.nvm/versions/node/v22.17.0/bin/node", "run_tests.js"]
            elif language == "cpp":
                # First compile
                compile_cmd = ["gcc", "-o", "test_runner", "test_runner.cpp", "-lstdc++"]
                compile_result = subprocess.run(
                    compile_cmd,
                    cwd=temp_dir,
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )

                if compile_result.returncode != 0:
                    return [{
                        "test_case_id": "compile_error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": f"Compilation failed: {compile_result.stderr}"
                    }]

                cmd = ["./test_runner"]
            else:
                return [{
                    "test_case_id": "error",
                    "passed": False,
                    "actual_output": "",
                    "expected_output": "",
                    "execution_time": 0.0,
                    "error_message": f"Unsupported language: {language}"
                }]

            # Run the command
            result = subprocess.run(
                cmd,
                cwd=temp_dir,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            if result.returncode != 0:
                return [{
                    "test_case_id": "runtime_error",
                    "passed": False,
                    "actual_output": "",
                    "expected_output": "",
                    "execution_time": 0.0,
                    "error_message": f"Runtime error: {result.stderr}"
                }]

            # Read results from file
            results_path = os.path.join(temp_dir, "results.json")
            if os.path.exists(results_path):
                with open(results_path, "r") as f:
                    return json.load(f)
            else:
                # If no results file, try to parse stdout for C++
                if language == "cpp" and result.stdout:
                    try:
                        return json.loads(result.stdout)
                    except json.JSONDecodeError:
                        pass

                return [{
                    "test_case_id": "error",
                    "passed": False,
                    "actual_output": "",
                    "expected_output": "",
                    "execution_time": 0.0,
                    "error_message": "No results file generated"
                }]

        except subprocess.TimeoutExpired:
            return [{
                "test_case_id": "timeout",
                "passed": False,
                "actual_output": "",
                "expected_output": "",
                "execution_time": timeout * 1000,
                "error_message": f"Execution timed out after {timeout} seconds"
            }]
        except Exception as e:
            return [{
                "test_case_id": "error",
                "passed": False,
                "actual_output": "",
                "expected_output": "",
                "execution_time": 0.0,
                "error_message": f"Execution error: {str(e)}"
            }]
