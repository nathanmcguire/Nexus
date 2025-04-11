from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Asset(Base):
    __tablename__ = "Assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Data(Asset):
    __tablename__ = "Data"

    data_sensitivity = Column(String, nullable=False)

class Device(Asset):
    __tablename__ = "Devices"

    device_type = Column(String, nullable=False)

class Documentation(Asset):
    __tablename__ = "Documentation"

    document_type = Column(String, nullable=False)

class Network(Asset):
    __tablename__ = "Network"

    network_type = Column(String, nullable=False)

class Software(Asset):
    __tablename__ = "Software"

    software_version = Column(String, nullable=False)

class User(Asset):
    __tablename__ = "Users"

    user_role = Column(String, nullable=False)