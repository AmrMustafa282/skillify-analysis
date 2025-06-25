#!/bin/bash

# Script to load predefined questions into the assessment database

echo "🚀 Loading predefined questions into MongoDB..."

# Set environment variables
export PYTHONPATH=$(pwd)

# Check if the --drop-existing flag is provided
if [ "$1" == "--drop-existing" ]; then
    echo "Running with --drop-existing flag to drop existing collections..."
    python scripts/load_predefined_questions.py --drop-existing
else
    echo "Running without --drop-existing flag..."
    python scripts/load_predefined_questions.py
fi

# Check if the Python script executed successfully
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Predefined questions loading complete!"
    echo "📊 44 questions loaded successfully into MongoDB"
    echo "🎯 Ready for use in the assessment platform"
    echo ""
    echo "🔗 API Endpoints now available:"
    echo "   • GET /api/predefined-questions"
    echo "   • GET /api/predefined-questions/{id}"
    echo "   • GET /api/predefined-questions/topics"
    echo "   • GET /api/predefined-questions/languages"
    echo ""
    echo "📝 Usage Examples:"
    echo "   Linux:   ./scripts/load_predefined_questions.sh"
    echo "   Linux:   ./scripts/load_predefined_questions.sh --drop-existing"
    echo "   Python:  python scripts/load_predefined_questions.py"
else
    echo ""
    echo "❌ Error loading predefined questions"
    echo "Please check the error messages above"
    exit 1
fi
