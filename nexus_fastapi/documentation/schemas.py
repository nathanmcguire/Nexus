from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from assets.schemas import Asset

class Documentation(Asset):
    document_type: str = Field(..., description="Type of the document", example="Policy")