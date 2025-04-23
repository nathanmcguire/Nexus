from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    username: str
    password: str

class AccessTokenBase(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class AccessToken(AccessTokenBase):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

class PersonalTokenBase(BaseModel):
    note: str

class PersonalToken(PersonalTokenBase):
    token: str
    note: str

