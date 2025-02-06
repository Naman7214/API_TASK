from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from config.settings import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRATION
from repositories.user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def hash_password(self, password: str) -> str:
        """Hash password using bcrypt."""
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify hashed password."""
        return pwd_context.verify(plain_password, hashed_password)

    def generate_jwt(self, user_id: str, role: str) -> str:
        """Generate JWT token."""
        payload = {
            "sub": user_id,
            "role": role,
            "exp": datetime.utcnow() + timedelta(days=JWT_EXPIRATION)
        }
        return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    async def authenticate_user(self, email: str, password: str) -> dict | None:
        """Authenticate user by email and password."""
        user = await self.user_repo.find_by_email(email)
        if user and self.verify_password(password, user["password"]):
            return user
        return None
