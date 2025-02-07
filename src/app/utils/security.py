import jwt
import os
import bcrypt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from typing import List
from models.domain.user import User  # Ensure this imports correctly
from repositories.user_repository import UserRepository  # User DB interactions

# Load environment variables
load_dotenv()

# JWT Configurations
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Password Hashing
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

# JWT Token Creation
def create_access_token(user_id: str, role: str, expires_delta: timedelta = None):
    to_encode = {"sub": user_id, "role": role}
    from datetime import timezone
    expire = datetime.now(timezone.utc) + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# JWT Token Verification
def verify_token(token: str = Security(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Role-Based Access Control (RBAC)
async def get_current_user(token: str = Depends(verify_token)):
    email = token.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = await UserRepository.find_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

def require_roles(allowed_roles: List[str]):
    async def role_dependency(user: User = Depends(get_current_user)):
        if user.role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Not authorized")
        return user
    return role_dependency
