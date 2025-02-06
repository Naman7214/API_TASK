from pydantic import BaseModel
from typing import List

class ProductCreate(BaseModel):
    title: str
    description: str
    category: str
    price: float
    rating: float
    brand: str
    images: List[str]
    thumbnail: str

class ProductUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category: str | None = None
    price: float | None = None
    rating: float | None = None
    brand: str | None = None
    images: List[str] | None = None
    thumbnail: str | None = None
