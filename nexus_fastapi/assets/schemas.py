from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Asset(BaseModel):
    id: int = Field(..., description="Unique identifier for the asset", example=1)
    name: str = Field(..., description="Name of the asset", example="Asset Name")
    description: Optional[str] = Field(None, description="Optional description of the asset", example="This is an asset.")
    created_at: datetime = Field(..., description="Timestamp when the asset was created", example="2025-04-11T10:00:00Z")
    updated_at: datetime = Field(..., description="Timestamp when the asset was last updated", example="2025-04-11T12:00:00Z")

    class Config:
        from_attributes = True

