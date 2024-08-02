from sqlalchemy import Column, Integer, String
from .database import Base, engine

class DataItem(Base):
    __tablename__ = 'data_items'
    key = Column(String, primary_key=True, index=True)
    value = Column(String, index=True)
