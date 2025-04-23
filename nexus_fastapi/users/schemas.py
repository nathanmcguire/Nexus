from pydantic import BaseModel, Field, create_model
from typing import Optional
from ..common.schemas import AuditMixIn


class Config:
    from_attributes = True

class Username(BaseModel):
    username: str

class UserRegister(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    password: str
    is_active: Optional[bool] = Field(default=True)


User = create_model(
    'User',
    id=(int, ...),
    guid=(str, ...),
    username=(str, ...),
    is_active=(bool, ...),
    **AuditMixIn.__annotations__
)


class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


class UserDelete(BaseModel):
    is_deleted: Optional[bool] = None
    is_archived: Optional[bool] = None


User.__config__ = Config
UserRegister.__config__ = Config
UserCreate.__config__ = Config
UserUpdate.__config__ = Config
UserDelete.__config__ = Config
