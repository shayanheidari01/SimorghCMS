from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Advanced CMS"
    PROJECT_DESCRIPTION: str = "A WordPress-like CMS built with FastAPI"
    VERSION: str = "1.0.0"
    
    # Database - تغییر به SQLite برای سادگی
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./cms.db")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Upload settings
    UPLOAD_DIR: str = "static/uploads"
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()