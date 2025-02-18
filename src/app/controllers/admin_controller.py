from fastapi import APIRouter, HTTPException, Depends
from services.admin_services import AdminService
from repositories.user_repository import UserRepository
from utils.security import get_current_user
from config.database import mongodb  # ✅ Import MongoDB connection

router = APIRouter(prefix="/admin", tags=["Admin"])

# ✅ Initialize UserRepository with the users collection
user_collection = mongodb.db["users"]
admin_service = AdminService(UserRepository(user_collection))

@router.put("/update-role/{user_id}")
async def update_user_role(user_id: str, role: str, user: dict = Depends(get_current_user)):
    """Updates user role (Admin only)."""
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only")

    success = await admin_service.update_role(user_id, role)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to update role")

    return {"message": "User role updated successfully"}
