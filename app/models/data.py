from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Float

from app.core.db import Base


class Data(Base):
    device_id = Column(
        Integer,
        ForeignKey('device.id')
    )
    x = Column(
        Float,
        nullable=False
    )
    y = Column(
        Float,
        nullable=False
    )
    z = Column(
        Float,
        nullable=False
    )
    create_date = Column(
        DateTime,
        default=datetime.now,
        nullable=False
    )
