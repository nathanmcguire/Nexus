from sqlalchemy.orm import Session
from .models import Data
from .schemas import DataCreate, DataUpdate

# Service functions
def get_data(db: Session, data_id: int):
    return db.query(Data).filter(Data.id == data_id).first()

def get_all_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Data).offset(skip).limit(limit).all()

def create_data(db: Session, data: DataCreate):
    db_data = Data(name=data.name, description=data.description, data_sensitivity=data.data_sensitivity)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def update_data(db: Session, data_id: int, data: DataUpdate):
    db_data = get_data(db, data_id)
    if not db_data:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(db_data, key, value)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_data(db: Session, data_id: int):
    db_data = get_data(db, data_id)
    if not db_data:
        return None
    db.delete(db_data)
    db.commit()
    return db_data