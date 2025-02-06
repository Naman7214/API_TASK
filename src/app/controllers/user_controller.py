from fastapi import APIRouter, HTTPException, Depends
from services.user_services import UserService
from repositories.user_repository import UserRepository
from models.schemas.user_schema import UserUpdate
from utils.security import get_current_user
from config.database import mongodb  

router = APIRouter(prefix="/users", tags=["Users"])

user_collection = mongodb.db["users"]
user_service = UserService(UserRepository(user_collection))

@router.get("/me")
async def get_my_profile(user: dict = Depends(get_current_user)):
    """Fetches the logged-in user's profile."""
    return {"user": user}

@router.put("/me")
async def update_my_profile(user_data: UserUpdate, user: dict = Depends(get_current_user)):
    """Updates the logged-in user's profile."""
    success = await user_service.update_user(user["_id"], user_data.model_dump())  # ✅ Use `model_dump()`
    
    if not success:
        raise HTTPException(status_code=400, detail="Profile update failed")
    
    return {"message": "Profile updated successfully"}
