"""
Service for executing code in a secure Docker environment.
"""
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
        "cpp": "gcc:latest",
        "csharp": "mcr.microsoft.com/dotnet/sdk:6.0"
    }

    def __init__(self):
        """Initialize the code execution service."""
        # Check if Docker is available
        try:
            subprocess.run(["docker", "--version"], check=True, capture_output=True)
            self.docker_available = True
        except (subprocess.SubprocessError, FileNotFoundError):
            logger.warning("Docker is not available. Falling back to local execution.")
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

    def execute_code(self, code: str, language: str, test_cases: List[Dict],
                     timeout: int = DEFAULT_TIMEOUT) -> List[Dict]:
        """Execute code with the given test cases.

        Args:
            code: The code to execute
            language: The programming language (python, javascript, java, etc.)
            test_cases: List of test cases with input and expected output
            timeout: Maximum execution time in seconds

        Returns:
            List of test case results
        """
        language = language.lower()

        if not self.docker_available:
            logger.warning("Docker not available. Using fallback execution method.")
            return self._fallback_execute(code, language, test_cases, timeout)

        if language not in self.DOCKER_IMAGES:
            logger.warning(f"Language {language} not supported. Falling back to Python.")
            language = "python"

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
            "csharp": ".cs"
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
        else:
            # Default to Python
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

results = []

