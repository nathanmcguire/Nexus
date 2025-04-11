from fastapi import APIRouter, HTTPException, Query
from typing import List
from . import schemas as schemas
from . import models as models


# Initialize router for asset-related endpoints
router = APIRouter(tags=["Assets"])

# In-memory storage for demonstration purposes
assets = []

# Removed asset scope from the endpoints
@router.get("/assets", response_model=List[schemas.Asset])
def get_assets():
    return assets

@router.post("/assets", response_model=schemas.Asset)
def create_asset(asset: schemas.Asset):
    new_asset = models.Asset(**asset.dict())
    assets.append(new_asset)
    return new_asset

@router.get("/assets/{id}", response_model=schemas.Asset)
def get_asset(id: int):
    for asset in assets:
        if asset.id == id:
            return asset
    raise HTTPException(status_code=404, detail="Asset not found")

@router.put("/assets/{id}", response_model=schemas.Asset)
def update_asset(id: int, updated_asset: schemas.Asset):
    for index, asset in enumerate(assets):
        if asset.id == id:
            updated_asset_dict = updated_asset.dict()
            assets[index] = models.Asset(**updated_asset_dict)
            return assets[index]
    raise HTTPException(status_code=404, detail="Asset not found")

@router.patch("/assets/{id}", response_model=schemas.Asset)
def partial_update_asset(id: int, partial_asset: schemas.Asset):
    for index, asset in enumerate(assets):
        if asset.id == id:
            updated_asset_dict = asset.dict()
            updated_asset_dict.update(partial_asset.dict(exclude_unset=True))
            assets[index] = models.Asset(**updated_asset_dict)
            return assets[index]
    raise HTTPException(status_code=404, detail="Asset not found")

@router.delete("/assets/{id}", response_model=dict)
def delete_asset(id: int):
    for index, asset in enumerate(assets):
        if asset.id == id:
            del assets[index]
            return {"message": "Asset deleted successfully"}
    raise HTTPException(status_code=404, detail="Asset not found")