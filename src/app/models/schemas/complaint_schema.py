from pydantic import BaseModel

class ComplaintCreate(BaseModel):
    order_id: str
    product_id: str
    issue: str
    image_url: str | None = None
