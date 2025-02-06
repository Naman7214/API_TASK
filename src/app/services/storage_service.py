from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaInMemoryUpload

class StorageService:
    def __init__(self, credentials_json: str):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_json)
        self.service = build('drive', 'v3', credentials=self.credentials)

    async def upload_file(self, file_bytes: bytes, filename: str) -> str:
        """Upload file to Google Drive and return URL."""
        media = MediaInMemoryUpload(file_bytes, mimetype='application/pdf')
        file_metadata = {'name': filename}
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        file_id = file.get('id')
        
        # Make the file public
        self.service.permissions().create(
            fileId=file_id,
            body={'type': 'anyone', 'role': 'reader'}
        ).execute()
        
        return f"https://drive.google.com/uc?id={file_id}&export=download"
