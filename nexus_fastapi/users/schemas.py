from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from ..common.schemas import Audit

class UserCreate(BaseModel):
    username: str
    password: str
    is_active: Optional[bool] = Field(default=True)

    class Config:
        from_attributes = True

class User(BaseModel):
    id: int
    guid: str
    username: str
    is_active: bool
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    archived_at: Optional[datetime] = None
    archived_by: Optional[str] = None
    unarchived_at: Optional[datetime] = None
    unarchived_by: Optional[str] = None
    is_archived: bool = Field(default=False)
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[str] = None
    undeleted_at: Optional[datetime] = None
    undeleted_by: Optional[str] = None
    is_deleted: bool = Field(default=False)

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

    class Config:
        from_attributes = True

class UserDelete(BaseModel):
    is_deleted: Optional[bool] = None
    is_archived: Optional[bool] = None

    class Config:
        from_attributes = True