from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "MARLIN-X"
    VERSION: str = "1.0.0-SIH2026"
    API_V1_STR: str = "/api/v1"
    
    # Environment
    ENV: str = "development"
    DEBUG: bool = True
    DEMO_MODE: bool = True
    
    # Storage & DB
    DATABASE_URL: str = "sqlite:///./marlin_x.db"
    
    # CORS
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "*"
    ]

    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()
