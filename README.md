# Assessment Management System

A comprehensive Python-based system for analyzing coding assessments, evaluating solutions, and generating detailed reports.

![Assessment Management System](https://via.placeholder.com/800x400?text=Assessment+Management+System)

## Overview

The Assessment Management System is designed to help educators, hiring managers, and technical interviewers evaluate coding solutions with precision and consistency. The system analyzes solutions based on multiple dimensions:

- **Correctness**: Evaluates if the solution passes test cases
- **Code Quality**: Analyzes complexity, maintainability, and structure
- **AI Detection**: Identifies patterns common in AI-generated code
- **Style Analysis**: Checks adherence to coding conventions
- **Performance Analysis**: Estimates time and space complexity
- **Naming Conventions**: Evaluates variable and function naming

## Key Features

- **MongoDB Integration**: Stores assessments, solutions, and analysis results
- **Multi-dimensional Analysis**: Evaluates code across 6+ dimensions
- **Automated Reporting**: Generates individual and comparative reports
- **RESTful API**: Provides programmatic access to all functionality
- **Swagger Documentation**: Interactive API documentation
- **Professional Dataset**: Includes 5 assessment types with 50 solutions each
- **No Authentication Required**: All endpoints are publicly accessible

## System Architecture

```
assessment-system/
├── server/                # Core server components
│   ├── api.py             # API endpoints
│   ├── server.py          # Server initialization
│   ├── services/          # Core services
│   │   ├── analyzers/     # Analysis components
│   │   ├── transformers/  # Data transformation
│   │   ├── database_service.py
│   │   ├── analysis_service.py
│   │   ├── ranking_service.py
│   │   ├── reporting_service.py
│   │   └── code_execution_service.py  # Docker-based code execution
│   └── utils/             # Utility functions
├── scripts/               # Utility scripts
│   ├── drop_database.sh
│   ├── add_dummy_data.sh
│   ├── load_professional_data.sh
│   ├── start_api_server.sh
│   ├── analyze_all.sh
│   ├── generate_reports.sh
│   └── start_docker.sh    # Start Docker containers
├── docker/                # Docker configuration
│   └── code-execution/    # Code execution environment
├── sample_data/           # Sample data for testing
├── tests/                 # Unit and integration tests
├── postman/               # Postman collection
└── README.md              # Documentation
```

## Installation

### Prerequisites

- Python 3.8+
- MongoDB 4.4+
- Docker (optional)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/assessment-management-system.git
cd assessment-management-system
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start Docker services (MongoDB and code execution environment):

```bash
# Start all Docker services
./scripts/start_docker.sh

# Or manually using docker-compose
docker-compose up -d
```

5. Make scripts executable:

```bash
chmod +x scripts/*.sh
```

## Usage

### Loading Data

The system comes with scripts to load sample data:

```bash
# Add basic dummy data
./scripts/add_dummy_data.sh

# Load professional dataset (5 tests with 50 solutions each)
./scripts/load_professional_data.sh

# Clear database and load professional data
./scripts/load_professional_data.sh --drop-existing
```

### Starting the API Server

```bash
./scripts/start_api_server.sh
```

The API server will be available at http://localhost:5002.

### Analyzing Solutions

```bash
# Analyze all unprocessed solutions
./scripts/analyze_all.sh

# Or using Python directly
python -m server.server --analyze-all
```

### Generating Reports

```bash
# Generate reports for all tests
./scripts/generate_reports.sh

# Or using Python directly
python -m server.server --generate-reports
```

## API Documentation

The API is documented using Swagger (OpenAPI). You can access the interactive documentation at:

```
http://localhost:5002/api/docs/
```

### Key Endpoints

#### Assessments

| Method | Endpoint                  | Description               |
| ------ | ------------------------- | ------------------------- |
| GET    | /api/assessments          | Get all assessments       |
| GET    | /api/assessments/:test_id | Get a specific assessment |
| POST   | /api/assessments          | Create a new assessment   |
| PUT    | /api/assessments/:test_id | Update an assessment      |
| DELETE | /api/assessments/:test_id | Delete an assessment      |

#### Solutions

| Method | Endpoint                            | Description                           |
| ------ | ----------------------------------- | ------------------------------------- |
| GET    | /api/solutions                      | Get all solutions                     |
| GET    | /api/solutions/:solution_id         | Get a specific solution               |
| GET    | /api/assessments/:test_id/solutions | Get all solutions for a specific test |
| POST   | /api/solutions                      | Create a new solution                 |

#### Analysis

| Method | Endpoint                           | Description                               |
| ------ | ---------------------------------- | ----------------------------------------- |
| GET    | /api/analysis/:solution_id         | Get analysis for a specific solution      |
| POST   | /api/analyze/solution/:solution_id | Analyze a specific solution               |
| POST   | /api/analyze/test/:test_id         | Analyze all solutions for a specific test |
| POST   | /api/analyze/all                   | Analyze all unprocessed solutions         |

#### Reports

| Method | Endpoint                       | Description                         |
| ------ | ------------------------------ | ----------------------------------- |
| GET    | /api/reports                   | Get all reports                     |
| GET    | /api/reports/:report_id        | Get a specific report               |
| GET    | /api/reports/test/:test_id     | Get report for a specific test      |
| POST   | /api/reports/generate/:test_id | Generate report for a specific test |
| POST   | /api/reports/generate/all      | Generate reports for all tests      |

## Professional Dataset

The system includes a professional dataset with:

- 5 different assessment types:
  - Python Basics
  - JavaScript Basics
  - Java Basics
  - Data Structures
  - Algorithms
- 50 solutions per assessment with varying quality
- Realistic answers for MCQ, open-ended, and coding questions
- Automatic analysis of all solutions
- Generated reports for each assessment

## Analysis Features

### Correctness Analysis

- Executes code against test cases in a secure Docker environment
- Supports Python, JavaScript, and Java code execution
- Automatically detects function names and parameters
- Intelligently handles array inputs based on function signatures
- Calculates correctness score based on test case results
- Takes into account the number of passed tests
- Provides detailed error messages and execution metrics
- Handles permission errors gracefully when cleaning up temporary files
- Falls back to local execution when Docker is not available

### Code Quality Analysis

- Measures cyclomatic complexity
- Calculates maintainability index
- Analyzes comment ratio and function count

### AI Detection

- Detects patterns common in AI-generated code
- Calculates probability of AI generation
- Identifies specific patterns that suggest AI generation

### Style Analysis

- Checks adherence to coding style conventions
- Analyzes naming conventions
- Identifies style issues

### Performance Analysis

- Estimates time and space complexity
- Compares with expected complexity
- Suggests optimizations

## Report Generation

The system generates two types of reports:

1. **Individual Reports**: Detailed analysis of a single candidate's performance
2. **Comparative Reports**: Comparison of all candidates for a specific test

Reports include:

- Overall scores and rankings
- Detailed breakdown by analysis dimension
- Comparative tables for easy comparison
- Visualizations of performance metrics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MongoDB for database functionality
- Flask for API framework
- Swagger for API documentation
