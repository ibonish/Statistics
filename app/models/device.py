from sqlalchemy import Column, ForeignKey, Integer, String
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
    user_id = Column(Integer, ForeignKey('user.id'))
