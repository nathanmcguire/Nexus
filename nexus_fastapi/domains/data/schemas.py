from pydantic import BaseModel, Field
from typing import Optional
from ..assets.schemas import AssetBase

class DataBase(AssetBase):
    data_sensitivity: str = Field(..., description="Sensitivity level of the data", example="High")

class DataCreate(DataBase):
    pass

class DataUpdate(DataBase):
    pass

class Data(DataBase):
    id: int

    class Config:
        from_attributes = True