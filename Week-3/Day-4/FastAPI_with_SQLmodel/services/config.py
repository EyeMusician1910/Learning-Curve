from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


_base_config = SettingsConfigDict(
    env_file=Path(__file__).resolve().parents[2] / ".env",
    env_ignore_empty=True,
    extra="ignore",
)


class SecuritySettings(BaseSettings):
    JWT_SECRET: str = Field(..., env="JWT_SECRET")
    JWT_ALGORITHM: str = Field(..., env="JWT_ALGORITHM")
    model_config = _base_config


security_settings = SecuritySettings()
