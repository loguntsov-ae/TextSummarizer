#!/bin/bash
# Script to run tests locally

set -e

echo "🧪 Setting up test environment..."

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo -e "${YELLOW}pytest not found. Installing test dependencies...${NC}"
    pip install -r requirements-test.txt
fi

# Check if Redis is running
if ! nc -z localhost 6379 2>/dev/null; then
    echo -e "${YELLOW}⚠️  Redis not running on localhost:6379${NC}"
    echo "Starting Redis with Docker..."
    docker run -d --name test-redis -p 6379:6379 redis:7-alpine
    sleep 2
fi

# Set test environment variables
export REDIS_URL="redis://localhost:6379"
export DATABASE_URL="sqlite:///./test.db"
export MODEL_BACKEND="huggingface"

# Clean up old test database
rm -f test.db 2>/dev/null || true

echo ""
echo -e "${GREEN}🚀 Running tests...${NC}"
echo ""

# Run tests
if pytest tests/ -v --cov=. --cov-report=term-missing -m "not integration"; then
    echo ""
    echo -e "${GREEN}✅ All tests passed!${NC}"
    exit 0
else
    echo ""
    echo -e "${RED}❌ Some tests failed!${NC}"
    exit 1
fi
