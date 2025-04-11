from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from ..assets.schemas import Asset

class Device(Asset):
    device_type: str = Field(..., description="Type of the device", example="IoT Device")


