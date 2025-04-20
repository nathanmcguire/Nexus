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