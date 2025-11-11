# 🤝 Contributing to Text Summarizer

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Submitting Changes](#submitting-changes)

---

## 📜 Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Git
- Basic knowledge of FastAPI, Redis, and async Python

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/TextSummarizer.git
   cd TextSummarizer
   ```
3. **Add upstream remote:**
   ```bash
   git remote add upstream https://github.com/loguntsov-ae/TextSummarizer.git
   ```

---

## 🛠️ Development Setup

### Quick Start

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
nano .env

# Start services
make up

# View logs
make logs
```

### Manual Setup (without Docker)

**Terminal 1 - Redis:**
```bash
docker run -p 6379:6379 redis:7-alpine
```

**Terminal 2 - API Gateway:**
```bash
cd api_gateway
pip install -e .
uvicorn main:app --reload --port 8000
```

**Terminal 3 - Worker:**
```bash
cd worker
pip install -e .
python main.py
```

---

## 🎯 How to Contribute

### Types of Contributions

We welcome various types of contributions:

#### 🐛 Bug Reports
- Use GitHub Issues
- Describe the bug clearly
- Include steps to reproduce
- Mention your environment (OS, Python version)

#### ✨ Feature Requests
- Open a GitHub Issue with `[Feature Request]` tag
- Describe the feature and its use case
- Discuss implementation approach

#### 📝 Documentation
- Fix typos or unclear sections
- Add examples or tutorials
- Improve API documentation

#### 💻 Code Contributions
- Bug fixes
- New features
- Performance improvements
- Tests

---

## 🎨 Coding Standards

### Python Style

Follow **PEP 8** guidelines:

```python
# Good
async def summarize_text(text: str) -> str:
    """Summarize the given text."""
    result = await model.process(text)
    return result

# Bad
async def summarizetext(text):
    result=await model.process(text)
    return result
```

### Type Hints

Always use type hints:

```python
from typing import List, Optional

def get_tasks(limit: Optional[int] = None) -> List[Task]:
    """Get all tasks with optional limit."""
    ...
```

### Async/Await

Use async properly:

```python
# Good
async def process_task(task_id: str) -> None:
    task = await db.get_task(task_id)
    result = await model.summarize(task.text)
    await db.update_task(task_id, result)

# Bad - blocking call in async function
async def process_task(task_id: str) -> None:
    result = blocking_api_call()  # ❌
```

### Naming Conventions

- **Functions/methods:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`
- **Private:** `_leading_underscore`

```python
class TaskRepository:
    MAX_RETRIES = 3
    
    def __init__(self):
        self._connection = None
    
    async def get_task(self, task_id: str) -> Task:
        ...
```

---

## 🧪 Testing

### Writing Tests

```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/summarize",
        json={"text": "Test text"}
    )
    assert response.status_code == 200
    assert "task_id" in response.json()

@pytest.mark.asyncio
async def test_summarize():
    repo = OpenAIRepository()
    result = await repo.summarize("Test text")
    assert len(result) > 0
```

### Running Tests

```bash
# Run all tests
make test

# Run specific test file
pytest tests/test_api.py

# Run with coverage
pytest --cov=. tests/
```

---

## 📤 Submitting Changes

### Workflow

1. **Create a branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes:**
   - Write code
   - Add tests
   - Update documentation

3. **Commit with clear messages:**
   ```bash
   git add .
   git commit -m "feat: add batch processing endpoint"
   ```

### Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <description>

[optional body]

[optional footer]
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Build/tooling changes

**Examples:**
```bash
feat: add PostgreSQL support
fix: handle WebSocket reconnection properly
docs: update API examples in README
refactor: extract Redis client to separate module
```

### Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Ensure tests pass:**
   ```bash
   make test
   make lint
   ```

4. **Push to your fork:**
   ```bash
   git push origin feature/amazing-feature
   ```

5. **Create Pull Request** on GitHub:
   - Clear title and description
   - Link related issues
   - Mention breaking changes

6. **Address review comments:**
   - Make requested changes
   - Push updates to the same branch

7. **Wait for approval** and merge

---

## 🗂️ Project Structure

Understanding the structure helps you contribute:

```
TextSummarizer/
├── api_gateway/          # FastAPI application
│   ├── main.py          # Entry point, routes
│   ├── db.py            # Database models
│   ├── schemas.py       # Pydantic models
│   └── redis_client.py  # Redis Pub/Sub
│
├── worker/              # Background worker
│   ├── main.py         # Worker entry point
│   └── domain/         # Business logic
│       ├── factory.py  # Model factory
│       ├── interfaces.py
│       └── repositories/  # ML model implementations
│
├── tests/              # Test suite (to be added)
├── docs/               # Additional documentation
└── docker-compose.yml  # Service orchestration
```

---

## 🐛 Debugging Tips

### Enable Debug Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Task received: %s", task_id)
```

### Docker Logs

```bash
# All services
make logs

# Specific service
docker-compose logs -f api-gateway
docker-compose logs -f worker
```

### Interactive Debugging

Add breakpoint in code:

```python
import pdb; pdb.set_trace()  # Python debugger
```

Or use IDE debugger (VSCode, PyCharm)

---

## 💡 Development Tips

### Hot Reload

Both services support hot reload:
- **API Gateway:** Uvicorn auto-reloads on file changes
- **Worker:** Restart required (or use `watchdog`)

### Quick Iteration

```bash
# Rebuild single service
docker-compose up -d --build api-gateway

# Restart without rebuild
docker-compose restart worker

# View real-time logs
make logs-api
```

### Database Reset

```bash
# Clear database
rm api_gateway/tasks.db

# Restart to recreate
make restart
```

---

## 📚 Resources

### Learning Materials

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Redis Pub/Sub Guide](https://redis.io/docs/manual/pubsub/)
- [Python Asyncio](https://docs.python.org/3/library/asyncio.html)
- [Docker Compose](https://docs.docker.com/compose/)

### Project Documentation

- [README.md](README.md) - Overview and quick start
- [ARCHITECTURE.md](ARCHITECTURE.md) - Detailed architecture
- [API_EXAMPLES.md](API_EXAMPLES.md) - API usage examples

---

## ❓ Questions?

- **General questions:** Open a GitHub Discussion
- **Bug reports:** Open a GitHub Issue
- **Security issues:** Email directly (see README)

---

## 🎉 Recognition

Contributors will be recognized in:
- GitHub Contributors page
- Release notes
- README acknowledgments

Thank you for contributing! 🙏