for i, test_case in enumerate(test_cases):
    test_id = f"test_{{i}}"
    input_value = test_case.get("input", "")
    expected_output = test_case.get("expected_output", "")
    function_name = test_case.get("function_name", "")

    # Find the function to test
    func = None
    if function_name and function_name in solution_functions:
        func = solution_functions[function_name]
    elif len(solution_functions) == 1:
        # If only one function, use that
        func = next(iter(solution_functions.values()))
    else:
        # Try to find a function with a name that matches the test case
        for name, fn in solution_functions.items():
            if name.lower() in test_case.get("description", "").lower():
                func = fn
                break
        else:
            # Default to the first function
            if solution_functions:
                func = next(iter(solution_functions.values()))

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
        # Parse input based on type
        parsed_input = input_value
        if isinstance(input_value, str) and input_value.startswith('[') and input_value.endswith(']'):
            try:
                parsed_input = json.loads(input_value)
            except json.JSONDecodeError:
                pass

        # Execute the function
        start_time = time.time()

        # Check if the function expects a single argument but we have a list
        import inspect
        sig = inspect.signature(func)

        if isinstance(parsed_input, list):
            # If the function takes a single argument and it's not a variable argument function
            if len(sig.parameters) == 1 and not any(p.kind == inspect.Parameter.VAR_POSITIONAL for p in sig.parameters.values()):
                # Pass the list as a single argument
                result = func(parsed_input)
            else:
                # Pass each element of the list as a separate argument
                result = func(*parsed_input)
        else:
            result = func(parsed_input)

        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to ms

        # Convert result to string for comparison
        actual_output = str(result)

        # Check if the output matches the expected output
        passed = actual_output.strip() == str(expected_output).strip()

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

        # Create the JavaScript test runner script
        js_test_runner = f"""
const fs = require('fs');
const solution = require(`./{code_file_name}`);

// Load test cases
const testCases = JSON.parse(fs.readFileSync('./test_cases.json', 'utf8'));

// Get all exported functions from the solution
const solutionFunctions = Object.keys(solution)
    .filter(key => typeof solution[key] === 'function');

const results = [];

for (let i = 0; i < testCases.length; i++) {{
    const testCase = testCases[i];
    const testId = `test_${{i}}`;
    const inputValue = testCase.input || "";
    const expectedOutput = testCase.expected_output || "";
    const functionName = testCase.function_name || "";

    // Find the function to test
    let func;
    if (functionName && solution[functionName]) {{
        func = solution[functionName];
    }} else if (solutionFunctions.length === 1) {{
        // If only one function, use that
        func = solution[solutionFunctions[0]];
    }} else {{
        // Try to find a function with a name that matches the test case
        const matchingFunc = solutionFunctions.find(name =>
            testCase.description && testCase.description.toLowerCase().includes(name.toLowerCase()));

        if (matchingFunc) {{
            func = solution[matchingFunc];
        }} else if (solutionFunctions.length > 0) {{
            // Default to the first function
            func = solution[solutionFunctions[0]];
        }}
    }}

    if (!func) {{
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

    try {{
        // Parse input based on type
        let parsedInput = inputValue;
        if (typeof inputValue === 'string' && inputValue.startsWith('[') && inputValue.endsWith(']')) {{
            try {{
                parsedInput = JSON.parse(inputValue);
            }} catch (e) {{
                // Keep as string if parsing fails
            }}
        }}

        // Execute the function
        const startTime = Date.now();

        let result;
        if (Array.isArray(parsedInput)) {{
            // Check if the function expects a single argument
            // In JavaScript, we can check the number of parameters the function expects
            if (func.length === 1) {{
                // Pass the array as a single argument
                result = func(parsedInput);
            }} else {{
                // Pass each element of the array as a separate argument
                result = func(...parsedInput);
            }}
        }} else {{
            result = func(parsedInput);
        }}

        const endTime = Date.now();
        const executionTime = endTime - startTime;

        // Convert result to string for comparison
        const actualOutput = String(result);

        // Check if the output matches the expected output
        const passed = actualOutput.trim() === String(expectedOutput).trim();

        results.push({{
            test_case_id: testId,
            passed: passed,
            actual_output: actualOutput,
            expected_output: expectedOutput,
            execution_time: executionTime,
            memory_usage: 0.0,  // Memory profiling not implemented
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

// Write results to file
fs.writeFileSync('./results.json', JSON.stringify(results, null, 2));
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

        # Create the Java test runner script
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
        try {{
            // Load test cases
            JSONParser parser = new JSONParser();
            JSONArray testCases = (JSONArray) parser.parse(new FileReader("test_cases.json"));

            // Create instance of solution class
            Class<?> solutionClass = Class.forName("{class_name}");
            Object solutionInstance = solutionClass.getDeclaredConstructor().newInstance();

            // Get all methods from the solution class
            Method[] methods = solutionClass.getDeclaredMethods();

            JSONArray results = new JSONArray();

            for (int i = 0; i < testCases.size(); i++) {{
                JSONObject testCase = (JSONObject) testCases.get(i);
                String testId = "test_" + i;
                String inputValue = testCase.containsKey("input") ? testCase.get("input").toString() : "";
                String expectedOutput = testCase.containsKey("expected_output") ? testCase.get("expected_output").toString() : "";
                String functionName = testCase.containsKey("function_name") ? testCase.get("function_name").toString() : "";

                // Find the method to test
                Method methodToTest = null;

                if (!functionName.isEmpty()) {{
                    // Try to find by name
                    for (Method method : methods) {{
                        if (method.getName().equals(functionName)) {{
                            methodToTest = method;
                            break;
                        }}
                    }}
                }}

                if (methodToTest == null && methods.length == 1) {{
                    // If only one method, use that
                    methodToTest = methods[0];
                }}

                if (methodToTest == null && testCase.containsKey("description")) {{
                    // Try to find a method with a name that matches the test case
                    String description = testCase.get("description").toString().toLowerCase();
                    for (Method method : methods) {{
                        if (description.contains(method.getName().toLowerCase())) {{
                            methodToTest = method;
                            break;
                        }}
                    }}
                }}

                if (methodToTest == null && methods.length > 0) {{
                    // Default to the first method
                    methodToTest = methods[0];
                }}

                if (methodToTest == null) {{
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

                    if (paramTypes.length == 1) {{
                        // Handle single parameter
                        if (paramTypes[0] == int.class || paramTypes[0] == Integer.class) {{
                            parsedInput = Integer.parseInt(inputValue);
                        }} else if (paramTypes[0] == double.class || paramTypes[0] == Double.class) {{
                            parsedInput = Double.parseDouble(inputValue);
                        }} else if (paramTypes[0] == boolean.class || paramTypes[0] == Boolean.class) {{
                            parsedInput = Boolean.parseBoolean(inputValue);
                        }} else if (paramTypes[0] == String.class) {{
                            // Already a string
                        }} else if (paramTypes[0].isArray()) {{
                            // TODO: Handle array parameters
                        }}
                    }}

                    // Execute the method
                    long startTime = System.currentTimeMillis();
                    Object result;

                    // Check if the input is a JSON array and the method expects an array
                    if (inputValue.startsWith("[") && inputValue.endsWith("]") &&
                        methodToTest.getParameterTypes().length == 1 &&
                        methodToTest.getParameterTypes()[0].isArray()) {{
                        // Parse the JSON array into a Java array
                        try {{
                            org.json.simple.JSONArray jsonArray = (org.json.simple.JSONArray) new org.json.simple.parser.JSONParser().parse(inputValue);
                            Object[] array = jsonArray.toArray();

                            // Create an array of the correct type
                            Class<?> componentType = methodToTest.getParameterTypes()[0].getComponentType();
                            Object typedArray = java.lang.reflect.Array.newInstance(componentType, array.length);

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
                            result = methodToTest.invoke(solutionInstance, typedArray);
                        }} catch (Exception e) {{
                            // If parsing fails, fall back to the original approach
                            result = methodToTest.invoke(solutionInstance, parsedInput);
                        }}
                    }} else {{
                        // Use the original approach
                        result = methodToTest.invoke(solutionInstance, parsedInput);
                    }}

                    long endTime = System.currentTimeMillis();
                    long executionTime = endTime - startTime;

                    // Convert result to string for comparison
                    String actualOutput = result != null ? result.toString() : "null";

                    // Check if the output matches the expected output
                    boolean passed = actualOutput.trim().equals(expectedOutput.trim());

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
            FileWriter file = new FileWriter("results.json");
            file.write(results.toJSONString());
            file.flush();
            file.close();

        }} catch (Exception e) {{
            e.printStackTrace();
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

        if language == "java":
            # For Java, we need to build a custom Docker image
            try:
                # Build the Docker image
                build_cmd = [
                    "docker", "build",
                    "-t", f"{container_name}_image",
                    temp_dir
                ]
                subprocess.run(build_cmd, check=True, capture_output=True, timeout=60)

                # Run the container
                run_cmd = [
                    "docker", "run",
                    "--name", container_name,
                    "--memory", self.MEMORY_LIMIT,
                    "--rm",
                    f"{container_name}_image"
                ]
                subprocess.run(run_cmd, check=True, capture_output=True, timeout=timeout)

                # Read the results
                results_path = os.path.join(temp_dir, "results.json")
                if os.path.exists(results_path):
                    with open(results_path, "r") as f:
                        return json.load(f)
                else:
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": "Failed to get results from Docker container"
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
            except subprocess.SubprocessError as e:
                return [{
                    "test_case_id": "error",
                    "passed": False,
                    "actual_output": "",
                    "expected_output": "",
                    "execution_time": 0.0,
                    "error_message": f"Docker execution error: {str(e)}"
                }]
        else:
            # For other languages, mount the directory and run the appropriate command
            try:
                cmd = []
                if language == "python":
                    cmd = ["python", "run_tests.py"]
                elif language == "javascript":
                    cmd = ["node", "run_tests.js"]
                else:
                    # Default to Python
                    cmd = ["python", "run_tests.py"]

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

                subprocess.run(run_cmd, check=True, capture_output=True, timeout=timeout)

                # Read the results
                results_path = os.path.join(temp_dir, "results.json")
                if os.path.exists(results_path):
                    with open(results_path, "r") as f:
                        return json.load(f)
                else:
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": "Failed to get results from Docker container"
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
            except subprocess.SubprocessError as e:
                return [{
                    "test_case_id": "error",
                    "passed": False,
                    "actual_output": "",
                    "expected_output": "",
                    "execution_time": 0.0,
                    "error_message": f"Docker execution error: {str(e)}"
                }]

    def _fallback_execute(self, code: str, language: str, test_cases: List[Dict],
                         timeout: int) -> List[Dict]:
        """Fallback execution method when Docker is not available.

        Args:
            code: The code to execute
            language: The programming language
            test_cases: List of test cases
            timeout: Maximum execution time in seconds

        Returns:
            List of test case results
        """
        # This is a simplified version that only works for Python
        if language.lower() != "python":
            return [{
                "test_case_id": f"test_{i}",
                "passed": False,
                "actual_output": "",
                "expected_output": tc.get("expected_output", ""),
                "execution_time": 0.0,
                "error_message": f"Fallback execution only supports Python, not {language}"
            } for i, tc in enumerate(test_cases)]

        try:
            # Create a temporary directory with safe cleanup
            with self._safe_temp_dir() as temp_dir:
                try:
                    # Write code to file
                    code_path = os.path.join(temp_dir, "solution.py")
                    with open(code_path, "w") as f:
                        f.write(code)

                    results = []

                    for i, test_case in enumerate(test_cases):
                        test_id = f"test_{i}"
                        input_value = test_case.get("input", "")
                        expected_output = test_case.get("expected_output", "")
                        function_name = test_case.get("function_name", "")

                        # Create a test script that doesn't import the solution module directly
                        # This avoids creating .pyc files
                        test_script = f"""
