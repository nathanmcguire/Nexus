from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

from ..assets.models import Asset

class Device(Asset):
    __tablename__ = "Devices"

    device_type = Column(String, nullable=False)