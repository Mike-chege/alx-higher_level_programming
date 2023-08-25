#!/usr/bin/python3
"""
This script lists all City objects
from the database hbtn_0e_101_us
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

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
