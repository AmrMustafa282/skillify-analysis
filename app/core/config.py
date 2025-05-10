"""
Configuration module for the application.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://admin:password@localhost:27017/assessment_db")
DATABASE_NAME = os.getenv("DATABASE_NAME", "assessment_db")

# Collections
ASSESSMENTS_COLLECTION = "assessments"
SOLUTIONS_COLLECTION = "solutions"
ANALYSIS_COLLECTION = "analysis"
REPORTS_COLLECTION = "reports"

# Analysis Configuration
ANALYSIS_CONFIG = {
    "coding": {
        "correctness_weight": 0.4,
        "ai_detection_weight": 0.1,
        "code_quality_weight": 0.2,
        "performance_weight": 0.2,
        "style_weight": 0.1,
    },
    "mcq": {
        "correctness_weight": 1.0,
    },
    "open_ended": {
        "relevance_weight": 0.6,
        "clarity_weight": 0.4,
    }
}
