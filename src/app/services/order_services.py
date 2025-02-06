from repositories.order_repository import OrderRepository

class OrderService:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def place_order(self, order_data: dict) -> str:
        """Place a new order."""
        return await self.order_repo.create_order(order_data)

    async def get_orders(self, user_id: str) -> list:
        """Fetch all orders for a user."""
        return await self.order_repo.get_orders_by_user(user_id)
