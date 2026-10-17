from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "TaskBoard API"
    # Default to local SQLite so developers can run without PostgreSQL.
    # Override with DATABASE_URL env var or a .env file for production/Docker.
    database_url: str = "sqlite:///./taskboard.db"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
