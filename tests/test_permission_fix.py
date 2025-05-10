"""
Test script to verify that the permission error fix works.
"""
import os
import sys
import json
import tempfile
import shutil

# Add the parent directory to the path so we can import the server modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.services.code_execution_service import CodeExecutionService

def test_permission_fix():
    """Test that the permission error fix works."""
    print("Testing permission error fix...")
    
    # Create a code execution service
    service = CodeExecutionService()
    
    # Force fallback execution
    service.docker_available = False
    
    # Python code that creates a __pycache__ directory
    code = """
def reverse_string(s):
    # This function will be compiled to a .pyc file
    return s[::-1]

# Import a module to trigger __pycache__ creation
import json
"""
    
    # Test cases
    test_cases = [
        {
            "input": "hello",
            "expected_output": "olleh",
            "function_name": "reverse_string"
        }
    ]
    
    # Execute the code multiple times to ensure the cleanup works
    for i in range(5):
        print(f"Execution {i+1}...")
        results = service.execute_code(code, "python", test_cases)
        
        # Print the results
        print(json.dumps(results, indent=2))
        
        # Check if all tests passed
        all_passed = all(result.get("passed", False) for result in results)
        print(f"All tests passed: {all_passed}")
        
        if not all_passed:
            print("Test failed!")
            return False
    
    print("All executions completed successfully.")
    return True

if __name__ == "__main__":
    # Run the test
    success = test_permission_fix()
    
    # Exit with success if the test passed
    sys.exit(0 if success else 1)
