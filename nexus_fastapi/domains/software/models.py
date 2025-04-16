from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ForeignKey, Enum
from ...database import Base
from datetime import datetime
from enum import Enum as PyEnum

from ..assets.models import Asset

class SoftwareType(PyEnum):
    APPLICATION = "Application"
    OPERATING_SYSTEM = "Operating System"
    FIRMWARE = "Firmware"

class Software(Asset):
    __tablename__ = "Software"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    software_version = Column(String, nullable=False)
    software_type = Column(Enum(SoftwareType), nullable=False)
    release_date = Column(DateTime, nullable=True)
