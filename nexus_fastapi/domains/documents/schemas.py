from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from ..assets.schemas import Asset

class Document(Asset):
    document_type: str = Field(..., description="Type of the document", example="Policy")
    category: str = Field(..., description="Category of the document", example="Procedure")
    description: Optional[str] = Field(None, description="Description of the document", example="Detailed process for onboarding employees")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")