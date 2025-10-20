FROM python:3.11-slim

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

CMD ["uv", "run", "python", "main.py"]