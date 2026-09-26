"""
Configuration Settings.
This module uses Pydantic Settings to load and validate environment variables from the .env file.
It centralizes all configuration management, ensuring type safety for API keys,
database paths, and other system-wide constants.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
        )
    DATA_DIRECTORY: str = ""
    EMBEDDING_MODEL_SOURCE: str = ""
    LLM_SOURCE: str = "openai"

    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: str = ""
    OPENAI_EMBEDDING_MODEL: str = ""
    OPENAI_LLM_MODEL: str = ""
    OPENAI_TEMPERATURE: float = 0.0

    OLLAMA_BASE_URL: str = ""
    OLLAMA_EMBEDDING_MODEL: str = ""
    OLLAMA_LLM_MODEL: str = "LLAMA3"
    OLLAMA_TEMPERATURE: float = 0.0

    DOCKER_BASE_URL: str = ""
    DOCKER_EMBEDDING_MODEL: str = ""

settings = Settings()
