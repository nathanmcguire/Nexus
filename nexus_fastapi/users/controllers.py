from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from . import schemas
from ..database import get_db
from .services import create_user_service, get_users_service, get_user_service


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user_service(user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error creating user: {str(e)}")


@router.get("/", response_model=list[schemas.User], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    try:
        return get_users_service(db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error fetching users: {str(e)}")


@router.get("/{id}", response_model=schemas.User, status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    try:
        return get_user_service(id, db)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error fetching user: {str(e)}")