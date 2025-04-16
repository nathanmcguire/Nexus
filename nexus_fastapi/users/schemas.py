from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    is_active: Optional[bool] = Field(default=True)

    class Config:
        from_attributes = True

class UserRead(BaseModel):
    id: int
    guid: str
    username: str
    is_active: bool
    created_at: datetime
    created_by: int
    updated_at: datetime
    updated_by: int
    deleted_at: Optional[datetime] = Field(default=None, nullable=True)
    deleted_by: Optional[int] = Field(default=None, nullable=True)
    is_deleted: bool
    recovered_at: Optional[datetime] = Field(default=None, nullable=True)
    recovered_by: Optional[int] = Field(default=None, nullable=True)

    class Config:
        from_attributes = True