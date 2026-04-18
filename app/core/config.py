from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "fullypack_fastapi"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/fullypack_fastapi"

    class Config:
        env_file = ".env"

settings = Settings()
