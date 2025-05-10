"""
Additional test runners for the code execution service.
"""
import os
import json
import logging

logger = logging.getLogger(__name__)

def _write_go_test_runner(self, temp_dir: str, code_file_name: str) -> str:
    """Write a Go test runner script.

    Args:
        temp_dir: The temporary directory
        code_file_name: The name of the code file

    Returns:
        Path to the test runner script
    """
    # Create a Go module
    module_path = os.path.join(temp_dir, "go.mod")
    with open(module_path, "w") as f:
        f.write("module solution\n\ngo 1.18\n")

    # Create a main.go file that will run the tests
    runner_path = os.path.join(temp_dir, "main.go")

    # Write a simple Go test runner that doesn't use struct tags
    with open(runner_path, "w") as f:
        f.write("""
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"time"
)

func main() {
	// Read test cases from file
	testCasesBytes, err := ioutil.ReadFile("test_cases.json")
	if err != nil {
		fmt.Println("Error reading test cases file:", err)
		os.Exit(1)
	}

	// Parse test cases
	var testCases []map[string]interface{}
	err = json.Unmarshal(testCasesBytes, &testCases)
	if err != nil {
		fmt.Println("Error parsing test cases:", err)
		os.Exit(1)
	}

	// Run tests
	results := make([]map[string]interface{}, 0, len(testCases))

	for i, tc := range testCases {
		testID := fmt.Sprintf("test_%d", i)

		// Get test case data
		input := tc["input"]
		expectedOutput := tc["expected_output"]
		functionName, _ := tc["function_name"].(string)

		// Execute the function
		var result interface{}
		var errorMsg *string

		startTime := time.Now()

		// Call the appropriate function based on the test case
		// This is where you would add your solution functions
		msg := fmt.Sprintf("Function %s not found", functionName)
		errorMsg = &msg

		executionTime := float64(time.Since(startTime).Microseconds()) / 1000.0 // Convert to ms

		// Convert result to string for comparison
		var actualOutput interface{} = ""
		if errorMsg == nil {
			actualOutput = fmt.Sprintf("%v", result)
		}

		// Check if the output matches the expected output
		expectedOutputStr := fmt.Sprintf("%v", expectedOutput)
		passed := errorMsg == nil && fmt.Sprintf("%v", actualOutput) == expectedOutputStr

		// Add the result
		resultMap := map[string]interface{}{
			"test_case_id":     testID,
			"passed":           passed,
			"actual_output":    actualOutput,
			"expected_output":  expectedOutput,
			"execution_time":   executionTime,
			"memory_usage":     0.0, // Memory profiling not implemented
			"error_message":    errorMsg,
		}
		results = append(results, resultMap)
	}

	// Write results to file
	resultsBytes, err := json.MarshalIndent(results, "", "  ")
	if err != nil {
		fmt.Println("Error marshaling results:", err)
		os.Exit(1)
	}

	err = ioutil.WriteFile("results.json", resultsBytes, 0644)
	if err != nil {
		fmt.Println("Error writing results file:", err)
		os.Exit(1)
	}
}
""")

    # Create a solution.go file that imports the user's code
    solution_path = os.path.join(temp_dir, "solution.go")
    with open(solution_path, "w") as f:
        f.write("""
package main

// Import the user's code
""" + f"// {code_file_name} should be in the same directory")

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

    # Create a simplified Ruby test runner script
    with open(runner_path, "w") as f:
        f.write("""
require 'json'

# Load test cases
test_cases = JSON.parse(File.read('test_cases.json'))

results = []

test_cases.each_with_index do |test_case, i|
  test_id = "test_#{i}"
  input_value = test_case['input'] || ""
  expected_output = test_case['expected_output'] || ""
  function_name = test_case['function_name'] || ""

  # For now, just return an error for all tests
  results << {
    'test_case_id' => test_id,
    'passed' => false,
    'actual_output' => "",
    'expected_output' => expected_output,
    'execution_time' => 0.0,
    'memory_usage' => 0.0,
    'error_message' => "Ruby execution not fully implemented yet"
  }
end

# Write results to file
File.write('results.json', JSON.pretty_generate(results))
""")

    # Create a file to load the solution
    solution_loader_path = os.path.join(temp_dir, "solution_loader.rb")
    with open(solution_loader_path, "w") as f:
        f.write(f"""
# This file will load the solution
require_relative './{os.path.splitext(code_file_name)[0]}'
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
    # Create a simple C++ test runner that just returns errors for now
    runner_path = os.path.join(temp_dir, "test_runner.cpp")

    with open(runner_path, "w") as f:
        f.write("""
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {
    try {
        // Read test cases from file
        std::ifstream test_cases_file("test_cases.json");
        if (!test_cases_file.is_open()) {
            std::cerr << "Error opening test cases file" << std::endl;
            return 1;
        }

        json test_cases_json;
        test_cases_file >> test_cases_json;
        test_cases_file.close();

        // Create results array
        json results = json::array();

        // For each test case, create a result
        for (size_t i = 0; i < test_cases_json.size(); ++i) {
            const auto& tc = test_cases_json[i];

            json result;
            result["test_case_id"] = "test_" + std::to_string(i);
            result["passed"] = false;
            result["actual_output"] = "";
            result["expected_output"] = tc.value("expected_output", "");
            result["execution_time"] = 0.0;
            result["memory_usage"] = 0.0;
            result["error_message"] = "C++ execution not fully implemented yet";

            results.push_back(result);
        }

        // Write results to file
        std::ofstream results_file("results.json");
        results_file << results.dump(4);
        results_file.close();

        return 0;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}
""")

    # Create a CMakeLists.txt file
    cmake_path = os.path.join(temp_dir, "CMakeLists.txt")
    with open(cmake_path, "w") as f:
        f.write(f"""
cmake_minimum_required(VERSION 3.10)
project(CodeExecution)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(test_runner test_runner.cpp)
""")

    # Create a Dockerfile for building and running the C++ code
    dockerfile_path = os.path.join(temp_dir, "Dockerfile")
    with open(dockerfile_path, "w") as f:
        f.write("""
FROM gcc:latest

WORKDIR /app

# Install CMake and nlohmann/json
RUN apt-get update && apt-get install -y \
    cmake \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget -O json.hpp https://github.com/nlohmann/json/releases/download/v3.11.2/json.hpp \
    && mkdir -p /usr/include/nlohmann \
    && mv json.hpp /usr/include/nlohmann/

# Copy the source files
COPY . /app/

# Build the project
RUN mkdir -p build && cd build && cmake .. && make

# Run the tests
CMD ["./build/test_runner"]
""")

    return runner_path
