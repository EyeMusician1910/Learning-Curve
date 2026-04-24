from pathlib import Path
from sqlmodel import SQLModel
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


_base_config = SettingsConfigDict(
    env_file=Path(__file__).resolve().parents[2] / ".env",
    env_ignore_empty=True,
    extra="ignore",
)

class DatabaseSettings(BaseSettings):
    REDIS_HOST:str
    REDIS_PORT:str
    model_config = _base_config


database_settings = DatabaseSettings()

class SecuritySettings(BaseSettings):
    JWT_SECRET: str = Field(..., env="JWT_SECRET")
    JWT_ALGORITHM: str = Field(..., env="JWT_ALGORITHM")
    model_config = _base_config


security_settings = SecuritySettings()


class DatabaseConfig:
    BASE_DIR = Path(__file__).resolve().parents[1]
    DATABASE_PATH = BASE_DIR / "sqlite2.db"
    TEST_DATABASE_PATH = BASE_DIR / "test.db"
    DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_PATH.as_posix()}"
    TEST_DATABASE_URL = f"sqlite+aiosqlite:///{TEST_DATABASE_PATH.as_posix()}"
    SYNC_DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"
    SYNC_TEST_DATABASE_URL = f"sqlite:///{TEST_DATABASE_PATH.as_posix()}"
