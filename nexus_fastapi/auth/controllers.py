from datetime import datetime, timedelta
import uuid
from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from sqlalchemy.orm import Session
from . import schemas
from ..database import get_db
from ..users.models import User

router = APIRouter(prefix="/auth", tags=["Authentication"])



SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7



# --- Helper functions ---
def create_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        return None

# --- Auth endpoints ---
@router.post("/login", response_model=schemas.AccessToken, responses={
    400: {"description": "Invalid credentials provided."}
})
def login(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate a user and return access and refresh tokens.

    **Input:**
    - A JSON object of type `schemas.UserLogin` with the following structure:
      ```json
      {
        "username": "string",
        "password": "string"
      }
      ```

    **Output:**
    - A `schemas.Token` object containing:
      - `access_token`: The JWT access token.
      - `refresh_token`: The JWT refresh token.
      - `expires_in`: The expiration time of the access token in seconds.

    **Responses:**
    - `400`: Invalid credentials provided.
    """
    user = db.query(User).filter(User.username == user_login.username).first()
    if not user or user.password != user_login.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_token(
        {"sub": user.username}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    refresh_token = create_token(
        {"sub": user.username, "type": "refresh"}, timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    )
    return schemas.AccessToken(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

@router.post("/refresh", response_model=schemas.AccessToken)
def refresh(token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/refresh"))):
    payload = decode_token(token)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access = create_token(
        {"sub": payload["sub"]}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return schemas.TokenOnly(
        access_token=new_access,
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

@router.get("/me")
def me(token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login"))):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": payload["sub"]}

# Optional logout endpoint (would need a token store/blacklist to invalidate refresh tokens)
@router.post("/logout")
def logout():
    return {"message": "Logout not implemented (requires token storage/blacklist)"}


# --- Personal Token endpoints ---
@router.post("/tokens", response_model=schemas.PersonalToken)
def create_personal_token(data: schemas.PersonalTokenBase, authorization: str = Header(None), db: Session = Depends(get_db)):
    token = authorization.replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.username == payload["sub"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    token_id = str(uuid.uuid4())
    personal_token = create_token({"sub": payload["sub"], "type": "personal", "token_id": token_id}, timedelta(days=365))
    if not hasattr(user, "personal_tokens"):
        user.personal_tokens = {}
    user.personal_tokens[token_id] = {"note": data.note, "token": personal_token}

    return schemas.PersonalToken(token=personal_token, note=data.note)

@router.get("/tokens")
def list_personal_tokens(authorization: str = Header(None), db: Session = Depends(get_db)):
    token = authorization.replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.username == payload["sub"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return [{"token_id": tid, "note": t["note"]} for tid, t in user.personal_tokens.items()]

@router.delete("/tokens/{token_id}")
def delete_personal_token(token_id: str, authorization: str = Header(None), db: Session = Depends(get_db)):
    token = authorization.replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.username == payload["sub"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if token_id not in user.personal_tokens:
        raise HTTPException(status_code=404, detail="Token not found")

    del user.personal_tokens[token_id]
    return {"detail": "Token deleted"}