from repositories.user_repository import UserRepository
from fastapi import HTTPException
from models.schemas.user_schema import UserUpdate

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_user_by_id(self, user_id: str):
        """Fetch user details by user ID."""
        user = await self.user_repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def update_user(self, user_id: str, user_data: dict):
        """Update user details."""
        success = await self.user_repo.update_user(user_id, user_data)
        if not success:
            raise HTTPException(status_code=400, detail="Failed to update user")
        return True
