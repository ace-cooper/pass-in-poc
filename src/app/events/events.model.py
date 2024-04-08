from src.core.database.entity import Entity
from sqlalchemy import Column, Integer, String, ForeignKey

class Event(Entity):
    __tablename__ = 'events'

    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)