from fastapi import APIRouter, HTTPException, Depends
from services.auth_services import AuthService
from repositories.user_repository import UserRepository
from models.schemas.user_schema import UserRegister, UserLogin
from utils.security import create_access_token, get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

auth_service = AuthService(UserRepository())

@router.post("/register")
async def register(user_data: UserRegister):
    """Registers a new user."""
    existing_user = await auth_service.user_repo.find_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_data.password = auth_service.hash_password(user_data.password)
    user_id = await auth_service.user_repo.create_user(user_data.dict())
    
    return {"message": "User registered successfully", "user_id": str(user_id)}

@router.post("/login")
async def login(user_data: UserLogin):
    """Logs in a user and returns JWT token."""
    user = await auth_service.authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user["_id"], user["role"])
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
async def get_current_user_details(user: dict = Depends(get_current_user)):
    """Fetches details of the currently logged-in user."""
    return {"user": user}
