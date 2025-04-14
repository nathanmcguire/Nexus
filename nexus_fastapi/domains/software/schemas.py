from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

from assets.schemas import Asset

class SoftwareType(str, Enum):
    APPLICATION = "Application"
    OPERATING_SYSTEM = "Operating System"
    FIRMWARE = "Firmware"

class Software(Asset):
    software_version: str = Field(..., description="Version of the software", example="1.0.0")
    software_type: SoftwareType = Field(..., description="Type of the software", example="Application")
    release_date: Optional[datetime] = Field(None, description="Release date of the software", example="2025-01-01")

