from fastapi import APIRouter, Depends
from services.order_services import OrderService
from repositories.order_repository import OrderRepository
from models.schemas.order_schema import OrderCreate
from utils.security import get_current_user

router = APIRouter(prefix="/orders", tags=["Orders"])

order_service = OrderService(OrderRepository())

@router.post("/")
async def place_order(order_data: OrderCreate, user: dict = Depends(get_current_user)):
    """Places a new order."""
    order_id = await order_service.place_order(order_data.dict())
    return {"message": "Order placed successfully", "order_id": order_id}

@router.get("/")
async def get_orders(user: dict = Depends(get_current_user)):
    """Fetches user's orders."""
    orders = await order_service.get_orders(user["_id"])
    return {"orders": orders}
