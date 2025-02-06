from repositories.complaint_repository import ComplaintRepository
from services.email_service import EmailService

class ComplaintService:
    def __init__(self, complaint_repo: ComplaintRepository, email_service: EmailService):
        self.complaint_repo = complaint_repo
        self.email_service = email_service

    async def file_complaint(self, complaint_data: dict) -> str:
        """File a complaint and send email notification."""
        complaint_id = await self.complaint_repo.file_complaint(complaint_data)
        await self.email_service.send_complaint_notification(complaint_data)
        return complaint_id
