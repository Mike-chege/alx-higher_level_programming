#!/usr/bin/python3
"""
This script  contains the class definition of a
State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class State Definition
    Stores states information based in id and name
    """
    # Name of the MySql table to store state's info
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
