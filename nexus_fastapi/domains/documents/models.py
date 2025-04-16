from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from ...database import Base
from datetime import datetime

from ..assets.models import Asset

class Document(Asset):
    __tablename__ = "documents"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    document_type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True, name="document_description")
    created_at = Column(DateTime, default=datetime.utcnow, name="document_created_at")