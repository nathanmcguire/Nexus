from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from ..assets.schemas import Asset

class Data(Asset):
    data_sensitivity: str = Field(..., description="Sensitivity level of the data", example="High")