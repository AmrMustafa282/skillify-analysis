#!/usr/bin/env python3
"""
Script to load professional data into the assessment database.
Creates 5 different tests and 50 solutions for each test.
"""

import os
import sys
import json
import random
import uuid
from datetime import datetime, timedelta
import argparse

# Add the parent directory to the path so we can import the server modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.services.database_service import DatabaseService
from server.services.analysis_service import AnalysisService

# Configure argument parser
parser = argparse.ArgumentParser(description='Load professional data into the assessment database')
parser.add_argument('--drop-existing', action='store_true', help='Drop existing collections before loading data')
args = parser.parse_args()

# Initialize services
db_service = DatabaseService()
analysis_service = AnalysisService(db_service)

# Function to generate MCQ questions for Python
def generate_python_mcq_questions(num_questions=50):
    python_mcq_questions = [
        {
            "order": 1,
            "type": "MCQ",
            "text": "What is the output of print(type([]))?",
            "options": {
                "choices": [
                    {"id": "q1_a", "text": "<class 'list'>"},
                    {"id": "q1_b", "text": "<class 'array'>"},
                    {"id": "q1_c", "text": "<class 'tuple'>"},
                    {"id": "q1_d", "text": "<class 'dict'>"}
                ]
            },
            "correctAnswer": {"value": "q1_a"}
        },
        {
            "order": 2,
            "type": "MCQ",
            "text": "Which of the following is mutable in Python?",
            "options": {
                "choices": [
                    {"id": "q2_a", "text": "String"},
                    {"id": "q2_b", "text": "Tuple"},
                    {"id": "q2_c", "text": "List"},
                    {"id": "q2_d", "text": "Integer"}
                ]
            },
            "correctAnswer": {"value": "q2_c"}
        }
    ]

    # Additional Python MCQ questions
    additional_questions = [
        {
            "text": "What does the 'self' keyword represent in a Python class?",
            "options": {
                "choices": [
                    {"id": "a", "text": "It refers to the class itself"},
                    {"id": "b", "text": "It refers to the instance of the class"},
                    {"id": "c", "text": "It is a reserved keyword for static methods"},
                    {"id": "d", "text": "It is used to access private variables"}
                ]
            },
            "correctAnswer": {"value": "b"}
        },
        {
            "text": "Which of the following is NOT a valid way to create a list in Python?",
            "options": {
                "choices": [
                    {"id": "a", "text": "my_list = []"},
                    {"id": "b", "text": "my_list = list()"},
                    {"id": "c", "text": "my_list = [i for i in range(10)]"},
                    {"id": "d", "text": "my_list = list.new()"}
                ]
            },
            "correctAnswer": {"value": "d"}
        },
        {
            "text": "What is the output of '3' + '4' in Python?",
            "options": {
                "choices": [
                    {"id": "a", "text": "7"},
                    {"id": "b", "text": "34"},
                    {"id": "c", "text": "'34'"},
                    {"id": "d", "text": "TypeError"}
                ]
            },
            "correctAnswer": {"value": "b"}
        },
        {
            "text": "Which of the following is used to handle exceptions in Python?",
            "options": {
                "choices": [
                    {"id": "a", "text": "try-catch"},
                    {"id": "b", "text": "try-except"},
                    {"id": "c", "text": "try-finally"},
                    {"id": "d", "text": "try-handle"}
                ]
            },
            "correctAnswer": {"value": "b"}
        },
        {
            "text": "What is the output of len('Hello World')?",
            "options": {
                "choices": [
                    {"id": "a", "text": "10"},
                    {"id": "b", "text": "11"},
                    {"id": "c", "text": "12"},
                    {"id": "d", "text": "Error"}
                ]
            },
            "correctAnswer": {"value": "b"}
        },
        {
            "text": "Which method is used to add an element to the end of a list?",
            "options": {
                "choices": [
                    {"id": "a", "text": "append()"},
                    {"id": "b", "text": "extend()"},
                    {"id": "c", "text": "insert()"},
                    {"id": "d", "text": "add()"}
                ]
            },
            "correctAnswer": {"value": "a"}
        },
        {
            "text": "What is the correct way to import a module named 'math' in Python?",
            "options": {
                "choices": [
                    {"id": "a", "text": "import math"},
                    {"id": "b", "text": "include math"},
                    {"id": "c", "text": "using math"},
                    {"id": "d", "text": "#include <math>"}
                ]
            },
            "correctAnswer": {"value": "a"}
        },
        {
            "text": "What is the output of 5 // 2 in Python?",
            "options": {
                "choices": [
                    {"id": "a", "text": "2.5"},
                    {"id": "b", "text": "2"},
                    {"id": "c", "text": "2.0"},
                    {"id": "d", "text": "Error"}
                ]
            },
            "correctAnswer": {"value": "b"}
        },
        {
            "text": "Which of the following is NOT a built-in data type in Python?",
            "options": {
                "choices": [
                    {"id": "a", "text": "list"},
                    {"id": "b", "text": "dictionary"},
                    {"id": "c", "text": "array"},
                    {"id": "d", "text": "tuple"}
                ]
            },
            "correctAnswer": {"value": "c"}
        },
        {
            "text": "What does the 'pass' statement do in Python?",
            "options": {
                "choices": [
                    {"id": "a", "text": "It skips the current iteration of a loop"},
                    {"id": "b", "text": "It terminates the program"},
                    {"id": "c", "text": "It does nothing and acts as a placeholder"},
                    {"id": "d", "text": "It passes control to another function"}
                ]
            },
            "correctAnswer": {"value": "c"}
        }
    ]

    # Generate more questions to reach the desired number
    for i in range(3, num_questions + 1):
        if i - 3 < len(additional_questions):
            # Use predefined questions first
            question = additional_questions[i - 3].copy()
        else:
            # Generate generic questions if we run out of predefined ones
            question = {
                "text": f"Python MCQ Question #{i}",
                "options": {
                    "choices": [
                        {"id": "a", "text": f"Option A for question {i}"},
                        {"id": "b", "text": f"Option B for question {i}"},
                        {"id": "c", "text": f"Option C for question {i}"},
                        {"id": "d", "text": f"Option D for question {i}"}
                    ]
                },
                "correctAnswer": {"value": random.choice(["a", "b", "c", "d"])}
            }

        # Add order and type
        question["order"] = i
        question["type"] = "MCQ"

        # Format the question ID in options
        for choice in question["options"]["choices"]:
            choice["id"] = f"q{i}_{choice['id']}"

        # Update correct answer with the new ID format
        old_correct = question["correctAnswer"]["value"]
        question["correctAnswer"]["value"] = f"q{i}_{old_correct}"

        python_mcq_questions.append(question)

    # Add an open-ended question at the end
    python_mcq_questions.append({
        "order": num_questions + 1,
        "type": "OPEN_ENDED",
        "text": "Explain the difference between a list and a tuple in Python.",
        "difficulty": "MEDIUM"
    })

    return python_mcq_questions

