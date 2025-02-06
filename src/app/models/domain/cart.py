from pydantic import BaseModel
from bson import ObjectId

class CartItem(BaseModel):
    user_id: ObjectId
    product_id: ObjectId
    quantity: int

    class Config:
        json_encoders = {ObjectId: str}
