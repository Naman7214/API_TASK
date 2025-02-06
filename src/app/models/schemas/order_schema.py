from pydantic import BaseModel
from typing import List, Literal

class OrderItemCreate(BaseModel):
    product_id: str
    quantity: int
    price: float

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    total_amount: float

class OrderStatusUpdate(BaseModel):
    status: Literal["pending", "shipped", "delivered", "cancelled"]
