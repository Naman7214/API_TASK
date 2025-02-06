from pydantic import BaseModel

class CartAddItem(BaseModel):
    product_id: str
    quantity: int

class CartItem(BaseModel):
    product_id: str
    quantity: int