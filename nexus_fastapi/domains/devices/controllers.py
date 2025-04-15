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

@router.get("/devices/{device_id}", response_model=schemas.Device, tags=["Devices"])
def get_device(device_id: int, db: Session = Depends(get_db)):
    """Retrieve a single device by ID."""
    return db.query(models.Device).filter(models.Device.id == device_id).first()

@router.put("/devices/{device_id}", response_model=schemas.Device, tags=["Devices"])
def update_device(device_id: int, device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    """Update an existing device by ID."""
    db_device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if not db_device:
        return None
    for key, value in device.dict().items():
        setattr(db_device, key, value)
    db.commit()
    db.refresh(db_device)
    return db_device

@router.delete("/devices/{device_id}", tags=["Devices"])
def delete_device(device_id: int, db: Session = Depends(get_db)):
    """Delete a device by ID."""
    db_device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if db_device:
        db.delete(db_device)
        db.commit()
    return {"message": "Device deleted successfully"}