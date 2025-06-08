# Analysis Solution Schema

This document provides the complete schema and sample data for the analysis solution that gets stored in the database after analyzing coding submissions.

## Database Collection: `analysis_results`

### Schema Structure

```typescript
interface AnalysisSolution {
 // Unique identifier for the analysis result
 analysis_id: string;

 // Reference to the original solution
 solution_id: string;
 test_id: string;
 candidate_id: string;

 // Analysis metadata
 analyzed_at: string; // ISO timestamp
 analysis_version: string; // Version of analysis engine
 status: "completed" | "failed" | "in_progress";

 // Overall analysis summary
 overall_score: number; // 0.0 to 1.0
 grade: "A" | "B" | "C" | "D" | "F";

 // Individual analysis results for each coding question
 coding_analysis: CodingQuestionAnalysis[];

 // Regular questions analysis (MCQ/Open-ended)
 regular_analysis: RegularQuestionAnalysis[];

 // Analysis summary and recommendations
 summary: AnalysisSummary;
}

interface CodingQuestionAnalysis {
 question_id: string;
 question_title: string;
 language: string;
 submitted_code: string;

 // Core analysis metrics
 correctness: CorrectnessAnalysis;
 ai_detection: AIDetectionAnalysis;
 code_quality: CodeQualityAnalysis;
 performance: PerformanceAnalysis;
 style: StyleAnalysis;
 naming: NamingAnalysis;

 // Overall score for this question
 question_score: number; // 0.0 to 1.0
 weighted_score: number; // Based on question weight
}

interface CorrectnessAnalysis {
 correctness_score: number; // 0.0 to 1.0
 test_case_results: TestCaseResult[];
 passed_tests: number;
 total_tests: number;
 execution_summary: {
  total_execution_time: number;
  average_execution_time: number;
  total_memory_usage: number;
 };
}

interface TestCaseResult {
 test_case_id: string;
 passed: boolean;
 actual_output: string;
 expected_output: string;
 execution_time: number; // milliseconds
 memory_usage: number; // KB
 error_message?: string;
 weight: number; // Test case weight
}

interface AIDetectionAnalysis {
 ai_generated_probability: number; // 0.0 to 1.0
 detection_method: string;
 flagged_patterns: string[];
 confidence_level: "low" | "medium" | "high";
 risk_assessment: "minimal" | "moderate" | "high" | "critical";
}

interface CodeQualityAnalysis {
 cyclomatic_complexity: number;
 maintainability_index: number;
 halstead_volume?: number;
 comment_ratio: number;
 function_count: number;
 line_count: number;
 quality_score: number; // 0.0 to 1.0
 quality_grade: "A" | "B" | "C" | "D" | "F";
}

interface PerformanceAnalysis {
 time_complexity: string; // e.g., "O(n)", "O(log n)"
 space_complexity: string;
 efficiency_score: number; // 0.0 to 1.0
 performance_issues: string[];
 optimization_suggestions: string[];
}

interface StyleAnalysis {
 style_score: number; // 0.0 to 1.0
 style_violations: StyleViolation[];
 formatting_issues: string[];
 best_practices_followed: string[];
 improvement_suggestions: string[];
}

interface StyleViolation {
 type: string;
 line_number: number;
 description: string;
 severity: "info" | "warning" | "error";
}

interface NamingAnalysis {
 naming_score: number; // 0.0 to 1.0
 naming_issues: NamingIssue[];
 conventions_followed: string[];
 improvement_suggestions: string[];
}

interface NamingIssue {
 variable_name: string;
 issue_type: string;
 suggestion: string;
 line_number: number;
}

interface RegularQuestionAnalysis {
 question_id: string;
 question_type: "MCQ" | "OPEN_ENDED";
 submitted_answer: string;
 correct_answer?: string;
 is_correct: boolean;
 score: number; // 0.0 to 1.0

 // For open-ended questions
 quality_assessment?: {
  completeness: number;
  accuracy: number;
  clarity: number;
  depth: number;
  overall_quality: number;
 };
}

interface AnalysisSummary {
 strengths: string[];
 weaknesses: string[];
 recommendations: string[];
 overall_feedback: string;

 // Score breakdown
 score_breakdown: {
  correctness: number;
  ai_detection: number;
  code_quality: number;
  performance: number;
  style: number;
  naming: number;
  regular_questions: number;
 };

 // Time and effort analysis
 time_analysis: {
  total_time_taken: number; // seconds
  time_per_question: { [question_id: string]: number };
  efficiency_rating: "excellent" | "good" | "average" | "poor";
 };
}
```

## Sample Analysis Solution

