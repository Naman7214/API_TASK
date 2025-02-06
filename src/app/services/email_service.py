from googleapiclient.discovery import build
from utils.email_template import generate_complaint_email
# from config.settings import GMAIL_USER

class EmailService:
    def __init__(self, credentials):
        self.service = build("gmail", "v1", credentials=credentials)

    async def send_complaint_notification(self, complaint_data: dict):
        """Generate email with Gemini and send via Gmail API."""
        email_content = generate_complaint_email(complaint_data)
        message = {
            "raw": email_content.encode("utf-8"),
            "to": complaint_data["user_email"],
            "subject": "Complaint Received"
        }
        self.service.users().messages().send(userId="me", body=message).execute()
