#!/usr/bin/python3
"""
This module contains the function model_state_filter_a()
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_filter_a():
    """lists all State objects that contain the letter a from the database hbtn_0e_6_usa"""

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    State.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    conn = engine.connect()
    session = Session(bind=conn)

    objs = session.query(State).order_by(State.id).all()

    for obj in objs:
        if 'a' in obj.name:
            print("{}: {}".format(obj.id, obj.name))


if __name__ == "__main__":
    model_state_filter_a()