import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Bookverse"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
