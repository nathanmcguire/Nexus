from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import models, schemas


def create_user_service(user: schemas.UserCreate, db: Session):
    # Check if the username is already taken
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")

    # Create the User instance
    new_user = models.User(
        username=user.username,
        password=user.password,
        enabled=user.enabled,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Refresh to get the generated fields like id, guid, etc.
    return new_user


def get_users_service(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return users


def get_user_service(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


def put_user_service(user_id: int, user: schemas.UserUpdate, db: Session):
    # Check if the user exists
    existing_user = db.query(models.User).filter(models.User.id == user_id).first()
    
    if not existing_user:
        # Use UserCreate schema to create a new user
        new_user = schemas.UserReplace(
            id=user_id,  # Use the specified ID
            username=user.username,
            password=user.password,
            enabled=user.enabled,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    # Update the existing user details
    existing_user.username = user.username
    existing_user.password = user.password
    existing_user.enabled = user.enabled

    db.commit()
    db.refresh(existing_user)
    return existing_user
