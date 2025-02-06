import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    PROJECT_NAME: str = "E-Commerce API"
    VERSION: str = "1.0.0"
    
    # JWT settings
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "supersecretkey")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

    # Google Cloud Storage
    GCP_BUCKET_NAME: str = os.getenv("GCP_BUCKET_NAME")
    GCP_CREDENTIALS_PATH: str = os.getenv("GCP_CREDENTIALS_PATH")

    # Gmail API credentials
    GMAIL_API_CLIENT_SECRET: str = os.getenv("GMAIL_API_CLIENT_SECRET")

    # Other settings
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "False").lower() == "true"

    Gemini_API_KEY: str = os.getenv("Gemini_API_KEY")

settings = Settings()
