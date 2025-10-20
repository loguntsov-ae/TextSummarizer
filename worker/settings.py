from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    redis_url: str = "redis://redis:6379"
    huggingface_api_key: str | None = None
    openai_api_key: str | None = None
    openai_model_name: str = "gpt-4o-mini"
    model_backend: str = "openai"  # 👈 можно переключать: openai / huggingface / local_t5

    class Config:
        env_file = ".env"

settings = Settings()