```json
{
 "analysis_id": "analysis-python-basics-candidate-123-20250608",
 "solution_id": "python-basics-candidate-123-abc12345",
 "test_id": "python-basics",
 "candidate_id": "candidate-123",
 "analyzed_at": "2025-06-08T09:45:30.123456",
 "analysis_version": "1.0.0",
 "status": "completed",
 "overall_score": 0.78,
 "grade": "B",
 "coding_analysis": [
  {
   "question_id": "52",
   "question_title": "Reverse String",
   "language": "python",
   "submitted_code": "def reverse_string(s):\n    return s[::-1]",
   "correctness": {
    "correctness_score": 1.0,
    "test_case_results": [
     {
      "test_case_id": "test_0",
      "passed": true,
      "actual_output": "olleh",
      "expected_output": "olleh",
      "execution_time": 0.05,
      "memory_usage": 1024,
      "error_message": null,
      "weight": 0.3
     },
     {
      "test_case_id": "test_1",
      "passed": true,
      "actual_output": "",
      "expected_output": "",
      "execution_time": 0.02,
      "memory_usage": 512,
      "error_message": null,
      "weight": 0.3
     },
     {
      "test_case_id": "test_2",
      "passed": true,
      "actual_output": "!dlroW olleH",
      "expected_output": "!dlroW olleH",
      "execution_time": 0.08,
      "memory_usage": 1536,
      "error_message": null,
      "weight": 0.4
     }
    ],
    "passed_tests": 3,
    "total_tests": 3,
    "execution_summary": {
     "total_execution_time": 0.15,
     "average_execution_time": 0.05,
     "total_memory_usage": 3072
    }
   },
   "ai_detection": {
    "ai_generated_probability": 0.15,
    "detection_method": "pattern_matching",
    "flagged_patterns": ["generic_variable_names: 1 instances"],
    "confidence_level": "low",
    "risk_assessment": "minimal"
   },
   "code_quality": {
    "cyclomatic_complexity": 1.0,
    "maintainability_index": 100.0,
    "halstead_volume": null,
    "comment_ratio": 0.0,
    "function_count": 1,
    "line_count": 2,
    "quality_score": 0.85,
    "quality_grade": "A"
   },
   "performance": {
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "efficiency_score": 0.9,
    "performance_issues": [],
    "optimization_suggestions": [
     "Consider in-place reversal for large strings to reduce memory usage"
    ]
   },
   "style": {
    "style_score": 0.8,
    "style_violations": [],
    "formatting_issues": ["Missing docstring"],
    "best_practices_followed": [
     "Clear function name",
     "Concise implementation"
    ],
    "improvement_suggestions": [
     "Add docstring to explain function purpose",
     "Consider adding type hints"
    ]
   },
   "naming": {
    "naming_score": 0.9,
    "naming_issues": [],
    "conventions_followed": [
     "snake_case function name",
     "Descriptive parameter name"
    ],
    "improvement_suggestions": []
   },
   "question_score": 0.85,
   "weighted_score": 0.85
  },
  {
   "question_id": "53",
   "question_title": "Find Duplicates",
   "language": "python",
   "submitted_code": "def find_duplicates(nums):\n    seen = set()\n    duplicates = set()\n    for num in nums:\n        if num in seen:\n            duplicates.add(num)\n        else:\n            seen.add(num)\n    return list(duplicates)",
   "correctness": {
    "correctness_score": 0.67,
    "test_case_results": [
     {
      "test_case_id": "test_0",
      "passed": true,
      "actual_output": "[2, 3]",
      "expected_output": "[2, 3]",
      "execution_time": 0.12,
      "memory_usage": 2048,
      "error_message": null,
      "weight": 0.3
     },
     {
      "test_case_id": "test_1",
      "passed": false,
      "actual_output": "[1]",
      "expected_output": "[1, 2]",
      "execution_time": 0.08,
      "memory_usage": 1536,
      "error_message": null,
      "weight": 0.4
     },
     {
      "test_case_id": "test_2",
      "passed": true,
      "actual_output": "[]",
      "expected_output": "[]",
      "execution_time": 0.03,
      "memory_usage": 512,
      "error_message": null,
      "weight": 0.3
     }
    ],
    "passed_tests": 2,
    "total_tests": 3,
    "execution_summary": {
     "total_execution_time": 0.23,
     "average_execution_time": 0.077,
     "total_memory_usage": 4096
    }
   },
   "ai_detection": {
    "ai_generated_probability": 0.25,
    "detection_method": "pattern_matching",
    "flagged_patterns": [
     "generic_variable_names: 3 instances",
     "verbose_comments: 0 instances"
    ],
    "confidence_level": "low",
    "risk_assessment": "minimal"
   },
   "code_quality": {
    "cyclomatic_complexity": 2.0,
    "maintainability_index": 85.0,
    "halstead_volume": null,
    "comment_ratio": 0.0,
    "function_count": 1,
    "line_count": 8,
    "quality_score": 0.75,
    "quality_grade": "B"
   },
   "performance": {
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "efficiency_score": 0.85,
    "performance_issues": [],
    "optimization_suggestions": [
     "Consider using collections.Counter for counting duplicates"
    ]
   },
   "style": {
    "style_score": 0.7,
    "style_violations": [
     {
      "type": "missing_docstring",
      "line_number": 1,
      "description": "Function missing docstring",
      "severity": "warning"
     }
    ],
    "formatting_issues": ["Missing docstring", "Could benefit from type hints"],
    "best_practices_followed": [
     "Clear variable names",
     "Proper use of sets for efficiency"
    ],
    "improvement_suggestions": [
     "Add docstring explaining the function",
     "Add type hints for parameters and return value",
     "Consider edge case handling"
    ]
   },
   "naming": {
    "naming_score": 0.8,
    "naming_issues": [
     {
      "variable_name": "num",
      "issue_type": "generic_name",
      "suggestion": "Consider more descriptive name like 'element' or 'value'",
      "line_number": 4
     }
    ],
    "conventions_followed": [
     "snake_case function name",
     "Descriptive parameter name"
    ],
    "improvement_suggestions": ["Use more descriptive variable names"]
   },
   "question_score": 0.71,
   "weighted_score": 0.71
  }
 ],
 "regular_analysis": [
  {
   "question_id": "1",
   "question_type": "MCQ",
   "submitted_answer": "q1_a",
   "correct_answer": "q1_b",
   "is_correct": false,
   "score": 0.0
  },
  {
   "question_id": "2",
   "question_type": "MCQ",
   "submitted_answer": "q2_c",
   "correct_answer": "q2_c",
   "is_correct": true,
   "score": 1.0
  },
  {
   "question_id": "51",
   "question_type": "OPEN_ENDED",
   "submitted_answer": "Lists are mutable and can be modified after creation, while tuples are immutable and cannot be changed. Lists use square brackets [] while tuples use parentheses ().",
   "correct_answer": null,
   "is_correct": true,
   "score": 0.85,
   "quality_assessment": {
    "completeness": 0.8,
    "accuracy": 0.9,
    "clarity": 0.85,
    "depth": 0.7,
    "overall_quality": 0.81
   }
  }
 ],
 "summary": {
  "strengths": [
   "Strong understanding of Python string manipulation",
   "Efficient use of data structures (sets)",
   "Clean and readable code structure",
   "Good performance in most test cases"
  ],
  "weaknesses": [
   "Missing documentation (docstrings)",
   "Some test case failures in complex scenarios",
   "Limited error handling",
   "Could improve variable naming consistency"
  ],
  "recommendations": [
   "Add comprehensive docstrings to all functions",
   "Include type hints for better code documentation",
   "Test edge cases more thoroughly",
   "Consider adding input validation",
   "Review failed test cases and fix logic issues"
  ],
  "overall_feedback": "Good foundational programming skills with room for improvement in documentation and edge case handling. The candidate demonstrates solid understanding of Python fundamentals and efficient algorithm design.",
  "score_breakdown": {
   "correctness": 0.84,
   "ai_detection": 0.8,
   "code_quality": 0.8,
   "performance": 0.88,
   "style": 0.75,
   "naming": 0.85,
   "regular_questions": 0.62
  },
  "time_analysis": {
   "total_time_taken": 3264,
   "time_per_question": {
    "52": 420,
    "53": 380,
    "1": 45,
    "2": 60,
    "51": 180
   },
   "efficiency_rating": "good"
  }
 }
}
```

