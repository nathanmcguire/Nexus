from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ForeignKey
from ...database import Base
from datetime import datetime

from ..assets.models import Asset

class Network(Asset):
    __tablename__ = "Networks"  # Ensure the table name matches the convention

    id = Column(Integer, ForeignKey('Assets.id', ondelete="CASCADE"), primary_key=True)
    network_type = Column(String, nullable=False)

# Ensure the foreign key references the correct table name
class NetworkInfrastructure(Base):
    __tablename__ = "NetworkInfrastructure"

    id = Column(Integer, primary_key=True, autoincrement=True)
    network_id = Column(Integer, ForeignKey('Networks.id', ondelete="CASCADE"))
    topology = Column(String, nullable=True)
    devices = Column(String, nullable=True)  # Store as a comma-separated string

class NetworkArchitecture(Base):
    __tablename__ = "NetworkArchitecture"

    id = Column(Integer, primary_key=True, autoincrement=True)
    network_id = Column(Integer, ForeignKey('Networks.id', ondelete="CASCADE"))
    design = Column(String, nullable=True)
    protocols = Column(String, nullable=True)  # Store as a comma-separated string