from domain.interfaces import ModelRepository


class LocalT5Repository(ModelRepository):
    """Local T5 model implementation."""
    
    async def summarize(self, text: str) -> str:
        # TODO: Connect transformers pipeline for actual T5 summarization
        return f"[LOCAL SUMMARY]: {text[:80]}..."