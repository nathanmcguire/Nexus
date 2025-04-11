from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import datetime

from ..assets.models import Asset

class Data(Asset):
    __tablename__ = "Data"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    data_sensitivity = Column(String, nullable=False)
