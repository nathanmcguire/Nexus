from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: int = Field(..., example=1234)
    guid: str = Field(..., example="12345678-90AB-CDEF-1234-567890ABCDEF")
    username: str = Field(..., example="johndoe")
#    password: str = Field(..., example="P@ssw0rd123")
    enabled: bool = Field(default=False, example=True)
    archived: bool = Field(default=False, example=False)
    deleted: bool = Field(default=False, example=False)

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=32, example="johndoe")
    password: str = Field(..., min_length=8, max_length=128, example="P@ssw0rd123")
    enabled: Optional[bool] = Field(default=False, example=True)

    class Config:
        from_attributes = True