from domain.interfaces import ModelRepository

class LocalT5Repository(ModelRepository):
    """Локальная модель (пример)."""
    async def summarize(self, text: str) -> str:
        # Здесь можно подключить transformers pipeline(...)
        return f"[LOCAL SUMMARY]: {text[:80]}..."