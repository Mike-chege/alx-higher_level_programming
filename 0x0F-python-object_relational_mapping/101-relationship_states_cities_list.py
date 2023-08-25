#!/usr/bin/python3
"""
This script lists all State objects,
And corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from relationship_city import City
from relationship_state import State


if __name__ == '__main__':
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for s in session.query(State).order_by(State.id):
        # Getting the state objects
        print("{}: {}".format(state.id, state.name))
        for c in state.cities:
            # Getting the city objects related to the states
            print("{}: {}".format(city.id, city.name))
