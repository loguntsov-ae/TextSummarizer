from domain.repositories import HuggingFaceRepository, LocalT5Repository, OpenAIRepository
from settings import settings
from domain.interfaces import ModelRepository


def get_repository() -> ModelRepository:
    repo_type = getattr(settings, "model_backend", "huggingface")

    if repo_type == "huggingface":
        return HuggingFaceRepository()
    elif repo_type == "local_t5":
        return LocalT5Repository()
    elif repo_type == "openai":
        return OpenAIRepository()
    else:
        raise ValueError(f"Unknown model backend: {repo_type}")