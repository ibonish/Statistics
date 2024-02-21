from typing import Optional

from pydantic import BaseModel, Field


class DeviceCreate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)


class DeviceDB(DeviceCreate):
    id: int
    user_id: Optional[int]

    class Config:
        orm_mode = True
