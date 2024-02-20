from datetime import datetime
from sqlalchemy import select
from app.crud.base import CRUDBase
from app.models.data import Data
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDData(CRUDBase):
    async def get_all_by_attribute(
            self,
            attribute_name: str,
            session: AsyncSession,
            start_date: datetime = None,
            stop_date: datetime = None,
            device_id: int = None,
    ):
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


data_crud = CRUDData(Data)