import sys
import time
import traceback
import importlib.util

try:
    # Import the solution module using importlib to avoid creating .pyc files
    spec = importlib.util.spec_from_file_location("solution", "{code_path}")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Find the function to test
    function_name = "{function_name}"
    if function_name and hasattr(solution, function_name):
        func = getattr(solution, function_name)
    else:
        # Get all functions from the module
        funcs = [getattr(solution, f) for f in dir(solution)
                if callable(getattr(solution, f)) and not f.startswith('__')]
        func = funcs[0] if funcs else None

    if not func:
        print("ERROR: No suitable function found")
        sys.exit(1)

    # Parse input
    input_value = "{input_value}"

    # Execute the function
    start_time = time.time()

    # Check if input is a JSON array
    try:
        if input_value.startswith('[') and input_value.endswith(']'):
            import json
            parsed_input = json.loads(input_value)

            # Check if the function expects a single argument
            import inspect
            sig = inspect.signature(func)

            if len(sig.parameters) == 1 and not any(p.kind == inspect.Parameter.VAR_POSITIONAL for p in sig.parameters.values()):
                # Pass the list as a single argument
                result = func(parsed_input)
            else:
                # Pass each element of the list as a separate argument
                result = func(*parsed_input)
        else:
            result = func(input_value)
    except (json.JSONDecodeError, AttributeError):
        # If parsing fails or input is not a string, use the original input
        result = func(input_value)

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to ms

    print(f"RESULT: {{result}}")
    print(f"EXECUTION_TIME: {{execution_time}}")
