from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database import Base
from datetime import datetime

from ..assets.models import Asset

class Software(Asset):
    __tablename__ = "Software"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    software_version = Column(String, nullable=False)
