from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from ..assets.schemas import Asset

class Network(Asset):
    network_type: str = Field(..., description="Type of the network", example="LAN")