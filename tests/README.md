# Tests

This directory contains unit and integration tests for the Text Summarizer project.

## Structure

```
tests/
├── __init__.py
├── conftest.py           # Pytest configuration and fixtures
├── test_api.py           # API Gateway tests
├── test_worker.py        # Worker tests
└── test_repositories.py  # Repository tests
```

## Running Tests

### All tests:
```bash
pytest
```

### With coverage:
```bash
pytest --cov=. --cov-report=html
```

### Specific test file:
```bash
pytest tests/test_api.py
```

### Specific test:
```bash
pytest tests/test_api.py::test_create_task
```

## Requirements

Install test dependencies:
```bash
pip install pytest pytest-asyncio pytest-cov httpx
```
