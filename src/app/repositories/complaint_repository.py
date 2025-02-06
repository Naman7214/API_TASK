from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId

class ComplaintRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def file_complaint(self, complaint_data: dict) -> str:
        """File a complaint and return complaint ID."""
        result = await self.collection.insert_one(complaint_data)
        return str(result.inserted_id)

    async def get_all_complaints(self) -> list:
        """Retrieve all complaints."""
        return await self.collection.find().to_list(length=50)

    async def get_complaint_by_id(self, complaint_id: str) -> dict | None:
        """Retrieve a complaint by ID."""
        return await self.collection.find_one({"_id": ObjectId(complaint_id)})
