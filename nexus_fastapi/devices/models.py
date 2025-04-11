from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import datetime

from assets.models import Asset

class Device(Asset):
    __tablename__ = "Devices"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    device_type = Column(String, nullable=False)