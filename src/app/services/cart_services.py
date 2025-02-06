from repositories.cart_repository import CartRepository

class CartService:
    def __init__(self, cart_repo: CartRepository):
        self.cart_repo = cart_repo

    async def add_item(self, user_id: str, product_id: str, quantity: int) -> bool:
        """Add item to cart."""
        return await self.cart_repo.add_to_cart(user_id, product_id, quantity)

    async def remove_item(self, user_id: str, product_id: str) -> bool:
        """Remove item from cart."""
        return await self.cart_repo.remove_from_cart(user_id, product_id)

    async def get_cart(self, user_id: str) -> list:
        """Get all items in cart."""
        return await self.cart_repo.get_cart(user_id)
