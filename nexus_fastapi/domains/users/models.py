from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ForeignKey, Enum
from datetime import datetime
from enum import Enum as PyEnum

from ..assets.models import Asset

class UserRole(PyEnum):
    WORKFORCE = "workforce"
    SERVICE_PROVIDER = "service_provider"
    USER_ACCOUNT = "user_account"
    ADMINISTRATOR_ACCOUNT = "administrator_account"
    SERVICE_PROVIDER_ACCOUNT = "service_provider_account"

class User(Asset):
    __tablename__ = "Users"

    id = Column(Integer, ForeignKey('Assets.id'), primary_key=True)
    user_role = Column(Enum(UserRole), nullable=False)