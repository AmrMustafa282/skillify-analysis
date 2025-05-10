"""
Assessment Analysis Server

This server retrieves assessments and solutions from MongoDB,
analyzes the solutions, and stores the analysis results back in MongoDB.
"""
import argparse
import logging
from server.services.database_service import DatabaseService
from server.services.analysis_service import AnalysisService
from server.services.reporting_service import ReportingService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function to run the server."""
    parser = argparse.ArgumentParser(description="Assessment Analysis Server")
    parser.add_argument("--test-id", help="Process a specific test ID")
    parser.add_argument("--solution-id", help="Process a specific solution ID")
    parser.add_argument("--analyze-all", action="store_true", help="Analyze all unprocessed solutions")
    parser.add_argument("--generate-reports", action="store_true", help="Generate reports for analyzed solutions")
    parser.add_argument("--load-sample-data", action="store_true", help="Load sample data into the database")
    parser.add_argument("--sample-data-dir", default="sample_data", help="Directory containing sample data files")
    parser.add_argument("--drop-existing", action="store_true", help="Drop existing collections before loading sample data")
    args = parser.parse_args()

    # Initialize services
    db_service = DatabaseService()
    analysis_service = AnalysisService(db_service)
    reporting_service = ReportingService(db_service)

    # Load sample data if requested
    if args.load_sample_data:
        logger.info("Loading sample data...")
        db_service.load_sample_data(args.sample_data_dir, args.drop_existing)

    if args.test_id:
        # Process all solutions for a specific test
        logger.info(f"Processing solutions for test ID: {args.test_id}")
        solutions = db_service.get_solutions_by_test_id(args.test_id)

        if not solutions:
            logger.warning(f"No solutions found for test ID: {args.test_id}")
            return

        logger.info(f"Found {len(solutions)} solutions for test ID: {args.test_id}")

        for solution in solutions:
            process_solution(solution, db_service, analysis_service)

        # Generate reports for the test
        if args.generate_reports:
            logger.info(f"Generating reports for test ID: {args.test_id}")
            reporting_service.generate_test_report(args.test_id)

    elif args.solution_id:
        # Process a specific solution
        logger.info(f"Processing solution ID: {args.solution_id}")
        solution = db_service.get_solution_by_id(args.solution_id)

        if not solution:
            logger.warning(f"Solution not found: {args.solution_id}")
            return

        process_solution(solution, db_service, analysis_service)

        # Generate report for the solution
        if args.generate_reports:
            logger.info(f"Generating report for solution ID: {args.solution_id}")
            reporting_service.generate_solution_report(args.solution_id)

    elif args.analyze_all:
        # Process all unprocessed solutions
        logger.info("Processing all unprocessed solutions")
        solutions = db_service.get_unprocessed_solutions()

        if not solutions:
            logger.warning("No unprocessed solutions found")
            return

        logger.info(f"Found {len(solutions)} unprocessed solutions")

        for solution in solutions:
            process_solution(solution, db_service, analysis_service)

        # Generate reports for all tests with processed solutions
        if args.generate_reports:
            logger.info("Generating reports for all tests with processed solutions")
            test_ids = db_service.get_tests_with_processed_solutions()

            for test_id in test_ids:
                reporting_service.generate_test_report(test_id)

    else:
        logger.info("No action specified. Use --test-id, --solution-id, or --analyze-all")
        parser.print_help()

def process_solution(solution, db_service, analysis_service):
    """Process a single solution.

    Args:
        solution: Solution document from MongoDB
        db_service: Database service
        analysis_service: Analysis service
    """
    solution_id = solution.get("solution_id")
    test_id = solution.get("test_id")

    # Check if solution has already been analyzed
    existing_analysis = db_service.get_analysis_by_solution_id(solution_id)
    if existing_analysis:
        logger.info(f"Solution {solution_id} has already been analyzed. Skipping.")
        return

    # Get the assessment for this solution
    assessment = db_service.get_assessment_by_id(test_id)
    if not assessment:
        logger.warning(f"Assessment not found for test ID: {test_id}")
        return

    # Analyze the solution
    logger.info(f"Analyzing solution: {solution_id}")
    analysis_result = analysis_service.analyze_solution(solution, assessment)

    # Store the analysis result
    analysis_id = db_service.store_analysis(analysis_result)
    logger.info(f"Analysis stored with ID: {analysis_id}")

if __name__ == "__main__":
    main()
