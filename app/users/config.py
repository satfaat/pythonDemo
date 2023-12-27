from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    algorithm: str
    jwt_secret_key: str
    jwt_refresh_secret_key: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
