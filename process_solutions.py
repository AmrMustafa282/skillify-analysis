"""
Script to process multiple solutions and generate a comparative report.
"""
import json
import sys
from app.main import (
    setup_mongodb,
    load_assessment,
    load_solution,
    store_assessment,
    store_solution,
    transform_solution,
    analyze_solution,
    store_analysis,
    rank_candidates,
    generate_report
)

def process_solutions(assessment_path, solution_paths):
    """Process multiple solutions and generate a comparative report.
    
    Args:
        assessment_path: Path to the assessment JSON file
        solution_paths: List of paths to solution JSON files
    """
    # Set up MongoDB
    db = setup_mongodb()
    
    # Load and store assessment
    assessment = load_assessment(assessment_path)
    assessment_id = store_assessment(assessment)
    
    # Process each solution
    analysis_ids = []
    for solution_path in solution_paths:
        print(f"\nProcessing solution: {solution_path}")
        
        # Load and store solution
        solution = load_solution(solution_path)
        solution_id = store_solution(solution)
        
        # Transform solution
        transformed_data = transform_solution(solution, assessment)
        
        # Analyze solution
        analysis = analyze_solution(transformed_data)
        
        # Store analysis
        analysis_id = store_analysis(analysis)
        analysis_ids.append(analysis_id)
    
    # Rank candidates
    ranked_candidates = rank_candidates(assessment.test_id)
    
    # Generate comparative report
    _, comparative_report = generate_report(analysis_ids[0], assessment.test_id, ranked_candidates)
    
    # Print comparative report
    print("\n=== Comparative Report ===")
    print(json.dumps(comparative_report, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_solutions.py <assessment_path> <solution_path1> [<solution_path2> ...]")
        sys.exit(1)
    
    assessment_path = sys.argv[1]
    solution_paths = sys.argv[2:]
    
    process_solutions(assessment_path, solution_paths)
