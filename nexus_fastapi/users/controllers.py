from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import datetime
from . import schemas, models
from ..database import get_db

# Initialize router for user-related endpoints
router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=List[schemas.User], operation_id="getUsers", responses={
    418: {"description": "Error fetching users"}
})
async def get_users(db: Session = Depends(get_db)):
    try:
        users = db.query(models.User).all()
        return [schemas.User.from_orm(user) for user in users]
    except SQLAlchemyError as e:
        print(f"Error fetching users: {e}")
        raise HTTPException(status_code=418, detail="Error fetching users")


@router.post("", response_model=schemas.User, operation_id="createUser", responses={
    409: {"description": "Conflict: Username already exists."},
    418: {"description": "Error creating user"}
})
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = models.User(
            username=user.username,
            password=user.password,  # In a real application, hash the password before storing it
            is_active=user.is_active if user.is_active is not None else True,
            created_by=-1
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return schemas.User.from_orm(new_user)
    except IntegrityError as e:
        db.rollback()
        if "UNIQUE constraint failed: Users.username" in str(e):
            raise HTTPException(status_code=409, detail="Username already exists.")
        raise HTTPException(status_code=418, detail="Error creating user")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating user: {e}")
        raise HTTPException(status_code=418, detail="Error creating user")


@router.get("/{id}", response_model=schemas.User, operation_id="getUserById", responses={
    418: {"description": "Error fetching user by ID"}
})
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == id).first()
        if user:
            return schemas.User.from_orm(user).dict()
        raise HTTPException(status_code=404, detail="User not found")
    except SQLAlchemyError as e:
        print(f"Error fetching user by ID: {e}")
        raise HTTPException(status_code=418, detail="Error fetching user by ID")


@router.patch("/{id}", response_model=schemas.User, operation_id="updateUserById", responses={
    418: {"description": "Error patching user"}
})
def update_user_by_id(id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(models.User).filter(models.User.id == id).first()
        if existing_user:
            if user.username is not None:
                existing_user.username = user.username
            if user.password is not None:
                existing_user.password = user.password  # Hash the password in a real application
            if user.is_active is not None:
                existing_user.is_active = user.is_active
            existing_user.updated_by = -1
            db.commit()
            db.refresh(existing_user)
            return schemas.User.from_orm(existing_user)
        raise HTTPException(status_code=404, detail="User not found")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error updating user: {e}")
        raise HTTPException(status_code=418, detail="Error updating user")


@router.put("/{id}", response_model=schemas.User, operation_id="replaceUserById", responses={
    418: {"description": "Error updating user"}
})
def replace_user_by_id(id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(models.User).filter(models.User.id == id).first()
        if existing_user:
            existing_user.username = user.username
            existing_user.password = user.password  # Hash the password in a real application
            existing_user.is_active = user.is_active if user.is_active is not None else existing_user.is_active
            existing_user.updated_by = -1
            db.commit()
            db.refresh(existing_user)
            return schemas.User.from_orm(existing_user)
        raise HTTPException(status_code=404, detail="User not found")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error updating user: {e}")
        raise HTTPException(status_code=418, detail="Error updating user")


@router.delete("/{id}", response_model=schemas.User, operation_id="deleteUserById", responses={
    418: {"description": "Error deleting user"}
})
def delete_user_by_id(id: int, user: schemas.UserDelete, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(models.User).filter(models.User.id == id).first()
        if existing_user:
            if user.is_deleted is not None:
                existing_user.is_deleted = user.is_deleted

            if user.is_archived is not None:
                existing_user.is_archived = user.is_archived

            db.commit()
            db.refresh(existing_user)
            return schemas.User.from_orm(existing_user)
        raise HTTPException(status_code=404, detail="User not found")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error deleting user: {e}")
        raise HTTPException(status_code=418, detail="Error deleting user")