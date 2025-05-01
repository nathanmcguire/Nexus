from pydantic import BaseModel, Field, create_model
from typing import Optional


class User(BaseModel):
    id: int
    guid: str
    username: str
    password: str
    enabled: bool = Field(default=False)
    archived: bool = Field(default=False)
    deleted: bool = Field(default=False)

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=32)
    password: str = Field(..., min_length=8, max_length=128)
    enabled: Optional[bool] = Field(default=False)

    class Config:
        from_attributes = True