from datetime import datetime

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.data import data_crud
from app.servises.statistics import get_data_statistics


router = APIRouter()

START_DATE = 'Дата начала временного периода YYYY-MM-DD HH:MM:SS'
END_DATE = 'Дата окончания временного периода YYYY-MM-DD HH:MM:SS'
ATTR = 'Величина, по которой нужно расчитать статистику {x, y, z}'
DEVICE_ID = 'Идентификатор устройства'


@router.get("/")
async def analyze_statistics_from_device(
    start_date: datetime = Query(
        None,
        description=START_DATE
    ),
    end_date: datetime = Query(
        None,
        description=END_DATE
    ),
    attr: str = Query(
        'x',
        description=ATTR
    ),
    device_id: str = Query(
        None,
        description=DEVICE_ID
    ),
    session: AsyncSession = Depends(get_async_session),
) -> dict:
    """
    Анализ собранной статистики с устройства (или со всех)\n
    за определенный период или за все время.\n
    Query parameters:\n
        * start_date – Дата начала временного периода\n
        * end_date - Дата окончания временного периода\n
        * attr - Величина, по которой нужно расчитать статистику\n
        * device_id - Идентификатор устройства\n
    Пример ответа:\n
        {
            "минимальное значение": 30,
            "максимальное значение": 30,
            "количество": 1,
            "сумма": 30,
            "медиана": 30
        }
    """
    data = await data_crud.get_all_by_attribute(
        attr,
        session,
        start_date,
        end_date,
        device_id
    )
    return get_data_statistics(data)


@router.get(
    '/{user_id}',
)
async def analyze_statistics_from_user(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        attr: str = Query(
            'x',
            description=ATTR
        ),
        device_id: str = Query(
            None,
            description=DEVICE_ID
        ),
        start_date: datetime = Query(
            None,
            description=START_DATE
        ),
        end_date: datetime = Query(
            None,
            description=END_DATE
        ),
) -> dict:
    """
    Анализ собранной статистики с устройства (или со всех)\n
    за определенный период или за все время у определённого пользователя.\n
    Query parameters:\n
        * user_id - Идентификатор пользователя\n
        * start_date – Дата начала временного периода\n
        * end_date - Дата окончания временного периода\n
        * attr - Величина, по которой нужно расчитать статистику\n
        * device_id - Идентификатор устройства\n
    Пример ответа:\n
        {
            "минимальное значение": 30,
            "максимальное значение": 30,
            "количество": 1,
            "сумма": 30,
            "медиана": 30
        }
    """
    data = await data_crud.get_data_by_user_id(
        user_id,
        attr,
        session,
        device_id,
        start_date,
        end_date,
    )
    return get_data_statistics(data)
