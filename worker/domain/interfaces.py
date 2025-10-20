from abc import ABC, abstractmethod


class ModelRepository(ABC):
    """Абстрактный контракт для любых summarization моделей."""

    @abstractmethod
    async def summarize(self, text: str) -> str:
        """Возвращает summary для входного текста."""
        ...