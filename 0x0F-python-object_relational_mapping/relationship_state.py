#!/usr/bin/python3
"""
This script Improves the files model_city.py
And model_state.py, and saves them as
relationship_city.py and relationship_state.py
"""

from relationship_city import Base, City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class State(Base):
    """
    Class State Definition
    Contains the MySQL database table which stores State's
    information
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete")
