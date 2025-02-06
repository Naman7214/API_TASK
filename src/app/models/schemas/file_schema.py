from pydantic import BaseModel
from typing import Literal

class FileUploadSchema(BaseModel):
    file_url: str
    file_type: Literal["product", "complaint"]
