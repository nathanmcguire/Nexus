from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    WORKFORCE = "workforce"
    SERVICE_PROVIDER = "service_provider"
    USER_ACCOUNT = "user_account"
    ADMINISTRATOR_ACCOUNT = "administrator_account"
    SERVICE_PROVIDER_ACCOUNT = "service_provider_account"

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    user_role: UserRole

class UserInDB(UserBase):
    hashed_password: str