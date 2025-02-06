from pydantic import BaseModel
from typing import Literal
from bson import ObjectId

class Complaint(BaseModel):
    id: ObjectId
    user_id: ObjectId
    order_id: ObjectId
    product_id: ObjectId
    issue: str
    image_url: str
    status: Literal["open", "rejected"]

    class Config:
        json_encoders = {ObjectId: str}