## Frontend Display Recommendations

### 1. Analysis Dashboard Overview

```typescript
// Main dashboard component props
interface AnalysisDashboardProps {
 analysis: AnalysisSolution;
}

// Key metrics to display prominently
const keyMetrics = {
 overallScore: analysis.overall_score,
 grade: analysis.grade,
 totalQuestions:
  analysis.coding_analysis.length + analysis.regular_analysis.length,
 passedTests: analysis.coding_analysis.reduce(
  (sum, q) => sum + q.correctness.passed_tests,
  0
 ),
 totalTests: analysis.coding_analysis.reduce(
  (sum, q) => sum + q.correctness.total_tests,
  0
 ),
 aiRiskLevel: Math.max(
  ...analysis.coding_analysis.map(
   (q) => q.ai_detection.ai_generated_probability
  )
 ),
};
```

### 2. Score Visualization Components

#### Overall Score Card

```jsx
<ScoreCard
 score={analysis.overall_score}
 grade={analysis.grade}
 title="Overall Performance"
/>
```

#### Score Breakdown Chart

```jsx
<RadarChart data={analysis.summary.score_breakdown} />
// or
<BarChart data={analysis.summary.score_breakdown} />
```

### 3. Coding Questions Analysis Display

#### Question Summary Cards

```jsx
{
 analysis.coding_analysis.map((question) => (
  <QuestionCard key={question.question_id}>
   <QuestionHeader
    title={question.question_title}
    language={question.language}
    score={question.question_score}
   />
   <TestResults results={question.correctness.test_case_results} />
   <CodeQualityMetrics metrics={question.code_quality} />
   <AIDetectionAlert detection={question.ai_detection} />
  </QuestionCard>
 ));
}
```

