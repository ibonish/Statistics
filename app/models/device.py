from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.core.db import Base


class Device(Base):
    name = Column(
        String(50)
    )
    data = relationship(
        'Data',
        cascade='delete'
    )
