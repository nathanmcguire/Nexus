from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from ..assets.schemas import Asset

class User(Asset):
    user_role: str = Field(..., description="Role of the user", example="Administrator")