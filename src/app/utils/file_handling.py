from fastapi import UploadFile, HTTPException
from typing import List

# Allowed file types
ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png"]
ALLOWED_PDF_TYPES = ["application/pdf"]

# Validate File Type
async def validate_and_read_file(file: UploadFile, allowed_types: List[str]) -> bytes:
    """Validate file type and return file bytes for direct cloud upload."""
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail=f"Invalid file type: {file.content_type}")
    
    return await file.read()  
