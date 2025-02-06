from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId

class CartRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def add_to_cart(self, user_id: str, product_id: str, quantity: int) -> bool:
        """Add a product to the user's cart or update quantity if already exists."""
        result = await self.collection.update_one(
            {"user_id": ObjectId(user_id), "product_id": ObjectId(product_id)},
            {"$inc": {"quantity": quantity}},
            upsert=True
        )
        return result.modified_count > 0

    async def remove_from_cart(self, user_id: str, product_id: str) -> bool:
        """Remove a product from the cart."""
        result = await self.collection.delete_one({"user_id": ObjectId(user_id), "product_id": ObjectId(product_id)})
        return result.deleted_count > 0

    async def get_cart(self, user_id: str) -> list:
        """Fetch all items in the user's cart."""
        return await self.collection.find({"user_id": ObjectId(user_id)}).to_list(length=50)
