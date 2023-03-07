from sqlalchemy import Column, Integer, DateTime, String
from .base import Base


class Log(Base):
    """This class declares schema of 'Log' table"""
    __tablename__ = 'Log'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    type = Column(String)
    message = Column(String)
