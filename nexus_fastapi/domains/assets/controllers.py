from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import services, schemas
from ...database import get_db

router = APIRouter(prefix="/assets", tags=["Assets"])

@router.get("/{asset_id}", response_model=schemas.Asset)
def read_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = services.get_asset(db, asset_id=asset_id)
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@router.get("/", response_model=list[schemas.Asset])
def read_assets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.get_assets(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Asset)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    return services.create_asset(db=db, asset=asset)

@router.put("/{asset_id}", response_model=schemas.Asset)
def update_asset(asset_id: int, asset: schemas.AssetUpdate, db: Session = Depends(get_db)):
    db_asset = services.update_asset(db=db, asset_id=asset_id, asset=asset)
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@router.delete("/{asset_id}", response_model=schemas.Asset)
def delete_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = services.delete_asset(db=db, asset_id=asset_id)
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset