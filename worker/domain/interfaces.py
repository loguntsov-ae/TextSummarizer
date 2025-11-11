from abc import ABC, abstractmethod


class ModelRepository(ABC):
    """Abstract interface for text summarization models."""

    @abstractmethod
    async def summarize(self, text: str) -> str:
        """Generate a summary for the input text.
        
        Args:
            text: The input text to summarize
            
        Returns:
            A summarized version of the input text
        """
        ...