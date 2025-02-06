from pydantic import BaseModel
from typing import Literal
from bson import ObjectId

class FileUpload(BaseModel):
    id: ObjectId
    user_id: ObjectId
    file_url: str
    file_type: Literal["product", "complaint"]

    class Config:
        json_encoders = {ObjectId: str}
