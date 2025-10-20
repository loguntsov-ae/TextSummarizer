from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    redis_url: str = "redis://localhost:6379"
    database_url: str = "sqlite:///./tasks.db"

    class Config:
        env_file = ".env"


settings = Settings()
