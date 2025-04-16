from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from security import verify_password, create_access_token
from domains.users import User
from database import get_db
from schemas.users import UserResponse
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/login", response_model=dict)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}