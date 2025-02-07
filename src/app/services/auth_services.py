from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from config.settings import settings
from repositories.user_repository import UserRepository
from nashx import nashCore

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

JWT_SECRET = settings.JWT_SECRET
JWT_ALGORITHM = settings.JWT_ALGORITHM
JWT_EXPIRATION = settings.JWT_EXPIRATION

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def hash_password(self, password: str) -> str:
        """Hash password using bcrypt."""
        # return pwd_context.hash(password)
        print("Into hasher func",password)
        return nashCore(password,16)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify hashed password."""
        if nashCore(plain_password,16) == hashed_password:  
            return True
        else:
            return False
        
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
        print(password)
    
        print(user['password'])
        print("after hashing:", nashCore(password,16))
        if user and self.verify_password(password, user["password"]):
            print("True")
            return user
        return None
    
    async def create_user(self, user_data: dict) -> dict:
        """Create a new user with hashed password."""
        print(user_data['password'])
        hashed_password = self.hash_password(user_data["password"])
        print(hashed_password)
        new_user = {
            "name": user_data["name"],
            "email": user_data["email"],
            "password": hashed_password,
            "role": user_data.get("role", "buyer"),
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        user_id = await self.user_repo.create_user(new_user)
        return {**new_user, "id": user_id}