from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.device import device_crud
from app.schemas.device import DeviceCreate, DeviceDB

router = APIRouter()


@router.post(
    '/',
    response_model=DeviceDB,
    response_model_exclude_none=True,
)
async def create_new_device(
        device: DeviceCreate,
        session: AsyncSession = Depends(get_async_session),
):
    new_device = await device_crud.create(device, session)
    return new_device


@router.get(
    '/',
    response_model=list[DeviceDB],
    response_model_exclude_none=True,
)
async def get_all_devices(
        session: AsyncSession = Depends(get_async_session),
):
    all_rooms = await device_crud.get_multi(session)
    return all_rooms
