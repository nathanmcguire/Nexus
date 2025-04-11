from fastapi import APIRouter, Depends
from typing import Annotated
from nexus_fastapi.auth import get_current_active_user
from nexus_fastapi.models import User

# Initialize router for user-related endpoints
router = APIRouter()

@router.get("/me", response_model=UserResponse)
def get_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user

@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]