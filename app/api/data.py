from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.data import data_crud
from app.schemas.data import DataCreate, DataDB

router = APIRouter()


@router.post(
    '/',
    response_model=DataDB,
    response_model_exclude_none=True,
)
async def create_new_data(
        data: DataCreate,
        session: AsyncSession = Depends(get_async_session),
):
    new_data = await data_crud.create(data, session)
    return new_data


@router.get(
    '/',
    response_model=list[DataDB],
    response_model_exclude_none=True,
)
async def get_all_data(
        session: AsyncSession = Depends(get_async_session),
):
    all_data = await data_crud.get_multi(session)
    return all_data
