# 🚀 Getting Started - 5 Minute Guide

Быстрое руководство для запуска Text Summarizer за 5 минут.

---

## ⚡ Super Quick Start

**Минимум 3 команды:**

```bash
cp .env.example .env
make up
open http://localhost:8000
```

✅ Готово! Проект запущен.

---

## 📋 Пошаговая инструкция

### Шаг 1: Проверка требований (30 сек)

Убедитесь что установлены:
- ✅ Docker Desktop
- ✅ Docker Compose
- ✅ Git (для клонирования)

**Проверка:**
```bash
docker --version      # Должно быть >= 20.10
docker-compose --version  # Должно быть >= 1.29
```

### Шаг 2: Клонирование проекта (30 сек)

```bash
git clone https://github.com/loguntsov-ae/TextSummarizer.git
cd TextSummarizer
```

### Шаг 3: Конфигурация (1 мин)

```bash
# Создать .env файл из шаблона
cp .env.example .env

# Открыть для редактирования (опционально)
nano .env
```

**Минимальная конфигурация для локального запуска:**
```env
REDIS_URL=redis://redis:6379
DATABASE_URL=sqlite:///./tasks.db
MODEL_BACKEND=huggingface
```

💡 Для работы с HuggingFace или OpenAI добавьте API ключи позже.

### Шаг 4: Запуск (2 мин)

```bash
# Запустить все сервисы
make up

# Или без Makefile:
docker-compose up -d
```

**Что происходит:**
- 🐳 Загружаются Docker образы
- ⚙️ Запускаются 3 контейнера: Redis, API Gateway, Worker
- 📊 Создается база данных SQLite

### Шаг 5: Проверка (30 сек)

**Откройте в браузере:**
```
http://localhost:8000
```

Вы должны увидеть интерфейс Text Summarizer! 🎉

---

## 🧪 Первый тест

### Через Web UI:

1. Откройте http://localhost:8000
2. Вставьте текст в поле ввода:
   ```
   Artificial intelligence is transforming the world. 
   Machine learning enables computers to learn from data. 
   Deep learning has enabled breakthroughs in many fields.
   ```
3. Нажмите **"Summarize Text"**
4. Дождитесь результата (статус изменится на "done")

### Через API:

```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Artificial intelligence is transforming the world. Machine learning enables computers to learn from data."
  }'
```

**Ответ:**
```json
{
  "task_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "queued"
}
```

### Проверить все задачи:

```bash
curl http://localhost:8000/tasks
```

---

## 🔍 Мониторинг

### Просмотр логов:

```bash
# Все сервисы
make logs

# Только API
make logs-api

# Только Worker
make logs-worker
```

### Проверка статуса контейнеров:

```bash
make ps

# Или:
docker-compose ps
```

**Ожидаемый вывод:**
```
NAME                    STATUS      PORTS
textsummarizer-redis    Up          6379/tcp
textsummarizer-api      Up          8000->8000/tcp
textsummarizer-worker   Up
```

---

## 🛑 Остановка и очистка

### Остановить сервисы:

```bash
make down
```

### Полная очистка (включая данные):

```bash
make clean
```

### Удалить всё (включая образы):

```bash
make clean-all
```

---

## 🐛 Troubleshooting

### Проблема: Порт 8000 занят

**Решение:**
```bash
# Найти процесс
lsof -i :8000

# Убить процесс
kill -9 <PID>

# Или изменить порт в docker-compose.yml:
ports:
  - "8001:8000"  # Вместо 8000:8000
```

### Проблема: Docker образы не загружаются

**Решение:**
```bash
# Проверить Docker daemon
docker info

# Перезапустить Docker Desktop
# macOS: Cmd+Q и запустить снова
# Windows: Restart Docker Desktop
```

### Проблема: Worker не обрабатывает задачи

**Решение:**
```bash
# Проверить логи Worker
make logs-worker

# Проверить что MODEL_BACKEND настроен:
cat .env | grep MODEL_BACKEND

# Перезапустить Worker
docker-compose restart worker
```

### Проблема: Redis connection failed

**Решение:**
```bash
# Проверить что Redis запущен
docker-compose ps redis

# Перезапустить Redis
docker-compose restart redis

# Проверить REDIS_URL в .env
cat .env | grep REDIS_URL
```

---

## ⚙️ Конфигурация ML-моделей

### Вариант 1: HuggingFace (по умолчанию)

```env
MODEL_BACKEND=huggingface
HUGGINGFACE_API_KEY=your_key_here
```

Получить ключ: https://huggingface.co/settings/tokens

### Вариант 2: OpenAI

```env
MODEL_BACKEND=openai
OPENAI_API_KEY=sk-your_key_here
```

Получить ключ: https://platform.openai.com/api-keys

### Вариант 3: Локальная модель (без API ключей)

```env
MODEL_BACKEND=local_t5
```

**Внимание:** Локальная модель требует больше ресурсов.

После изменения конфигурации:
```bash
docker-compose restart worker
```

---

## 📚 Дальнейшие шаги

### Изучите документацию:

- 📖 [README.md](../README.md) - Полное описание проекта
- 🏗️ [ARCHITECTURE.md](../ARCHITECTURE.md) - Архитектура системы
- 📚 [API_EXAMPLES.md](../API_EXAMPLES.md) - Примеры использования API
- 🤝 [CONTRIBUTING.md](../CONTRIBUTING.md) - Как внести вклад

### Попробуйте примеры:

```bash
# См. примеры текстов для тестирования
cat docs/SAMPLE_TEXTS.md
```

### Изучите код:

```
api_gateway/main.py     - FastAPI endpoints
worker/main.py          - Worker process
worker/domain/          - Business logic
```

---

## 🎓 Полезные команды

```bash
# Управление
make up              # Запустить
make down            # Остановить
make restart         # Перезапустить
make build           # Пересобрать образы

# Мониторинг
make logs            # Все логи
make logs-api        # API логи
make logs-worker     # Worker логи
make ps              # Статус контейнеров

# Очистка
make clean           # Очистить данные
make clean-all       # Удалить всё

# Утилиты
make shell-api       # Shell в API контейнере
make shell-worker    # Shell в Worker контейнере
```

---

## ✨ Поздравляем!

Вы успешно запустили Text Summarizer! 🎉

**Следующие шаги:**
1. Протестируйте различные тексты
2. Изучите API через примеры
3. Посмотрите архитектуру
4. Попробуйте изменить код

**Вопросы?**
- GitHub Issues: [создать issue](https://github.com/loguntsov-ae/TextSummarizer/issues)
- Документация: См. README.md

---

**Время выполнения:** ~5 минут ⏱️  
**Сложность:** Начинающий 🟢  
**Платформы:** macOS, Linux, Windows ✅
