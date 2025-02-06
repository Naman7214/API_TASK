from fastapi import APIRouter, Depends
from services.complaint_services import ComplaintService
from repositories.complaint_repository import ComplaintRepository
from services.email_service import EmailService
from models.schemas.complaint_schema import ComplaintCreate
from utils.security import get_current_user
from config.database import get_database  
from config.settings import settings

credentials = settings.EmailCredentials

router = APIRouter(prefix="/complaints", tags=["Complaints"])
db = get_database()
complaint_collection = db["complaints"]

complaint_service = ComplaintService(ComplaintRepository(complaint_collection), EmailService(credentials=credentials))

@router.post("/")
async def file_complaint(complaint_data: ComplaintCreate, user: dict = Depends(get_current_user)):
    """Files a complaint and sends an email notification."""
    complaint_id = await complaint_service.file_complaint(complaint_data.dict())
    return {"message": "Complaint filed successfully", "complaint_id": complaint_id}
