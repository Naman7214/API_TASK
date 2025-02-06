from repositories.user_repository import UserRepository
from fastapi import HTTPException
from models.schemas.user_schema import UserRoleUpdate

class AdminService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_all_users(self):
        """Fetch all registered users (Admins Only)."""
        users = await self.user_repo.get_all_users()
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        
        return users

    async def update_user_role(self, user_id: str, role_update: UserRoleUpdate):
        """Update a user's role (Admins Only)."""
        if role_update.role not in ["admin", "buyer", "seller"]:
            raise HTTPException(status_code=400, detail="Invalid role provided")
        
        updated = await self.user_repo.update_user_role(user_id, role_update.role)
        if not updated:
            raise HTTPException(status_code=404, detail="User not found or update failed")
        
        return {"message": f"User role updated to {role_update.role}"}
