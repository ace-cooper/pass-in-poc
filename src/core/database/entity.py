from src.core.database.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Entity(Base):
    # __tablename__ = 'entities'

    id = Column(String, primary_key=True)
