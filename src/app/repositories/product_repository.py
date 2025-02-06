from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId

class ProductRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def add_product(self, product_data: dict) -> str:
        """Insert a new product and return its ID."""
        result = await self.collection.insert_one(product_data)
        return str(result.inserted_id)

    async def get_all_products(self) -> list:
        """Retrieve all products."""
        return await self.collection.find().to_list(length=100)

    async def get_product_by_id(self, product_id: str) -> dict | None:
        """Find a product by ID."""
        return await self.collection.find_one({"_id": ObjectId(product_id)})

    async def update_product(self, product_id: str, seller_id: str, update_data: dict) -> bool:
        """Update product details (only if seller matches)."""
        result = await self.collection.update_one(
            {"_id": ObjectId(product_id), "seller_id": seller_id},
            {"$set": update_data}
        )
        return result.modified_count > 0

    async def delete_product(self, product_id: str, seller_id: str) -> bool:
        """Delete a product (only if seller matches)."""
        result = await self.collection.delete_one({"_id": ObjectId(product_id), "seller_id": seller_id})
        return result.deleted_count > 0
