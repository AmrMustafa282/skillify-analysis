# Assessment Analysis API - Postman Collection

This folder contains a Postman collection for the Assessment Analysis API. The collection includes all available endpoints organized by category.

## Importing the Collection

1. Open Postman
2. Click on "Import" in the top left corner
3. Select "File" and choose the `assessment_analysis_api.postman_collection.json` file
4. Click "Import"

## Collection Structure

The collection is organized into the following folders:

- **Health**: Health check endpoint
- **Authentication**: Login endpoint (not required for current API version)
- **Assessments**: Assessment management endpoints (CRUD operations)
- **Solutions**: Solution management endpoints
- **Analysis**: Analysis endpoints
- **Reports**: Report management endpoints

## Using the Collection

### Environment Setup

It's recommended to set up a Postman environment to easily switch between different environments (e.g., local, development, production).

1. Click on "Environments" in the sidebar
2. Click "Add" to create a new environment
3. Name it "Assessment Analysis API - Local"
4. Add the following variables:
   - `baseUrl`: `http://localhost:5001`
   - `token`: (leave empty for now)
5. Click "Save"

Then, update the requests to use the environment variable:
1. Select all requests in the collection
2. Replace `http://localhost:5001` with `{{baseUrl}}`
3. Save the collection

### Running Requests

1. Make sure the API server is running
2. Select the environment from the dropdown in the top right corner
3. Navigate to the desired endpoint in the collection
4. Click "Send" to execute the request

### Testing the API Flow

Here's a recommended sequence to test the API:

1. **Health Check**: Verify the API is running
2. **Create Assessment**: Create a new assessment
3. **Create Solution**: Submit a solution for the assessment
4. **Analyze Solution**: Analyze the submitted solution
5. **Generate Report**: Generate a report for the assessment
6. **Get Report**: Retrieve the generated report

## Example Requests

### Create Assessment

```json
POST {{baseUrl}}/api/assessments
Content-Type: application/json

{
    "testId": "test456",
    "title": "JavaScript Programming Assessment",
    "description": "This assessment tests your JavaScript programming skills.",
    "duration": 60,
    "questions": [
        {
            "order": 1,
            "type": "MCQ",
            "text": "What is the result of 2 + '2' in JavaScript?",
            "options": {
                "choices": [
                    {
                        "id": "q1_a",
                        "text": "4"
                    },
                    {
                        "id": "q1_b",
                        "text": "'22'"
                    },
                    {
                        "id": "q1_c",
                        "text": "22"
                    },
                    {
                        "id": "q1_d",
                        "text": "TypeError"
                    }
                ]
            },
            "correctAnswer": {
                "value": "q1_c"
            }
        }
    ],
    "codingQuestions": [
        {
            "order": 2,
            "title": "Fibonacci Sequence",
            "description": "Implement a function to generate the nth Fibonacci number.",
            "language": "javascript",
            "starterCode": "function fibonacci(n) {\n    // Your code here\n}",
            "solutionCode": "function fibonacci(n) {\n    if (n <= 1) return n;\n    return fibonacci(n-1) + fibonacci(n-2);\n}",
            "testCases": [
                {
                    "input": "0",
                    "expected_output": "0",
                    "weight": 0.2
                },
                {
                    "input": "1",
                    "expected_output": "1",
                    "weight": 0.2
                },
                {
                    "input": "10",
                    "expected_output": "55",
                    "weight": 0.6
                }
            ]
        }
    ]
}
```

### Create Solution

```json
POST {{baseUrl}}/api/solutions
Content-Type: application/json

{
    "solution_id": "sol456",
    "test_id": "test456",
    "candidate_id": "cand456",
    "answers": [
        {
            "question_id": "1",
            "answer_type": "MCQ",
            "value": "q1_c",
            "submitted_at": "2023-01-01T00:10:00Z"
        }
    ],
    "coding_answers": [
        {
            "question_id": "2",
            "code": "function fibonacci(n) {\n    if (n <= 1) return n;\n    let a = 0, b = 1;\n    for (let i = 2; i <= n; i++) {\n        let c = a + b;\n        a = b;\n        b = c;\n    }\n    return b;\n}",
            "language": "javascript",
            "execution_time": 0.05,
            "memory_usage": 1024,
            "submitted_at": "2023-01-01T00:30:00Z"
        }
    ],
    "started_at": "2023-01-01T00:00:00Z",
    "completed_at": "2023-01-01T00:30:00Z",
    "time_taken": 1800
}
```
