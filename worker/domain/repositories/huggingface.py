import httpx
from domain.interfaces import ModelRepository
from settings import settings


class HuggingFaceRepository(ModelRepository):
    """Реализация репозитория для Hugging Face API."""

    def __init__(self, model_name: str | None = None):
        self.model_name = model_name or settings.model_name
        self.api_key = settings.huggingface_api_key
        self.url = f"https://api-inference.huggingface.co/models/{self.model_name}"

    async def summarize(self, text: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(self.url, headers=headers, json={"inputs": text})
            response.raise_for_status()
            data = response.json()
        if isinstance(data, list) and "summary_text" in data[0]:
            return data[0]["summary_text"]
        return str(data)