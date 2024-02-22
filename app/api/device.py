from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user_or_none
from app.crud.device import device_crud
from app.models import User
from app.schemas.device import DeviceCreate, DeviceDB

router = APIRouter()


@router.post(
        '/',
        response_model=DeviceDB
)
async def create_device(
        reservation: DeviceCreate,
        session: AsyncSession = Depends(get_async_session),
        user: Optional[User] = Depends(current_user_or_none),
):
    """
    Эндпоинт для создания нового устройства.\n
    Если запрос отправлен от аторизованного пользователя,\n
    его идентификатор сохранается в бд в таблице device.\n
       * name - имя устройства
    """
    new_reservation = await device_crud.create(
        reservation, session, user
    )
    return new_reservation


@router.get(
    '/',
    response_model=list[DeviceDB],
    response_model_exclude_none=True,
)
async def get_all_devices(
        session: AsyncSession = Depends(get_async_session),
):
    """
    Получение всех устройств.
    """
    all_rooms = await device_crud.get_multi(session)
    return all_rooms
