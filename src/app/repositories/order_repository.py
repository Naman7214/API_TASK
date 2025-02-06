from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId

class OrderRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create_order(self, order_data: dict) -> str:
        """Create a new order."""
        result = await self.collection.insert_one(order_data)
        return str(result.inserted_id)

    async def get_orders_by_user(self, user_id: str) -> list:
        """Get all orders for a specific user."""
        return await self.collection.find({"user_id": user_id}).to_list(length=50)

    async def get_order_by_id(self, order_id: str) -> dict | None:
        """Retrieve a specific order by ID."""
        return await self.collection.find_one({"_id": ObjectId(order_id)})
