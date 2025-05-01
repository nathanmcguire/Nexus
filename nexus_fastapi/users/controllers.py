from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import datetime
from . import schemas, models
from ..database import get_db

# Initialize router for user-related endpoints
router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        # Check if the username is already taken
        existing_user = db.query(models.User).filter(models.User.username == user.username).first()
        if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")

        # Filter out invalid fields before creating the User instance
        new_user = models.User(
            username=user.username,
            password=user.password,
            enabled=user.enabled,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": f"User {new_user.username} created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error creating user: {str(e)}")