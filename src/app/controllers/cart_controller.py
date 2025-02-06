from fastapi import APIRouter, HTTPException, Depends
from services.cart_services import CartService
from repositories.cart_repository import CartRepository
from models.schemas.cart_schema import CartItem
from utils.security import get_current_user
from config.database import get_database  

router = APIRouter(prefix="/cart", tags=["Cart"])
db = get_database()
cart_collection = db["cart"]

cart_service = CartService(CartRepository(cart_collection))

@router.post("/add")
async def add_to_cart(cart_item: CartItem, user: dict = Depends(get_current_user)):
    """Adds a product to the user's cart."""
    success = await cart_service.add_item(user["_id"], cart_item.product_id, cart_item.quantity)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to add item to cart")

    return {"message": "Item added to cart"}

@router.delete("/remove/{product_id}")
async def remove_from_cart(product_id: str, user: dict = Depends(get_current_user)):
    """Removes a product from the user's cart."""
    success = await cart_service.remove_item(user["_id"], product_id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to remove item")

    return {"message": "Item removed from cart"}

@router.get("/")
async def get_cart(user: dict = Depends(get_current_user)):
    """Fetches all cart items for the user."""
    cart = await cart_service.get_cart(user["_id"])
    return {"cart": cart}
