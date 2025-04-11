from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import datetime

from assets.models import Asset

class User(Asset):
    __tablename__ = "Users"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    user_role = Column(String, nullable=False)