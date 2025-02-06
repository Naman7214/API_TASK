from fastapi import APIRouter, HTTPException, Depends
from services.product_services import ProductService
from repositories.product_repository import ProductRepository
from models.schemas.product_schema import ProductCreate
from utils.security import get_current_user
from config.database import get_database  # Import your MongoDB connection

router = APIRouter(prefix="/products", tags=["Products"])

# Initialize database connection
db = get_database()
product_collection = db["products"]  # Get the 'products' collection

# Pass the collection to ProductRepository
product_service = ProductService(ProductRepository(product_collection))

@router.post("/")
async def create_product(product_data: ProductCreate, user: dict = Depends(get_current_user)):
    """Creates a new product (Only sellers allowed)."""
    if user["role"] != "seller":
        raise HTTPException(status_code=403, detail="Only sellers can add products")

    product_id = await product_service.add_product(product_data.dict())
    return {"message": "Product created successfully", "product_id": product_id}

# @router.get("/{product_id}/pdf")
# async def get_product_pdf(product_id: str):
#     """Generates and downloads a product PDF."""
#     pdf_content = await product_service.generate_product_pdf(product_id)
#     if not pdf_content:
#         raise HTTPException(status_code=404, detail="Product not found")

    return pdf_content  # FastAPI will return the file as a response

@router.post("/preload")
async def preload_products():
    """Fetches and stores products from DummyJSON API."""
    await product_service.preload_dummy_products()
    return {"message": "Dummy products imported successfully"}
