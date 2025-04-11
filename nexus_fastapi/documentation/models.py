from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import datetime

from assets.models import Asset

class Documentation(Asset):
    __tablename__ = "Documentation"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    document_type = Column(String, nullable=False)