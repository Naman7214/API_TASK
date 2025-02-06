from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId
from models.domain.user import User

class UserRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create_user(self, user_data: dict) -> str:
        """Insert a new user and return the ID."""
        result = await self.collection.insert_one(user_data)
        return str(result.inserted_id)

    async def find_by_email(self, email: str) -> dict | None:
        """Find a user by email."""
        return await self.collection.find_one({"email": email})

    async def find_by_id(self, user_id: str) -> dict | None:
        """Find a user by ID."""
        return await self.collection.find_one({"_id": ObjectId(user_id)})

    async def update_role(self, user_id: str, new_role: str) -> bool:
        """Update user role."""
        result = await self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"role": new_role}}
        )
        return result.modified_count > 0