#### Test Case Results Table

```jsx
<TestResultsTable>
 {question.correctness.test_case_results.map((test) => (
  <TestRow
   key={test.test_case_id}
   passed={test.passed}
   expected={test.expected_output}
   actual={test.actual_output}
   executionTime={test.execution_time}
   memoryUsage={test.memory_usage}
  />
 ))}
</TestResultsTable>
```

### 4. Code Quality Visualization

#### Quality Metrics Dashboard

```jsx
<QualityMetrics>
 <MetricCard
  title="Maintainability Index"
  value={question.code_quality.maintainability_index}
  max={100}
  color="green"
 />
 <MetricCard
  title="Cyclomatic Complexity"
  value={question.code_quality.cyclomatic_complexity}
  threshold={10}
  color="orange"
 />
 <MetricCard
  title="Comment Ratio"
  value={question.code_quality.comment_ratio * 100}
  suffix="%"
  color="blue"
 />
</QualityMetrics>
```

### 5. AI Detection Warning System

#### Risk Assessment Display

```jsx
<AIDetectionPanel>
 <RiskLevel level={question.ai_detection.risk_assessment} />
 <ProbabilityMeter value={question.ai_detection.ai_generated_probability} />
 <FlaggedPatterns patterns={question.ai_detection.flagged_patterns} />
</AIDetectionPanel>
```

### 6. Performance Analysis

#### Performance Metrics

```jsx
<PerformanceAnalysis>
 <ComplexityBadge
  time={question.performance.time_complexity}
  space={question.performance.space_complexity}
 />
 <EfficiencyScore score={question.performance.efficiency_score} />
 <OptimizationSuggestions
  suggestions={question.performance.optimization_suggestions}
 />
</PerformanceAnalysis>
```

### 7. Style and Naming Analysis

#### Code Style Review

```jsx
<StyleAnalysis>
 <StyleScore score={question.style.style_score} />
 <ViolationsList violations={question.style.style_violations} />
 <ImprovementSuggestions suggestions={question.style.improvement_suggestions} />
</StyleAnalysis>
```

### 8. Summary and Recommendations

#### Analysis Summary

```jsx
<AnalysisSummary>
 <StrengthsList strengths={analysis.summary.strengths} />
 <WeaknessesList weaknesses={analysis.summary.weaknesses} />
 <RecommendationsList recommendations={analysis.summary.recommendations} />
 <OverallFeedback feedback={analysis.summary.overall_feedback} />
</AnalysisSummary>
```

### 9. Time Analysis

#### Time Efficiency Display

```jsx
<TimeAnalysis>
 <TotalTime time={analysis.summary.time_analysis.total_time_taken} />
 <TimePerQuestion data={analysis.summary.time_analysis.time_per_question} />
 <EfficiencyRating rating={analysis.summary.time_analysis.efficiency_rating} />
</TimeAnalysis>
```

### 10. Color Coding Guidelines

```css
/* Score-based color coding */
.score-excellent {
 color: #22c55e;
} /* 90-100% */
.score-good {
 color: #84cc16;
} /* 80-89% */
.score-average {
 color: #eab308;
} /* 70-79% */
.score-poor {
 color: #f97316;
} /* 60-69% */
.score-failing {
 color: #ef4444;
} /* 0-59% */

/* AI Detection risk levels */
.risk-minimal {
 color: #22c55e;
}
.risk-moderate {
 color: #eab308;
}
.risk-high {
 color: #f97316;
}
.risk-critical {
 color: #ef4444;
}

/* Test result indicators */
.test-passed {
 background: #dcfce7;
 color: #166534;
}
.test-failed {
 background: #fef2f2;
 color: #dc2626;
}
```

This schema provides a comprehensive structure for displaying analysis results in your frontend, with clear component suggestions and styling guidelines.
