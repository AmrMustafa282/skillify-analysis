#!/usr/bin/env python3
"""
Script to load predefined coding questions into the assessment database.
Contains all 42 predefined questions with implementations in 6 programming languages.
This script is self-contained and doesn't depend on external TypeScript files.
"""

import os
import sys
import argparse
from datetime import datetime
from typing import List, Dict, Any

# Add the parent directory to the path so we can import the server modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.services.database_service import DatabaseService
from scripts.predefined_questions_data import get_all_questions

# Configure argument parser
parser = argparse.ArgumentParser(description='Load predefined coding questions into the assessment database')
parser.add_argument('--drop-existing', action='store_true', help='Drop existing predefined_questions collection before loading data')
args = parser.parse_args()

# Initialize database service
db_service = DatabaseService()

def get_all_predefined_questions() -> List[Dict[str, Any]]:
    """
    Returns all predefined coding questions with complete implementations.
    Each question includes implementations in Python, JavaScript, Java, Go, Ruby, and C++.
    """
    return get_all_questions()

def add_timestamps_to_questions(questions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Add timestamps to each question."""
    current_time = datetime.now().isoformat()

    for question in questions:
        question['createdAt'] = current_time
        question['updatedAt'] = current_time

    return questions

def load_questions_to_database(questions: List[Dict[str, Any]]) -> None:
    """
    Load questions into MongoDB database.
    """
    print(f"Loading {len(questions)} questions into predefined_questions collection...")

    # Add timestamps
    questions_with_timestamps = add_timestamps_to_questions(questions)

    # Use the database service method to store questions
    if questions_with_timestamps:
        success = db_service.store_predefined_questions(questions_with_timestamps)

        if success:
            print(f"Successfully inserted {len(questions_with_timestamps)} questions")

            # Create indexes for better query performance
            print("Creating indexes...")
            collection = db_service.get_collection("predefined_questions")
            collection.create_index("id", unique=True)
            collection.create_index("metadata.difficulty")
            collection.create_index("metadata.topic")
            collection.create_index("metadata.tags")
            collection.create_index("metadata.companies")
            print("Indexes created successfully")
        else:
            print("Failed to insert questions")
    else:
        print("No questions to insert")

def print_summary(questions: List[Dict[str, Any]]) -> None:
    """Print a summary of the loaded questions."""
    print("\n" + "="*50)
    print("LOADING SUMMARY")
    print("="*50)
    print(f"Total questions loaded: {len(questions)}")

    # Group by topic
    topics = {}
    for question in questions:
        topic = question.get('metadata', {}).get('topic', 'Unknown')
        if topic not in topics:
            topics[topic] = 0
        topics[topic] += 1

    print("\nQuestions by topic:")
    for topic, count in sorted(topics.items()):
        print(f"  {topic}: {count} questions")

    # Group by difficulty
    difficulties = {}
    for question in questions:
        difficulty = question.get('metadata', {}).get('difficulty', 'Unknown')
        if difficulty not in difficulties:
            difficulties[difficulty] = 0
        difficulties[difficulty] += 1

    print("\nQuestions by difficulty:")
    for difficulty, count in sorted(difficulties.items()):
        print(f"  {difficulty}: {count} questions")

    # Group by language
    languages = set()
    for question in questions:
        for impl in question.get('implementations', []):
            languages.add(impl.get('language', 'Unknown'))

    print(f"\nSupported languages: {', '.join(sorted(languages))}")
    print("="*50)

def main():
    """Main function to orchestrate the loading process."""
    try:
        print("Starting predefined questions loading process...")
        print(f"Drop existing: {args.drop_existing}")

        # Get predefined questions
        questions = get_all_predefined_questions()

        # Load questions into database
        load_questions_to_database(questions)

        print("Predefined questions loading completed successfully!")

        # Print summary
        print_summary(questions)

    except Exception as e:
        print(f"Error during loading process: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
