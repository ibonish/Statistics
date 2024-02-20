from fastapi import APIRouter, Depends, Query
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.crud.data import data_crud
from app.servises.statistics import get_data_statistics

router = APIRouter()


@router.get("/")
async def analyze_statistics(
    start_date: datetime = Query(
        None,
        description="YYYY-MM-DD HH:MM:SS"
    ),
    end_date: datetime = Query(
        None,
        description="YYYY-MM-DD HH:MM:SS"
    ),
    attr: str = Query(
        None,
        description="{x, y, z}"
    ),
    device_id: str = Query(
        None,
        description="id_device"
    ),
    session: AsyncSession = Depends(get_async_session),
):
    data_list = await data_crud.get_all_by_attribute(
        attr,
        session,
        start_date,
        end_date,
        device_id
    )
    return get_data_statistics(data_list)
