from fastapi import APIRouter, UploadFile, Depends
from services.storage_service import StorageService
from utils.security import get_current_user

router = APIRouter(prefix="/upload", tags=["File Uploads"])

storage_service = StorageService()

@router.post("/product-image")
async def upload_product_image(file: UploadFile, user: dict = Depends(get_current_user)):
    """Uploads product image to Google Cloud Storage."""
    file_bytes = await file.read()
    file_url = await storage_service.upload_file(file_bytes, file.filename)
    return {"file_url": file_url}