# Function to generate MCQ questions for JavaScript
def generate_javascript_mcq_questions(num_questions=50):
    # Similar implementation for JavaScript questions
    # (Implementation similar to Python but with JavaScript-specific questions)
    javascript_mcq_questions = []
    # Add implementation here
    return javascript_mcq_questions

# Function to generate MCQ questions for Java
def generate_java_mcq_questions(num_questions=50):
    # Similar implementation for Java questions
    # (Implementation similar to Python but with Java-specific questions)
    java_mcq_questions = []
    # Add implementation here
    return java_mcq_questions

# Function to generate MCQ questions for Data Structures
def generate_data_structures_mcq_questions(num_questions=50):
    # Similar implementation for Data Structures questions
    # (Implementation similar to Python but with Data Structures-specific questions)
    data_structures_mcq_questions = []
    # Add implementation here
    return data_structures_mcq_questions

# Function to generate MCQ questions for Algorithms
def generate_algorithms_mcq_questions(num_questions=50):
    # Similar implementation for Algorithms questions
    # (Implementation similar to Python but with Algorithms-specific questions)
    algorithms_mcq_questions = []
    # Add implementation here
    return algorithms_mcq_questions

# Test templates
TEST_TEMPLATES = [
    {
        "testId": "python-basics",
        "title": "Python Programming Basics",
        "description": "This assessment tests fundamental Python programming skills.",
        "duration": 60,
        "questions": generate_python_mcq_questions(),
        "codingQuestions": [
            {
                "order": 52,
                "title": "Reverse a String",
                "text": "Implement a function to reverse a string without using built-in reverse methods.",
                "language": "python",
                "starterCode": "def reverse_string(s):\n    # Your code here\n    pass",
                "solutionCode": "def reverse_string(s):\n    return s[::-1]",
                "testCases": [
                    {"input": "hello", "expected_output": "olleh", "weight": 0.3},
                    {"input": "", "expected_output": "", "weight": 0.2},
                    {"input": "racecar", "expected_output": "racecar", "weight": 0.5}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(n)",
                    "spaceComplexity": "O(1)",
                    "constraints": ["No use of language built-in reverse functions"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "EASY",
                    "estimatedDuration": 5,
                    "tags": ["strings", "algorithms"]
                }
            },
            {
                "order": 53,
                "title": "Find Duplicates",
                "text": "Implement a function to find all duplicates in an array.",
                "language": "python",
                "starterCode": "def find_duplicates(nums):\n    # Your code here\n    pass",
                "solutionCode": "def find_duplicates(nums):\n    seen = set()\n    duplicates = set()\n    for num in nums:\n        if num in seen:\n            duplicates.add(num)\n        else:\n            seen.add(num)\n    return list(duplicates)",
                "testCases": [
                    {"input": "[1, 2, 3, 4]", "expected_output": "[]", "weight": 0.2},
                    {"input": "[1, 2, 2, 3, 4, 4]", "expected_output": "[2, 4]", "weight": 0.4},
                    {"input": "[1, 1, 1, 1]", "expected_output": "[1]", "weight": 0.4}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(n)",
                    "spaceComplexity": "O(n)",
                    "constraints": ["Return duplicates in any order"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "MEDIUM",
                    "estimatedDuration": 10,
                    "tags": ["arrays", "hash tables"]
                }
            }
        ]
    },
    {
        "testId": "javascript-basics",
        "title": "JavaScript Programming Basics",
        "description": "This assessment tests fundamental JavaScript programming skills.",
        "duration": 60,
        "questions": generate_python_mcq_questions(),  # Using Python questions as placeholder, ideally would be JavaScript questions
        "codingQuestions": [
            {
                "order": 52,
                "title": "Fibonacci Sequence",
                "text": "Implement a function to generate the nth Fibonacci number.",
                "language": "javascript",
                "starterCode": "function fibonacci(n) {\n    // Your code here\n}",
                "solutionCode": "function fibonacci(n) {\n    if (n <= 1) return n;\n    return fibonacci(n-1) + fibonacci(n-2);\n}",
                "testCases": [
                    {"input": "0", "expected_output": "0", "weight": 0.2},
                    {"input": "1", "expected_output": "1", "weight": 0.2},
                    {"input": "10", "expected_output": "55", "weight": 0.6}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(2^n)",
                    "spaceComplexity": "O(n)",
                    "constraints": ["Recursive solution preferred"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "MEDIUM",
                    "estimatedDuration": 10,
                    "tags": ["recursion", "algorithms"]
                }
            },
            {
                "order": 53,
                "title": "Palindrome Check",
                "text": "Implement a function to check if a string is a palindrome.",
                "language": "javascript",
                "starterCode": "function isPalindrome(str) {\n    // Your code here\n}",
                "solutionCode": "function isPalindrome(str) {\n    str = str.toLowerCase().replace(/[^a-z0-9]/g, '');\n    return str === str.split('').reverse().join('');\n}",
                "testCases": [
                    {"input": "'racecar'", "expected_output": "true", "weight": 0.3},
                    {"input": "'hello'", "expected_output": "false", "weight": 0.3},
                    {"input": "'A man, a plan, a canal: Panama'", "expected_output": "true", "weight": 0.4}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(n)",
                    "spaceComplexity": "O(n)",
                    "constraints": ["Ignore case and non-alphanumeric characters"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "EASY",
                    "estimatedDuration": 5,
                    "tags": ["strings", "algorithms"]
                }
            }
        ]
    }
,
    {
        "testId": "java-basics",
        "title": "Java Programming Basics",
        "description": "This assessment tests fundamental Java programming skills.",
        "duration": 60,
        "questions": generate_python_mcq_questions(),  # Using Python questions as placeholder, ideally would be Java questions
        "codingQuestions": [
            {
                "order": 52,
                "title": "Reverse Array",
                "text": "Implement a method to reverse an array in-place.",
                "language": "java",
                "starterCode": "public class Solution {\n    public static void reverseArray(int[] arr) {\n        // Your code here\n    }\n}",
                "solutionCode": "public class Solution {\n    public static void reverseArray(int[] arr) {\n        int left = 0;\n        int right = arr.length - 1;\n        while (left < right) {\n            int temp = arr[left];\n            arr[left] = arr[right];\n            arr[right] = temp;\n            left++;\n            right--;\n        }\n    }\n}",
                "testCases": [
                    {"input": "[1, 2, 3, 4, 5]", "expected_output": "[5, 4, 3, 2, 1]", "weight": 0.4},
                    {"input": "[1]", "expected_output": "[1]", "weight": 0.3},
                    {"input": "[]", "expected_output": "[]", "weight": 0.3}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(n)",
                    "spaceComplexity": "O(1)",
                    "constraints": ["In-place reversal required"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "EASY",
                    "estimatedDuration": 5,
                    "tags": ["arrays", "algorithms"]
                }
            },
            {
                "order": 53,
                "title": "Find Prime Numbers",
                "text": "Implement a method to find all prime numbers up to n using the Sieve of Eratosthenes algorithm.",
                "language": "java",
                "starterCode": "import java.util.*;\n\npublic class Solution {\n    public static List<Integer> findPrimes(int n) {\n        // Your code here\n        return new ArrayList<>();\n    }\n}",
                "solutionCode": "import java.util.*;\n\npublic class Solution {\n    public static List<Integer> findPrimes(int n) {\n        boolean[] isPrime = new boolean[n + 1];\n        Arrays.fill(isPrime, true);\n        isPrime[0] = isPrime[1] = false;\n        \n        for (int i = 2; i * i <= n; i++) {\n            if (isPrime[i]) {\n                for (int j = i * i; j <= n; j += i) {\n                    isPrime[j] = false;\n                }\n            }\n        }\n        \n        List<Integer> primes = new ArrayList<>();\n        for (int i = 2; i <= n; i++) {\n            if (isPrime[i]) {\n                primes.add(i);\n            }\n        }\n        return primes;\n    }\n}",
                "testCases": [
                    {"input": "10", "expected_output": "[2, 3, 5, 7]", "weight": 0.3},
                    {"input": "20", "expected_output": "[2, 3, 5, 7, 11, 13, 17, 19]", "weight": 0.4},
                    {"input": "1", "expected_output": "[]", "weight": 0.3}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(n log log n)",
                    "spaceComplexity": "O(n)",
                    "constraints": ["Use Sieve of Eratosthenes for optimal performance"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "MEDIUM",
                    "estimatedDuration": 15,
                    "tags": ["algorithms", "mathematics"]
                }
            }
        ]
    },
    {
        "testId": "data-structures",
        "title": "Data Structures Assessment",
        "description": "This assessment tests knowledge of common data structures and their implementations.",
        "duration": 90,
        "questions": generate_python_mcq_questions(),  # Using Python questions as placeholder, ideally would be Data Structures questions
        "codingQuestions": [
            {
                "order": 52,
                "title": "Implement a Stack",
                "text": "Implement a stack data structure with push, pop, and peek operations.",
                "language": "python",
                "starterCode": "class Stack:\n    def __init__(self):\n        # Your code here\n        pass\n    \n    def push(self, value):\n        # Your code here\n        pass\n    \n    def pop(self):\n        # Your code here\n        pass\n    \n    def peek(self):\n        # Your code here\n        pass\n    \n    def is_empty(self):\n        # Your code here\n        pass",
                "solutionCode": "class Stack:\n    def __init__(self):\n        self.items = []\n    \n    def push(self, value):\n        self.items.append(value)\n    \n    def pop(self):\n        if self.is_empty():\n            return None\n        return self.items.pop()\n    \n    def peek(self):\n        if self.is_empty():\n            return None\n        return self.items[-1]\n    \n    def is_empty(self):\n        return len(self.items) == 0",
                "testCases": [
                    {"input": "s = Stack(); s.push(1); s.push(2); s.peek()", "expected_output": "2", "weight": 0.3},
                    {"input": "s = Stack(); s.push(1); s.push(2); s.pop(); s.pop(); s.is_empty()", "expected_output": "True", "weight": 0.4},
                    {"input": "s = Stack(); s.pop()", "expected_output": "None", "weight": 0.3}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(1) for all operations",
                    "spaceComplexity": "O(n)",
                    "constraints": ["Implement all required methods"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "EASY",
                    "estimatedDuration": 10,
                    "tags": ["data structures", "stack"]
                }
            },
            {
                "order": 53,
                "title": "Implement a Binary Search Tree",
                "text": "Implement a binary search tree with insert, search, and in-order traversal operations.",
                "language": "python",
                "starterCode": "class TreeNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n\nclass BinarySearchTree:\n    def __init__(self):\n        # Your code here\n        pass\n    \n    def insert(self, value):\n        # Your code here\n        pass\n    \n    def search(self, value):\n        # Your code here\n        pass\n    \n    def in_order_traversal(self):\n        # Your code here\n        pass",
                "solutionCode": "class TreeNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n\nclass BinarySearchTree:\n    def __init__(self):\n        self.root = None\n    \n    def insert(self, value):\n        if not self.root:\n            self.root = TreeNode(value)\n            return\n        \n        def _insert(node, value):\n            if value < node.value:\n                if node.left is None:\n                    node.left = TreeNode(value)\n                else:\n                    _insert(node.left, value)\n            else:\n                if node.right is None:\n                    node.right = TreeNode(value)\n                else:\n                    _insert(node.right, value)\n        \n        _insert(self.root, value)\n    \n    def search(self, value):\n        def _search(node, value):\n            if node is None:\n                return False\n            if node.value == value:\n                return True\n            if value < node.value:\n                return _search(node.left, value)\n            return _search(node.right, value)\n        \n        return _search(self.root, value)\n    \n    def in_order_traversal(self):\n        result = []\n        \n        def _traverse(node):\n            if node:\n                _traverse(node.left)\n                result.append(node.value)\n                _traverse(node.right)\n        \n        _traverse(self.root)\n        return result",
                "testCases": [
                    {"input": "bst = BinarySearchTree(); bst.insert(5); bst.insert(3); bst.insert(7); bst.in_order_traversal()", "expected_output": "[3, 5, 7]", "weight": 0.4},
                    {"input": "bst = BinarySearchTree(); bst.insert(5); bst.insert(3); bst.insert(7); bst.search(3)", "expected_output": "True", "weight": 0.3},
                    {"input": "bst = BinarySearchTree(); bst.insert(5); bst.insert(3); bst.insert(7); bst.search(10)", "expected_output": "False", "weight": 0.3}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(log n) average case for insert and search",
                    "spaceComplexity": "O(n)",
                    "constraints": ["Implement all required methods"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "MEDIUM",
                    "estimatedDuration": 20,
                    "tags": ["data structures", "binary search tree", "recursion"]
                }
            }
        ]
    },
    {
        "testId": "algorithms",
        "title": "Algorithms Assessment",
        "description": "This assessment tests knowledge of common algorithms and problem-solving techniques.",
        "duration": 90,
        "questions": generate_python_mcq_questions(),  # Using Python questions as placeholder, ideally would be Algorithms questions
        "codingQuestions": [
            {
                "order": 52,
                "title": "Merge Sort",
                "text": "Implement the merge sort algorithm to sort an array of integers.",
                "language": "python",
                "starterCode": "def merge_sort(arr):\n    # Your code here\n    pass",
                "solutionCode": "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    \n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    \n    return merge(left, right)\n\ndef merge(left, right):\n    result = []\n    i = j = 0\n    \n    while i < len(left) and j < len(right):\n        if left[i] <= right[j]:\n            result.append(left[i])\n            i += 1\n        else:\n            result.append(right[j])\n            j += 1\n    \n    result.extend(left[i:])\n    result.extend(right[j:])\n    return result",
                "testCases": [
                    {"input": "[5, 2, 4, 7, 1, 3, 2, 6]", "expected_output": "[1, 2, 2, 3, 4, 5, 6, 7]", "weight": 0.4},
                    {"input": "[1]", "expected_output": "[1]", "weight": 0.3},
                    {"input": "[]", "expected_output": "[]", "weight": 0.3}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(n log n)",
                    "spaceComplexity": "O(n)",
                    "constraints": ["Implement merge sort correctly"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "MEDIUM",
                    "estimatedDuration": 15,
                    "tags": ["algorithms", "sorting", "divide and conquer"]
                }
            },
            {
                "order": 53,
                "title": "Longest Common Subsequence",
                "text": "Implement a function to find the length of the longest common subsequence between two strings.",
                "language": "python",
                "starterCode": "def longest_common_subsequence(text1, text2):\n    # Your code here\n    pass",
                "solutionCode": "def longest_common_subsequence(text1, text2):\n    m, n = len(text1), len(text2)\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    \n    for i in range(1, m + 1):\n        for j in range(1, n + 1):\n            if text1[i-1] == text2[j-1]:\n                dp[i][j] = dp[i-1][j-1] + 1\n            else:\n                dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n    \n    return dp[m][n]",
                "testCases": [
                    {"input": "'abcde', 'ace'", "expected_output": "3", "weight": 0.3},
                    {"input": "'abc', 'abc'", "expected_output": "3", "weight": 0.3},
                    {"input": "'abc', 'def'", "expected_output": "0", "weight": 0.4}
                ],
                "evaluationCriteria": {
                    "timeComplexity": "O(m*n)",
                    "spaceComplexity": "O(m*n)",
                    "constraints": ["Use dynamic programming for optimal solution"]
                },
                "gradingRules": {
                    "testCaseWeight": 0.7,
                    "codeQualityWeight": 0.2,
                    "efficiencyWeight": 0.1,
                    "partialCredit": True
                },
                "metadata": {
                    "difficulty": "HARD",
                    "estimatedDuration": 20,
                    "tags": ["algorithms", "dynamic programming", "strings"]
                }
            }
        ]
    }
]

# Function to generate solutions for a test
def generate_solutions(test_id, num_solutions=50):
    """Generate a specified number of solutions for a given test."""
    solutions = []

    # Get the test to extract question information
    test = next((t for t in TEST_TEMPLATES if t["testId"] == test_id), None)
    if not test:
        print(f"Test with ID {test_id} not found")
        return []

    # Extract MCQ questions and their correct answers
    mcq_questions = [q for q in test["questions"] if q["type"] == "MCQ"]
    mcq_correct_answers = {q["order"]: q["correctAnswer"]["value"] for q in mcq_questions}

    # Extract open-ended questions
    open_ended_questions = [q for q in test["questions"] if q["type"] == "OPEN_ENDED"]

    # Extract coding questions and their solution code
    coding_questions = test["codingQuestions"]
    coding_solutions = {q["order"]: q["solutionCode"] for q in coding_questions}

    # Generate solutions with varying quality
    for i in range(num_solutions):
        # Generate a unique solution ID
        solution_id = f"{test_id}-sol-{i+1}"

        # Generate a unique candidate ID
        candidate_id = f"candidate-{uuid.uuid4().hex[:8]}"

        # Generate start and end times
        started_at = (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat()
        time_taken = random.randint(15 * 60, test["duration"] * 60)  # Between 15 minutes and max duration
        completed_at = (datetime.fromisoformat(started_at) + timedelta(seconds=time_taken)).isoformat()

        # Generate MCQ answers with varying correctness
        mcq_answers = []
        for q in mcq_questions:
            q_order = q["order"]
            correct_answer = mcq_correct_answers[q_order]

            # Determine if this answer will be correct (70% chance for good solutions, decreasing for worse ones)
            correctness_chance = max(0.3, 0.7 - (i / num_solutions * 0.4))
            is_correct = random.random() < correctness_chance

            # If correct, use the correct answer, otherwise choose a random wrong answer
            if is_correct:
                answer_value = correct_answer
            else:
                # Get all possible answers except the correct one
                all_choices = [choice["id"] for choice in q["options"]["choices"]]
                wrong_choices = [c for c in all_choices if c != correct_answer]
                answer_value = random.choice(wrong_choices)

            mcq_answers.append({
                "question_id": str(q_order),
                "answer_type": "MCQ",
                "value": answer_value,
                "submitted_at": (datetime.fromisoformat(started_at) + timedelta(seconds=random.randint(60, time_taken - 60))).isoformat()
            })

        # Generate open-ended answers
        open_ended_answers = []
        for q in open_ended_questions:
            q_order = q["order"]

            # Generate answers of varying quality
            quality_factor = max(0.3, 0.8 - (i / num_solutions * 0.5))

            if q_order == 3 and test_id == "python-basics":
                # Answer for Python list vs tuple question
                if quality_factor > 0.7:
                    answer = "Lists are mutable, meaning they can be changed after creation (elements can be added, removed, or modified). Tuples are immutable, meaning they cannot be changed after creation. Lists use square brackets [] while tuples use parentheses (). Lists generally have more built-in methods and are slightly less memory efficient than tuples."
                elif quality_factor > 0.5:
                    answer = "Lists can be changed after creation but tuples cannot. Lists use [] and tuples use (). Lists have more methods than tuples."
                else:
                    answer = "Lists can be modified and tuples cannot. Lists are better for most cases."
            elif q_order == 3 and test_id == "javascript-basics":
                # Answer for JavaScript variable declaration question
                if quality_factor > 0.7:
                    answer = "let: Block-scoped variable that can be reassigned. const: Block-scoped variable that cannot be reassigned after declaration (though properties of objects can be modified). var: Function-scoped variable that can be reassigned and is hoisted to the top of its scope. Best practice is to use const by default, let when reassignment is needed, and avoid var in modern code."
                elif quality_factor > 0.5:
                    answer = "let is block-scoped and can be changed. const is block-scoped and cannot be changed. var is function-scoped and can be changed. const is preferred when possible."
                else:
                    answer = "let and const are newer than var. const can't be changed. var is old and shouldn't be used."
            elif q_order == 3 and test_id == "java-basics":
                # Answer for Java interface vs abstract class question
                if quality_factor > 0.7:
                    answer = "An abstract class can have both abstract and concrete methods, while an interface can only have abstract methods (prior to Java 8) or default/static methods (Java 8+). A class can implement multiple interfaces but can extend only one abstract class. Abstract classes can have constructors, instance variables, and different access modifiers, while interfaces cannot have constructors, have public static final variables by default, and all methods are implicitly public."
                elif quality_factor > 0.5:
                    answer = "Abstract classes can have implemented methods but interfaces only have method signatures. Classes can extend one abstract class but implement many interfaces. Abstract classes can have constructors but interfaces cannot."
                else:
                    answer = "Abstract classes have some implemented methods. Interfaces just define methods that must be implemented. You can only extend one class but implement many interfaces."
            elif q_order == 3 and test_id == "data-structures":
                # Answer for hash table vs BST question
                if quality_factor > 0.7:
                    answer = "Hash tables provide O(1) average case lookup, insertion, and deletion, while BSTs provide O(log n) for these operations. Hash tables don't maintain order of elements, while BSTs keep elements sorted. Hash tables may have collisions requiring resolution strategies, while BSTs don't have this issue. BSTs allow efficient in-order traversal and range queries, which hash tables don't support well. Hash tables typically use more memory than BSTs."
                elif quality_factor > 0.5:
                    answer = "Hash tables have O(1) operations while BSTs have O(log n). Hash tables don't keep elements in order but BSTs do. Hash tables can have collisions. BSTs are better for finding ranges of values."
                else:
                    answer = "Hash tables are faster for lookups. BSTs keep things in order. Hash tables use more memory."
            elif q_order == 3 and test_id == "algorithms":
                # Answer for dynamic programming question
                if quality_factor > 0.7:
                    answer = "Dynamic programming is an algorithmic technique for solving complex problems by breaking them down into simpler subproblems, solving each subproblem once, and storing the solutions to avoid redundant computations. It's applicable when problems have overlapping subproblems and optimal substructure. A classic example is the Fibonacci sequence calculation: instead of using recursion with exponential time complexity, we can use dynamic programming to compute it in linear time by storing previously calculated values. Other examples include the knapsack problem, longest common subsequence, and matrix chain multiplication."
                elif quality_factor > 0.5:
                    answer = "Dynamic programming solves problems by breaking them into smaller subproblems and storing the results to avoid recalculating. It works when problems have overlapping subproblems and optimal substructure. An example is calculating Fibonacci numbers by storing previous results instead of using recursion."
                else:
                    answer = "Dynamic programming is a way to make algorithms faster by storing results of calculations. It's used for things like Fibonacci numbers and the knapsack problem."
            else:
                # Generic answer for any other open-ended question
                if quality_factor > 0.7:
                    answer = "This is a high-quality, detailed answer that demonstrates deep understanding of the concept."
                elif quality_factor > 0.5:
                    answer = "This is a medium-quality answer that shows basic understanding of the concept."
                else:
                    answer = "This is a low-quality answer with minimal explanation."

            open_ended_answers.append({
                "question_id": str(q_order),
                "answer_type": "OPEN_ENDED",
                "value": answer,
                "submitted_at": (datetime.fromisoformat(started_at) + timedelta(seconds=random.randint(60, time_taken - 60))).isoformat()
            })

        # Generate coding answers
        coding_answers = []
        for q in coding_questions:
            q_order = q["order"]
            correct_solution = coding_solutions[q_order]

            # Determine solution quality
            quality_factor = max(0.2, 0.8 - (i / num_solutions * 0.6))

            # Generate a solution based on quality
            if quality_factor > 0.7:
                # High-quality solution (similar to correct solution)
                code = correct_solution
            elif quality_factor > 0.5:
                # Medium-quality solution (functional but not optimal)
                if "reverse_string" in correct_solution:
                    code = "def reverse_string(s):\n    result = ''\n    for char in s:\n        result = char + result\n    return result"
                elif "find_duplicates" in correct_solution:
                    code = "def find_duplicates(nums):\n    result = []\n    for i in range(len(nums)):\n        for j in range(i+1, len(nums)):\n            if nums[i] == nums[j] and nums[i] not in result:\n                result.append(nums[i])\n    return result"
                elif "fibonacci" in correct_solution:
                    code = "function fibonacci(n) {\n    if (n <= 1) return n;\n    let a = 0, b = 1;\n    for (let i = 2; i <= n; i++) {\n        let c = a + b;\n        a = b;\n        b = c;\n    }\n    return b;\n}"
                elif "isPalindrome" in correct_solution:
                    code = "function isPalindrome(str) {\n    str = str.toLowerCase();\n    let alphanumeric = '';\n    for (let char of str) {\n        if ((char >= 'a' && char <= 'z') || (char >= '0' && char <= '9')) {\n            alphanumeric += char;\n        }\n    }\n    for (let i = 0; i < alphanumeric.length / 2; i++) {\n        if (alphanumeric[i] !== alphanumeric[alphanumeric.length - 1 - i]) {\n            return false;\n        }\n    }\n    return true;\n}"
                elif "reverseArray" in correct_solution:
                    code = "public class Solution {\n    public static void reverseArray(int[] arr) {\n        int[] reversed = new int[arr.length];\n        for (int i = 0; i < arr.length; i++) {\n            reversed[i] = arr[arr.length - 1 - i];\n        }\n        for (int i = 0; i < arr.length; i++) {\n            arr[i] = reversed[i];\n        }\n    }\n}"
                elif "findPrimes" in correct_solution:
                    code = "import java.util.*;\n\npublic class Solution {\n    public static List<Integer> findPrimes(int n) {\n        List<Integer> primes = new ArrayList<>();\n        for (int i = 2; i <= n; i++) {\n            boolean isPrime = true;\n            for (int j = 2; j < i; j++) {\n                if (i % j == 0) {\n                    isPrime = false;\n                    break;\n                }\n            }\n            if (isPrime) {\n                primes.add(i);\n            }\n        }\n        return primes;\n    }\n}"
                elif "Stack" in correct_solution:
                    code = "class Stack:\n    def __init__(self):\n        self.stack = []\n    \n    def push(self, value):\n        self.stack.append(value)\n    \n    def pop(self):\n        if len(self.stack) == 0:\n            return None\n        return self.stack.pop()\n    \n    def peek(self):\n        if len(self.stack) == 0:\n            return None\n        return self.stack[-1]\n    \n    def is_empty(self):\n        return len(self.stack) == 0"
                elif "BinarySearchTree" in correct_solution:
                    code = "class TreeNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n\nclass BinarySearchTree:\n    def __init__(self):\n        self.root = None\n    \n    def insert(self, value):\n        if not self.root:\n            self.root = TreeNode(value)\n        else:\n            self._insert_recursive(self.root, value)\n    \n    def _insert_recursive(self, node, value):\n        if value < node.value:\n            if node.left is None:\n                node.left = TreeNode(value)\n            else:\n                self._insert_recursive(node.left, value)\n        else:\n            if node.right is None:\n                node.right = TreeNode(value)\n            else:\n                self._insert_recursive(node.right, value)\n    \n    def search(self, value):\n        return self._search_recursive(self.root, value)\n    \n    def _search_recursive(self, node, value):\n        if node is None:\n            return False\n        if node.value == value:\n            return True\n        if value < node.value:\n            return self._search_recursive(node.left, value)\n        return self._search_recursive(node.right, value)\n    \n    def in_order_traversal(self):\n        result = []\n        self._in_order_recursive(self.root, result)\n        return result\n    \n    def _in_order_recursive(self, node, result):\n        if node:\n            self._in_order_recursive(node.left, result)\n            result.append(node.value)\n            self._in_order_recursive(node.right, result)"
                elif "merge_sort" in correct_solution:
                    code = "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    \n    mid = len(arr) // 2\n    left = arr[:mid]\n    right = arr[mid:]\n    \n    left = merge_sort(left)\n    right = merge_sort(right)\n    \n    return merge(left, right)\n\ndef merge(left, right):\n    result = []\n    i = j = 0\n    \n    while i < len(left) and j < len(right):\n        if left[i] < right[j]:\n            result.append(left[i])\n            i += 1\n        else:\n            result.append(right[j])\n            j += 1\n    \n    while i < len(left):\n        result.append(left[i])\n        i += 1\n    \n    while j < len(right):\n        result.append(right[j])\n        j += 1\n    \n    return result"
                elif "longest_common_subsequence" in correct_solution:
                    code = "def longest_common_subsequence(text1, text2):\n    m, n = len(text1), len(text2)\n    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]\n    \n    for i in range(1, m+1):\n        for j in range(1, n+1):\n            if text1[i-1] == text2[j-1]:\n                dp[i][j] = dp[i-1][j-1] + 1\n            else:\n                dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n    \n    return dp[m][n]"
                else:
                    # Generic medium-quality solution
                    code = "# Medium quality solution\n" + "\n".join(correct_solution.split("\n")[1:])
            else:
                # Low-quality solution (incomplete or incorrect)
                if "reverse_string" in correct_solution:
                    code = "def reverse_string(s):\n    # Incomplete solution\n    result = ''\n    # Missing implementation\n    return result"
                elif "find_duplicates" in correct_solution:
                    code = "def find_duplicates(nums):\n    # Incorrect solution\n    return list(set(nums))"
                elif "fibonacci" in correct_solution:
                    code = "function fibonacci(n) {\n    // Inefficient solution\n    if (n <= 1) return n;\n    return fibonacci(n-1) + fibonacci(n-2);\n}"
                elif "isPalindrome" in correct_solution:
                    code = "function isPalindrome(str) {\n    // Incomplete solution that doesn't handle special cases\n    return str === str.split('').reverse().join('');\n}"
                elif "reverseArray" in correct_solution:
                    code = "public class Solution {\n    public static void reverseArray(int[] arr) {\n        // Incomplete solution\n        // Missing implementation\n    }\n}"
                elif "findPrimes" in correct_solution:
                    code = "import java.util.*;\n\npublic class Solution {\n    public static List<Integer> findPrimes(int n) {\n        // Incorrect implementation\n        List<Integer> primes = new ArrayList<>();\n        for (int i = 2; i <= n; i++) {\n            primes.add(i);\n        }\n        return primes;\n    }\n}"
                elif "Stack" in correct_solution:
                    code = "class Stack:\n    def __init__(self):\n        self.items = []\n    \n    def push(self, value):\n        self.items.append(value)\n    \n    # Missing pop and peek methods\n    \n    def is_empty(self):\n        return len(self.items) == 0"
                elif "BinarySearchTree" in correct_solution:
                    code = "class TreeNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n\nclass BinarySearchTree:\n    def __init__(self):\n        self.root = None\n    \n    def insert(self, value):\n        # Incomplete implementation\n        if not self.root:\n            self.root = TreeNode(value)\n    \n    # Missing search method\n    \n    def in_order_traversal(self):\n        # Incorrect implementation\n        return []"
                elif "merge_sort" in correct_solution:
                    code = "def merge_sort(arr):\n    # Incomplete implementation\n    if len(arr) <= 1:\n        return arr\n    \n    mid = len(arr) // 2\n    left = arr[:mid]\n    right = arr[mid:]\n    \n    # Missing recursive calls and merge function\n    return arr"
                elif "longest_common_subsequence" in correct_solution:
                    code = "def longest_common_subsequence(text1, text2):\n    # Naive and inefficient implementation\n    if not text1 or not text2:\n        return 0\n    if text1[0] == text2[0]:\n        return 1 + longest_common_subsequence(text1[1:], text2[1:])\n    return max(longest_common_subsequence(text1, text2[1:]), longest_common_subsequence(text1[1:], text2))"
                else:
                    # Generic low-quality solution
                    code = "# Low quality solution\n# Incomplete implementation"

            # Add random execution time and memory usage
            execution_time = random.uniform(0.01, 0.5)
            memory_usage = random.randint(512, 4096)

            coding_answers.append({
                "question_id": str(q_order),
                "code": code,
                "language": q["language"],
                "execution_time": execution_time,
                "memory_usage": memory_usage,
                "submitted_at": (datetime.fromisoformat(started_at) + timedelta(seconds=random.randint(60, time_taken - 60))).isoformat()
            })

        # Combine all answers
        solution = {
            "solution_id": solution_id,
            "test_id": test_id,
            "candidate_id": candidate_id,
            "answers": mcq_answers + open_ended_answers,
            "coding_answers": coding_answers,
            "started_at": started_at,
            "completed_at": completed_at,
            "time_taken": time_taken
        }

        solutions.append(solution)

    return solutions

# Main function to load data
def load_professional_data(drop_existing=False):
    """Load professional data into the database."""
    if drop_existing:
        print("Dropping existing collections...")
        db_service.drop_collections()

    # Store assessments
    print("Storing assessments...")
    for test in TEST_TEMPLATES:
        existing = db_service.get_assessment_by_id(test["testId"])
        if existing:
            print(f"Assessment {test['testId']} already exists, skipping...")
            continue

        assessment_id = db_service.store_assessment(test)
        print(f"Stored assessment {test['testId']} with ID: {assessment_id}")

    # Generate and store solutions
    print("Generating and storing solutions...")
    all_solutions = []
    for test in TEST_TEMPLATES:
        test_id = test["testId"]
        print(f"Generating solutions for test {test_id}...")
        solutions = generate_solutions(test_id, num_solutions=3)
        all_solutions.extend(solutions)

        for solution in solutions:
            solution_id = solution["solution_id"]
            existing = db_service.get_solution_by_id(solution_id)
            if existing:
                print(f"Solution {solution_id} already exists, skipping...")
                continue

            db_service.store_solution(solution)
            print(f"Stored solution {solution_id}")

# Run the script
if __name__ == "__main__":
    load_professional_data(drop_existing=args.drop_existing)
