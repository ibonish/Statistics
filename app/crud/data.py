from datetime import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.data import Data
from app.models.device import Device


class CRUDData(CRUDBase):
    async def get_all_by_attribute(
            self,
            attribute_name: str,
            session: AsyncSession,
            start_date: Optional[datetime] = None,
            stop_date: Optional[datetime] = None,
            device_id: Optional[int] = None,
    ):
        """
        Получение данных из бд.
        """
        if not start_date:
            start_date = await session.execute(
                select(
                    self.model.create_date
                ).where(
                    self.model.id == 1
                )
            )
            start_date = start_date.scalars().first()
            start_date = start_date.strftime('%Y-%m-%d %H:%M:%S.%f')
        attribute = getattr(self.model, attribute_name)
        db_obj = await session.execute(
             select(
                 attribute,
              ).where(
                self.model.create_date.between(
                    start_date,
                    stop_date
                ) if start_date and stop_date else
                self.model.create_date <= stop_date if stop_date else
                self.model.device_id == device_id if device_id else
                self.model.create_date >= start_date
             )
        )
        db_obj = db_obj.scalars().all()
        return db_obj

    async def get_data_by_user_id(
            self,
            user_id: int,
            attribute_name: str,
            session: AsyncSession,
            device_id: Optional[int] = None,
            start_date: Optional[datetime] = None,
            stop_date: Optional[datetime] = None,
    ):
        """
        Получение данных из бд для определённого пользователя
        """
        if not start_date:
            start_date = await session.execute(
                select(
                    self.model.create_date
                ).where(
                    self.model.id == 1
                )
            )
            start_date = start_date.scalars().first()
            start_date = start_date.strftime('%Y-%m-%d %H:%M:%S.%f')

        attribute = getattr(self.model, attribute_name)
        if not device_id:
            device_ids = await session.execute(
                select(Device.id).where(Device.user_id == user_id)
            )
            device_ids = device_ids.scalars().all()
            data_query = await session.execute(
                select(
                    attribute,
                ).where(
                    self.model.create_date.between(
                        start_date,
                        stop_date
                    ) if start_date and stop_date else
                    self.model.create_date <= stop_date if stop_date else
                    self.model.device_id.in_(device_ids) if device_ids else
                    self.model.create_date >= start_date
                )
            )
        else:
            data_query = await session.execute(
                select(
                    attribute,
                ).where(
                    self.model.create_date.between(
                        start_date,
                        stop_date
                    ) if start_date and stop_date else
                    self.model.create_date <= stop_date if stop_date else
                    self.model.device_id == device_id if device_id else
                    self.model.create_date >= start_date
                )
            )
        return data_query.scalars().all()


data_crud = CRUDData(Data)
