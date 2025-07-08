#!/bin/bash

# Script to manage predefined coding questions in the assessment database
# Supports loading, dropping, and managing the predefined_questions collection

# Set environment variables
export PYTHONPATH=$(pwd)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to show usage
show_usage() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  load              Load predefined questions into database"
    echo "  drop              Drop the predefined_questions collection"
    echo "  reload            Drop existing collection and reload questions"
    echo "  status            Show status of predefined_questions collection"
    echo "  help              Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 load           # Load all 42 predefined questions"
    echo "  $0 reload         # Drop and reload questions"
    echo "  $0 drop           # Drop the collection"
    echo "  $0 status         # Show collection status"
}

# Function to check if MongoDB is running
check_mongodb() {
    print_info "Checking MongoDB connection..."

    # Try to connect to MongoDB using Python
    python3 -c "
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from server.services.database_service import DatabaseService
    db_service = DatabaseService()
    db_service.db.admin.command('ping')
    print('MongoDB connection successful')
except Exception as e:
    print(f'MongoDB connection failed: {e}')
    sys.exit(1)
" 2>/dev/null

    if [ $? -eq 0 ]; then
        print_success "MongoDB is running and accessible"
        return 0
    else
        print_error "MongoDB is not running or not accessible"
        print_info "Please ensure MongoDB is running and the connection settings are correct"
        return 1
    fi
}



# Function to get collection status
get_collection_status() {
    print_info "Getting collection status..."

    python3 -c "
import sys
sys.path.append('.')
try:
    from server.services.database_service import DatabaseService
    db_service = DatabaseService()

    collection = db_service.db['predefined_questions']
    count = collection.count_documents({})

    if count > 0:
        print(f'Collection exists with {count} documents')

        # Get sample data
        sample = collection.find_one()
        if sample:
            print(f'Sample document ID: {sample.get(\"id\", \"N/A\")}')
            print(f'Sample title: {sample.get(\"title\", \"N/A\")}')

        # Get statistics by topic
        pipeline = [
            {'\$group': {'_id': '\$metadata.topic', 'count': {'\$sum': 1}}},
            {'\$sort': {'_id': 1}}
        ]
        topics = list(collection.aggregate(pipeline))
        if topics:
            print('Questions by topic:')
            for topic in topics:
                print(f'  {topic[\"_id\"]}: {topic[\"count\"]} questions')

        # Get statistics by difficulty
        pipeline = [
            {'\$group': {'_id': '\$metadata.difficulty', 'count': {'\$sum': 1}}},
            {'\$sort': {'_id': 1}}
        ]
        difficulties = list(collection.aggregate(pipeline))
        if difficulties:
            print('Questions by difficulty:')
            for diff in difficulties:
                print(f'  {diff[\"_id\"]}: {diff[\"count\"]} questions')
    else:
        print('Collection is empty or does not exist')

except Exception as e:
    print(f'Error getting collection status: {e}')
    sys.exit(1)
"
}

# Function to load questions
load_questions() {
    print_info "Loading predefined questions..."
    print_info "Loading all 42 questions from embedded data..."

    # Check prerequisites
    if ! check_mongodb; then
        return 1
    fi

    # Run the Python script
    print_info "Executing Python script to load questions..."
    python3 scripts/load_predefined_questions.py

    if [ $? -eq 0 ]; then
        print_success "Questions loaded successfully!"
        echo ""
        get_collection_status
        return 0
    else
        print_error "Failed to load questions"
        return 1
    fi
}

# Function to drop collection
drop_collection() {
    print_warning "This will permanently delete all predefined questions from the database!"
    read -p "Are you sure you want to continue? (y/N): " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        print_info "Dropping predefined_questions collection..."

        python3 -c "
import sys
sys.path.append('.')
try:
    from server.services.database_service import DatabaseService
    db_service = DatabaseService()

    collection = db_service.db['predefined_questions']
    count_before = collection.count_documents({})

    if count_before > 0:
        collection.drop()
        print(f'Dropped collection with {count_before} documents')
    else:
        print('Collection was already empty or did not exist')

except Exception as e:
    print(f'Error dropping collection: {e}')
    sys.exit(1)
"

        if [ $? -eq 0 ]; then
            print_success "Collection dropped successfully!"
        else
            print_error "Failed to drop collection"
            return 1
        fi
    else
        print_info "Operation cancelled"
    fi
}

# Function to reload questions (drop and load)
reload_questions() {
    print_info "Reloading predefined questions (drop and load)..."
    print_info "Reloading all 42 questions from embedded data..."

    # Check prerequisites
    if ! check_mongodb; then
        return 1
    fi

    # Run the Python script with drop flag
    print_info "Executing Python script to reload questions..."
    python3 scripts/load_predefined_questions.py --drop-existing

    if [ $? -eq 0 ]; then
        print_success "Questions reloaded successfully!"
        echo ""
        get_collection_status
        return 0
    else
        print_error "Failed to reload questions"
        return 1
    fi
}

# Main script logic
main() {
    # Check if no arguments provided
    if [ $# -eq 0 ]; then
        print_error "No command provided"
        show_usage
        exit 1
    fi

    # Parse command
    COMMAND=$1
    shift

    # Check for unexpected arguments
    if [ $# -gt 0 ]; then
        print_error "Unexpected arguments: $*"
        show_usage
        exit 1
    fi

    # Execute command
    case $COMMAND in
        load)
            load_questions
            ;;
        drop)
            drop_collection
            ;;
        reload)
            reload_questions
            ;;
        status)
            if check_mongodb; then
                get_collection_status
            fi
            ;;
        help)
            show_usage
            ;;
        *)
            print_error "Unknown command: $COMMAND"
            show_usage
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"
