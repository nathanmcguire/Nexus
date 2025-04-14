from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import schemas, services
from ...database import get_db

router = APIRouter(tags=["Data"])

@router.get("/data", response_model=List[schemas.Data], tags=["Data"])
def get_all_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.get_all_data(db, skip=skip, limit=limit)

@router.get("/data/{data_id}", response_model=schemas.Data, tags=["Data"])
def get_data(data_id: int, db: Session = Depends(get_db)):
    data = services.get_data(db, data_id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.post("/data", response_model=schemas.Data, tags=["Data"])
def create_data(data: schemas.DataCreate, db: Session = Depends(get_db)):
    return services.create_data(db, data)

@router.put("/data/{data_id}", response_model=schemas.Data, tags=["Data"])
def update_data(data_id: int, data: schemas.DataUpdate, db: Session = Depends(get_db)):
    updated_data = services.update_data(db, data_id, data)
    if not updated_data:
        raise HTTPException(status_code=404, detail="Data not found")
    return updated_data

@router.delete("/data/{data_id}", response_model=schemas.Data, tags=["Data"])
def delete_data(data_id: int, db: Session = Depends(get_db)):
    deleted_data = services.delete_data(db, data_id)
    if not deleted_data:
        raise HTTPException(status_code=404, detail="Data not found")
    return deleted_data