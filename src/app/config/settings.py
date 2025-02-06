import os
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials

scopes = ["https://www.googleapis.com/"]
# Load environment variables
load_dotenv()

class Settings:
    PROJECT_NAME: str = "E-Commerce API"
    VERSION: str = "1.0.0"
    
    # JWT settings
    JWT_SECRET: str = os.getenv("JWT_SECRET_KEY", "supersecretkey")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

    # MongoDB settings
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DB: str = os.getenv("MONGO_DB", "ecommerce")


    # Gmail API credentials
    
    GMAIL_API_CLIENT_SECRET: str = os.getenv("GMAIL_API_CLIENT_SECRET")
    creds = Credentials.from_authorized_user_file(GMAIL_API_CLIENT_SECRET, scopes)
    EmailCredentials = creds
    # Other settings
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "False").lower() == "true"

    Gemini_API_KEY: str = os.getenv("Gemini_API_KEY")

settings = Settings()
