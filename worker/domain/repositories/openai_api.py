from openai import AsyncOpenAI
from domain.interfaces import ModelRepository
from settings import settings


class OpenAIRepository(ModelRepository):
    """OpenAI API implementation for text summarization."""

    def __init__(self, model_name: str | None = None):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = model_name or settings.openai_model_name

    async def summarize(self, text: str) -> str:
        system_prompt = (
            "You are a text summarization assistant. "
            "Summarize the input text clearly and concisely in the same language."
        )
        completion = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
            max_tokens=300,
            temperature=0.3,
        )

        return completion.choices[0].message.content.strip()
