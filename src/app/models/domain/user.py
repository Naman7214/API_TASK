from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId

class User(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    email: str
    password: str

    # Fix: Allow arbitrary types for bson.ObjectId
    model_config = ConfigDict(arbitrary_types_allowed=True)
