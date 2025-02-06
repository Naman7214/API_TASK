from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId

class FileRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def save_file_metadata(self, file_data: dict) -> str:
        """Save file metadata and return file ID."""
        result = await self.collection.insert_one(file_data)
        return str(result.inserted_id)

    async def get_file_by_id(self, file_id: str) -> dict | None:
        """Retrieve file metadata by ID."""
        return await self.collection.find_one({"_id": ObjectId(file_id)})
