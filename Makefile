.PHONY: help up down build restart logs clean test lint format ps shell-api shell-worker

# Default target
help:
	@echo "📋 Text Summarizer - Available Commands"
	@echo ""
	@echo "🚀 Development:"
	@echo "  make up          - Start all services"
	@echo "  make down        - Stop all services"
	@echo "  make restart     - Restart all services"
	@echo "  make build       - Build all containers"
	@echo "  make ps          - Show running containers"
	@echo ""
	@echo "📊 Monitoring:"
	@echo "  make logs        - View logs (all services)"
	@echo "  make logs-api    - View API Gateway logs"
	@echo "  make logs-worker - View Worker logs"
	@echo ""
	@echo "🧹 Maintenance:"
	@echo "  make clean       - Remove containers, volumes, and database"
	@echo "  make clean-all   - Remove everything including images"
	@echo ""
	@echo "🔧 Utilities:"
	@echo "  make shell-api   - Open shell in API container"
	@echo "  make shell-worker- Open shell in Worker container"
	@echo "  make test        - Run tests"
	@echo "  make lint        - Run linter"
	@echo "  make format      - Format code"

# Start services
up:
	@echo "🚀 Starting Text Summarizer services..."
	docker-compose up -d
	@echo "✅ Services started!"
	@echo "🌐 Open http://localhost:8000 in your browser"

# Stop services
down:
	@echo "🛑 Stopping services..."
	docker-compose down
	@echo "✅ Services stopped!"

# Build containers
build:
	@echo "🔨 Building containers..."
	docker-compose build
	@echo "✅ Build complete!"

# Restart services
restart: down up

# View logs
logs:
	docker-compose logs -f

logs-api:
	docker-compose logs -f api-gateway

logs-worker:
	docker-compose logs -f worker

# Show running containers
ps:
	docker-compose ps

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	docker-compose down -v
	rm -f api_gateway/tasks.db
	rm -rf api_gateway/__pycache__ worker/__pycache__
	@echo "✅ Cleanup complete!"

clean-all: clean
	@echo "🗑️  Removing all images..."
	docker-compose down -v --rmi all
	@echo "✅ Everything cleaned!"

# Shell access
shell-api:
	docker-compose exec api-gateway /bin/sh

shell-worker:
	docker-compose exec worker /bin/sh

# Testing
test:
	@echo "🧪 Running tests..."
	pytest tests/ -v

test-cov:
	@echo "🧪 Running tests with coverage..."
	pytest tests/ --cov=. --cov-report=html --cov-report=term
	@echo "📊 Coverage report generated in htmlcov/index.html"

test-watch:
	@echo "🧪 Running tests in watch mode..."
	pytest-watch tests/

test-unit:
	@echo "🧪 Running unit tests only..."
	pytest tests/ -v -m "not integration"

test-integration:
	@echo "🧪 Running integration tests..."
	pytest tests/ -v -m integration

# Linting
lint:
	@echo "🔍 Running linter..."
	@echo "⚠️  Install: pip install flake8 black mypy"
	-flake8 api_gateway/ worker/ --max-line-length=100
	-mypy api_gateway/ worker/ --ignore-missing-imports

# Format code
format:
	@echo "✨ Formatting code..."
	@echo "⚠️  Install: pip install black"
	-black api_gateway/ worker/ tests/

# Development setup
setup:
	@echo "⚙️  Setting up development environment..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "✅ Created .env file from .env.example"; \
		echo "📝 Please edit .env and add your API keys"; \
	else \
		echo "ℹ️  .env file already exists"; \
	fi
	@echo "✅ Setup complete! Run 'make up' to start services"

# Quick start (setup + build + up)
start: setup build up
	@echo ""
	@echo "🎉 Text Summarizer is now running!"
	@echo "🌐 Visit: http://localhost:8000"
	@echo "📊 View logs: make logs"
	@echo "🛑 Stop services: make down"
