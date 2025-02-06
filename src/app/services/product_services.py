import aiohttp
from repositories.product_repository import ProductRepository
from utils.file_handling import generate_product_pdf

DUMMYJSON_URL = "https://dummyjson.com/products"

class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def add_product(self, product_data: dict) -> str:
        """Add a new product."""
        return await self.product_repo.add_product(product_data)

    async def preload_dummy_products(self):
        """Fetch and store products from DummyJSON API."""
        async with aiohttp.ClientSession() as session:
            async with session.get(DUMMYJSON_URL) as response:
                data = await response.json()
                for product in data.get("products", []):
                    await self.product_repo.add_product(product)

    async def generate_product_pdf(self, product_id: str) -> bytes | None:
        """Generate and return a PDF for product details."""
        product = await self.product_repo.get_product_by_id(product_id)
        if product:
            return generate_product_pdf(product)
        return None
