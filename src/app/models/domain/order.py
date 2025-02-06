from pydantic import BaseModel
from typing import List, Literal
from bson import ObjectId

class OrderItem(BaseModel):
    product_id: ObjectId
    quantity: int
    price: float

class Order(BaseModel):
    id: ObjectId
    user_id: ObjectId
    items: List[OrderItem]
    total_amount: float
    status: Literal["pending", "shipped", "delivered", "cancelled"]

    class Config:
        json_encoders = {ObjectId: str}
