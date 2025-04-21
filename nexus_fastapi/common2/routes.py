from fastapi import APIRouter

router = APIRouter(tags=["Common"])

@router.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
def read_root():
    return {"message": "Welcome to the FastAPI app!"}