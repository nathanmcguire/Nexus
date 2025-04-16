from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..assets.models import Asset
from datetime import datetime

class Data(Asset):
    __tablename__ = "Data"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    data_sensitivity = Column(String, nullable=False)
