from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from ..assets.schemas import Asset

class Software(Asset):
    software_version: str = Field(..., description="Version of the software", example="1.0.0")

