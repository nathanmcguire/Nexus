from pydantic import BaseModel

class DeviceBase(BaseModel):
    name: str
    description: str | None = None

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int

    class Config:
        from_attributes = True