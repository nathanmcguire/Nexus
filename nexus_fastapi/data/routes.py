from fastapi import APIRouter, HTTPException, Query
from typing import List
from data import schemas as schemas
from data import models as models

# Initialize router for data-related endpoints
router = APIRouter(tags=["Data"])

# In-memory storage for demonstration purposes
data_items = []

@router.get("/data", response_model=List[schemas.Data])
def get_data():
    return data_items

@router.post("/data", response_model=schemas.Data)
def create_data(data: schemas.Data):
    new_data = models.Data(**data.dict())
    data_items.append(new_data)
    return new_data

@router.get("/data/{id}", response_model=schemas.Data)
def get_data_item(id: int):
    for data in data_items:
        if data.id == id:
            return data
    raise HTTPException(status_code=404, detail="Data not found")

@router.put("/data/{id}", response_model=schemas.Data)
def update_data(id: int, updated_data: schemas.Data):
    for index, data in enumerate(data_items):
        if data.id == id:
            updated_data_dict = updated_data.dict()
            data_items[index] = models.Data(**updated_data_dict)
            return data_items[index]
    raise HTTPException(status_code=404, detail="Data not found")

@router.patch("/data/{id}", response_model=schemas.Data)
def partial_update_data(id: int, partial_data: schemas.Data):
    for index, data in enumerate(data_items):
        if data.id == id:
            updated_data_dict = data.dict()
            updated_data_dict.update(partial_data.dict(exclude_unset=True))
            data_items[index] = models.Data(**updated_data_dict)
            return data_items[index]
    raise HTTPException(status_code=404, detail="Data not found")

@router.delete("/data/{id}", response_model=dict)
def delete_data(id: int):
    for index, data in enumerate(data_items):
        if data.id == id:
            del data_items[index]
            return {"message": "Data deleted successfully"}
    raise HTTPException(status_code=404, detail="Data not found")