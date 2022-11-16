#!/usr/bin/python3
"""
This module contains the function model_state_fetch_all()
"""
from model_city import City
from model_state import Base, State
import sys
from sqlalchemy import create_engine, join
from sqlalchemy.orm import sessionmaker


def model_city_fetch_by_state():
    """prints all City objects from the database hbtn_0e_14_usa"""

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    City.metadata.create_all(engine)
    Base.metadata.create_all(engine)
    State.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    conn = engine.connect()
    session = Session(bind=conn)

    objs = session.query(City.name, City.id, State.name).\
        join(State).order_by(City.id).all()

    for obj in objs:
        print('{}: ({}) {}'.format(obj[2], obj[1], obj[0]))


if __name__ == "__main__":
    model_city_fetch_by_state()
