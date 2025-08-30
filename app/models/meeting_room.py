# app/models/meeting_room.py

from sqlalchemy import Column, String, Text

from app.core.db import Base
from sqlalchemy.orm import relationship


class MeetingRoom(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    reservations = relationship('Reservation', cascade='delete')

