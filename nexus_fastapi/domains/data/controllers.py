from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import schemas
from ...database import get_db
from .services import get_all_data, get_data, create_data, update_data, delete_data

router = APIRouter(prefix="/data", tags=["Data"])

@router.get("/", response_model=List[schemas.Data])
def get_all_data_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_data(db, skip=skip, limit=limit)

@router.get("/{data_id}", response_model=schemas.Data)
def get_data_endpoint(data_id: int, db: Session = Depends(get_db)):
    data = get_data(db, data_id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.post("/", response_model=schemas.Data)
def create_data_endpoint(data: schemas.DataCreate, db: Session = Depends(get_db)):
    return create_data(db, data)

@router.put("/{data_id}", response_model=schemas.Data)
def update_data_endpoint(data_id: int, data: schemas.DataUpdate, db: Session = Depends(get_db)):
    updated_data = update_data(db, data_id, data)
    if not updated_data:
        raise HTTPException(status_code=404, detail="Data not found")
    return updated_data

@router.delete("/{data_id}", response_model=schemas.Data)
def delete_data_endpoint(data_id: int, db: Session = Depends(get_db)):
    deleted_data = delete_data(db, data_id)
    if not deleted_data:
        raise HTTPException(status_code=404, detail="Data not found")
    return deleted_data