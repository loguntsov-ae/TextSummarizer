FROM python:3.11-slim

WORKDIR /app

# Устанавливаем uv
RUN pip install uv

# Копируем pyproject.toml и lock
COPY pyproject.toml uv.lock* ./

# Устанавливаем зависимости
RUN uv sync --frozen || uv sync

# Копируем остальной код
COPY . .

# Запускаем FastAPI через uv
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]