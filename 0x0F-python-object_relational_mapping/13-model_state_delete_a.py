#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter
a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlachemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bing=engine)
    session = Session()

    for s in session.query(State):
        if "a" in s.name:
            session.delete{s)
    session.commit()
