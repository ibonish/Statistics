from pydantic import BaseModel


class DataCreate(BaseModel):
    device_id: int
    x: float
    y: float
    z: float


class DataDB(DataCreate):
    id: int

    class Config:
        orm_mode = True
