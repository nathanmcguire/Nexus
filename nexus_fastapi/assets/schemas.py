from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AssetBase(BaseModel):
    name: str
    description: Optional[str] = None

class AssetCreate(AssetBase):
    pass

class AssetUpdate(AssetBase):
    pass

class AssetInDBBase(AssetBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class Asset(AssetInDBBase):
    pass