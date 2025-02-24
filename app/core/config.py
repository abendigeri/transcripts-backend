from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = 'YouTube Transcripts Backend'
    PROJECT_DESCRIPTION: str = 'A FastAPI service for downloading YouTube video transcripts'
    VERSION: str = '1.0.0'
    TRANSCRIPTS_DIR: str = 'transcripts'
    DATABASE_URL: Optional[str] = None

    class Config:
        env_file = '.env'

settings = Settings()