except Exception as e:
    print(f"ERROR: {{str(e)}}")
    print(traceback.format_exc())
"""

                        # Write the test script to a temporary file
                        test_path = os.path.join(temp_dir, f"test_{i}.py")
                        with open(test_path, "w") as f:
                            f.write(test_script)

                        # Run the test
                        try:
                            process = subprocess.run(
                                ["python", test_path],
                                capture_output=True,
                                text=True,
                                timeout=timeout
                            )

                            output = process.stdout
                            error = process.stderr

                            # Parse the output
                            result_match = re.search(r"RESULT: (.*)", output)
                            time_match = re.search(r"EXECUTION_TIME: ([\d.]+)", output)
                            error_match = re.search(r"ERROR: (.*)", output)

                            if result_match:
                                actual_output = result_match.group(1)
                                execution_time = float(time_match.group(1)) if time_match else 0.0
                                error_message = error_match.group(1) if error_match else None

                                # Check if the output matches the expected output
                                passed = actual_output.strip() == expected_output.strip()

                                results.append({
                                    "test_case_id": test_id,
                                    "passed": passed,
                                    "actual_output": actual_output,
                                    "expected_output": expected_output,
                                    "execution_time": execution_time,
                                    "memory_usage": 0.0,
                                    "error_message": error_message
                                })
                            else:
                                results.append({
                                    "test_case_id": test_id,
                                    "passed": False,
                                    "actual_output": "",
                                    "expected_output": expected_output,
                                    "execution_time": 0.0,
                                    "error_message": error or "Failed to execute test"
                                })
                        except subprocess.TimeoutExpired:
                            results.append({
                                "test_case_id": test_id,
                                "passed": False,
                                "actual_output": "",
                                "expected_output": expected_output,
                                "execution_time": timeout * 1000,
                                "error_message": f"Execution timed out after {timeout} seconds"
                            })
                        except Exception as e:
                            logger.error(f"Error running test {test_id}: {e}")
                            results.append({
                                "test_case_id": test_id,
                                "passed": False,
                                "actual_output": "",
                                "expected_output": expected_output,
                                "execution_time": 0.0,
                                "error_message": f"Error running test: {str(e)}"
                            })

                    return results
                except Exception as e:
                    logger.error(f"Error in fallback execution: {e}")
                    return [{
                        "test_case_id": "error",
                        "passed": False,
                        "actual_output": "",
                        "expected_output": "",
                        "execution_time": 0.0,
                        "error_message": f"Error in fallback execution: {str(e)}"
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
