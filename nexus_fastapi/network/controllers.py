from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .services import (
    get_all_network_assets,
    create_network_asset,
    get_network_asset,
    update_network_asset,
    delete_network_asset
)
from .schemas import Network, ExtendedNetwork
from ...database import get_db

router = APIRouter(prefix="/network", tags=["Network"])

@router.get("/", response_model=list[ExtendedNetwork])
def get_all_assets(db: Session = Depends(get_db)):
    try:
        return get_all_network_assets(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/", response_model=Network)
def add_network_asset(network: Network, db: Session = Depends(get_db)):
    try:
        return create_network_asset(db, network)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{network_id}", response_model=ExtendedNetwork)
def get_asset(network_id: int, db: Session = Depends(get_db)):
    try:
        return get_network_asset(db, network_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{network_id}", response_model=Network)
def update_asset(network_id: int, network: Network, db: Session = Depends(get_db)):
    try:
        return update_network_asset(db, network_id, network)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{network_id}", response_model=dict)
def delete_asset(network_id: int, db: Session = Depends(get_db)):
    try:
        delete_network_asset(db, network_id)
        return {"message": "Network asset deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))