from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from ..assets.schemas import Asset

class Network(Asset):
    network_type: str = Field(..., description="Type of the network", example="LAN")

class NetworkInfrastructure(BaseModel):
    topology: Optional[str] = Field(None, description="Network topology", example="Star")
    devices: Optional[list[str]] = Field(None, description="List of devices in the network", example=["Router", "Switch"])

class NetworkArchitecture(BaseModel):
    design: Optional[str] = Field(None, description="Network design", example="Three-tier")
    protocols: Optional[list[str]] = Field(None, description="Protocols used in the network", example=["TCP/IP", "HTTP"])

class ExtendedNetwork(Network):
    infrastructure: Optional[NetworkInfrastructure] = Field(None, description="Details about the network infrastructure")
    architecture: Optional[NetworkArchitecture] = Field(None, description="Details about the network architecture")