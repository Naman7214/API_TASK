from fastapi import APIRouter, HTTPException, Depends
from services.auth_services import AuthService
from repositories.user_repository import UserRepository
from models.schemas.user_schema import UserRegister, UserLogin
from utils.security import create_access_token, get_current_user
from config.database import mongodb  

router = APIRouter(prefix="/auth", tags=["Authentication"])

user_collection = mongodb.db["users"]
user_repo = UserRepository(user_collection)
auth_service = AuthService(user_repo)

@router.post("/register")
async def register(user_data: UserRegister):
    """Registers a new user."""


    hashed_password = auth_service.hash_password(user_data.password)
    
    user_dict = user_data.model_dump()
    user_dict["password"] = hashed_password  # Replace plain password with hashed one

    user_id = await auth_service.create_user(user_dict)
    
    return {"message": "User registered successfully", "user_id": str(user_id)}

@router.post("/login")
async def login(user_data: UserLogin):
    """Logs in a user and returns JWT token."""
    user = await auth_service.authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(str(user["_id"]), user["role"])
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
async def get_current_user_details(user: dict = Depends(get_current_user)):
    """Fetches details of the currently logged-in user."""
    return {"user": user}
