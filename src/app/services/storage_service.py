from google.cloud import storage
from config.settings import GCP_BUCKET_NAME

class StorageService:
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket(GCP_BUCKET_NAME)

    async def upload_file(self, file_bytes: bytes, filename: str) -> str:
        """Upload file to GCP Storage and return URL."""
        blob = self.bucket.blob(filename)
        blob.upload_from_string(file_bytes, content_type="application/pdf")
        blob.make_public()
        return blob.public_url
