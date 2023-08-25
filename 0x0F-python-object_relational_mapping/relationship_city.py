#!/usr/bin/python3
"""
This script Improves the files model_city.py
And model_state.py, and save them as
relationship_city.py and relationship_state.py
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()


class City(Base):
    """
    Class City Definition
    Contains the information about the city object
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
