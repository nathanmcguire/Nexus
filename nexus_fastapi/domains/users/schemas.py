from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class UserRole(str, Enum):
    WORKFORCE = "workforce"
    SERVICE_PROVIDER = "service_provider"
    USER_ACCOUNT = "user_account"
    ADMINISTRATOR_ACCOUNT = "administrator_account"
    SERVICE_PROVIDER_ACCOUNT = "service_provider_account"

class UserBase(BaseModel):
    user_role: UserRole = Field(..., description="Role of the user", example="Administrator")
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True