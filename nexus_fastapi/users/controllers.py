from typing import List
from fastapi import APIRouter, HTTPException
from . import schemas
from . import services

# Initialize router for user-related endpoints
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", response_model=List[schemas.UserRead])
def get_users():
    return services.get_users()

@router.post("", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate):
    return services.create_user (user)

@router.get("/{id}", response_model=schemas.UserRead)
def get_users_by_id(id: int):
    user = services.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}", response_model=schemas.UserRead)
def replace_user_by_id(id: int, user: schemas.UserCreate):
    updated_user = services.replace_user_by_id(id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.patch("/{id}", response_model=schemas.UserRead)
def update_user_by_id(id: int, user: schemas.UserCreate):
    updated_user = services.update_user_by_id(id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{id}", tags=["Users"])
def delete_user_by_id(id: int):
    if not services.delete_user_by_id(id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}