from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database import Base
from datetime import datetime

from ..assets.models import Asset

class Network(Asset):
    __tablename__ = "Network"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    network_type = Column(String, nullable=False)