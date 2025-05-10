"""
Test script to verify that array inputs are handled correctly.
"""
import os
import sys
import json

# Add the parent directory to the path so we can import the server modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.services.code_execution_service import CodeExecutionService

def test_find_duplicates():
    """Test that the find_duplicates function works correctly."""
    print("Testing find_duplicates function...")
    
    # Create a code execution service
    service = CodeExecutionService()
    
    # Force fallback execution
    service.docker_available = False
    
    # Python code for find_duplicates
    code = """
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return sorted(list(duplicates))
"""
    
    # Test cases
    test_cases = [
        {
            "input": "[1, 2, 3, 4]",
            "expected_output": "[]",
            "function_name": "find_duplicates"
        },
        {
            "input": "[1, 2, 2, 3, 4, 4]",
            "expected_output": "[2, 4]",
            "function_name": "find_duplicates"
        },
        {
            "input": "[1, 1, 1, 1]",
            "expected_output": "[1]",
            "function_name": "find_duplicates"
        }
    ]
    
    # Execute the code
    results = service.execute_code(code, "python", test_cases)
    
    # Print the results
    print(json.dumps(results, indent=2))
    
    # Check if all tests passed
    all_passed = all(result.get("passed", False) for result in results)
    print(f"All tests passed: {all_passed}")
    
    return all_passed

if __name__ == "__main__":
    # Run the test
    success = test_find_duplicates()
    
    # Exit with success if the test passed
    sys.exit(0 if success else 1)
