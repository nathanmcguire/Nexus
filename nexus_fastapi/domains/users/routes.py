from fastapi import APIRouter, Depends
from typing import Annotated
from nexus_fastapi.domains.common.auth.service import get_current_user
from nexus_fastapi.domains.users.schemas import UserBase, UserResponse

# Initialize router for user-related endpoints
router = APIRouter()

# Tagging the router for user-related operations
@router.get("/me", response_model=UserResponse, tags=["Users"])
def get_current_user_route(current_user: Annotated[UserResponse, Depends(get_current_user)]):
    return current_user

@router.get("/users/me/", response_model=UserBase, tags=["Users"])
async def read_users_me(
    current_user: Annotated[UserBase, Depends(get_current_user)],
):
    return current_user

@router.get("/users/me/items/", tags=["Users"])
async def read_own_items(
    current_user: Annotated[UserBase, Depends(get_current_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]