from app.crud.base import CRUDBase
from app.models.device import Device


class CRUDDevice(CRUDBase):
    pass


device_crud = CRUDDevice(Device)
