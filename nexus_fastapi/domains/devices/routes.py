from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...database import get_db
from . import schemas, models

router = APIRouter()

@router.get("/devices", response_model=list[schemas.Device], tags=["Devices"])
def list_devices(db: Session = Depends(get_db)):
    """Retrieve a list of all devices."""
    return db.query(models.Device).all()

@router.post("/devices", response_model=schemas.Device, tags=["Devices"])
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    """Create a new device."""
    db_device = models.Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device