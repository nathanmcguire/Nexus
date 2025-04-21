from sqlalchemy.orm import Session
from .models import Asset
from .schemas import AssetCreate, AssetUpdate

def get_asset(db: Session, asset_id: int):
    return db.query(Asset).filter(Asset.id == asset_id).first()

def get_assets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Asset).offset(skip).limit(limit).all()

def create_asset(db: Session, asset: AssetCreate):
    db_asset = Asset(name=asset.name, description=asset.description)
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

def update_asset(db: Session, asset_id: int, asset: AssetUpdate):
    db_asset = get_asset(db, asset_id)
    if not db_asset:
        return None
    for key, value in asset.dict(exclude_unset=True).items():
        setattr(db_asset, key, value)
    db.commit()
    db.refresh(db_asset)
    return db_asset

def delete_asset(db: Session, asset_id: int):
    db_asset = get_asset(db, asset_id)
    if not db_asset:
        return None
    db.delete(db_asset)
    db.commit()
    return db_asset