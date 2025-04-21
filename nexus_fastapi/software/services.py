from typing import List, Optional
from .models import Software as SoftwareModel
from .schemas import Software
from sqlalchemy.orm import Session
from fastapi import Depends
from ...database import get_db

class SoftwareService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_all_software(self) -> List[SoftwareModel]:
        return self.db.query(SoftwareModel).all()

    def get_software(self, software_id: int) -> Optional[SoftwareModel]:
        return self.db.query(SoftwareModel).filter(SoftwareModel.id == software_id).first()

    def create_software(self, software: Software) -> SoftwareModel:
        new_software = SoftwareModel(**software.dict())
        self.db.add(new_software)
        self.db.commit()
        self.db.refresh(new_software)
        return new_software

    def update_software(self, software_id: int, software: Software) -> Optional[SoftwareModel]:
        existing_software = self.get_software(software_id)
        if not existing_software:
            return None
        for key, value in software.dict().items():
            setattr(existing_software, key, value)
        self.db.commit()
        self.db.refresh(existing_software)
        return existing_software

    def delete_software(self, software_id: int) -> bool:
        software = self.get_software(software_id)
        if not software:
            return False
        self.db.delete(software)
        self.db.commit()
        return True