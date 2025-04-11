from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import datetime

from nexus_fastapi.assets.models import Asset

class Network(Asset):
    __tablename__ = "Network"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    network_type = Column(String, nullable=False)