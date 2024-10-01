from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    log_level: str
    telegram_api_token: str  # Add this to support the Telegram API token

    class Config:
        env_file = ".env"  # Load environment variables from .env

settings = Settings()
