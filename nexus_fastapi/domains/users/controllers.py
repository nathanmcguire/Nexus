from typing import List
from fastapi import APIRouter, HTTPException
from . import services, schemas

# Initialize router for user-related endpoints
router = APIRouter(tags=["Users"])

# Tagging the router for user-related operations
# @router.get("/me", response_model=UserResponse, tags=["Users"])
# def get_current_user_route(current_user: Annotated[UserResponse, Depends(get_current_user)]):
#     return current_user

# @router.get("/users/me/", response_model=UserBase, tags=["Users"])
# async def read_users_me(
#     current_user: Annotated[UserBase, Depends(get_current_user)],
# ):
#     return current_user

# @router.get("/users/me/items/", tags=["Users"])
# async def read_own_items(
#     current_user: Annotated[UserBase, Depends(get_current_user)],
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]

@router.get("/users", response_model=List[schemas.UserResponse])
def read_users():
    return services.read_users()

@router.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate):
    return services.create_user(user)

@router.get("/users/{id}", response_model=schemas.UserResponse)
def read_user(id: int):
    user = services.read_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{id}", response_model=schemas.UserResponse)
def replace_user(id: int, user: schemas.UserUpdate):
    updated_user = services.replace(id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.patch("/users/{id}", response_model=schemas.UserResponse)
def update_user(id: int, user: schemas.UserUpdate):
    updated_user = services.update(id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{id}", tags=["Users"])
def delete_user(id: int):
    if not services.delete(id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}