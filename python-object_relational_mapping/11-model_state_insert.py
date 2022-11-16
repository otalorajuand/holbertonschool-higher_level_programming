#!/usr/bin/python3
"""
This module contains the function model_state_insert()
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_insert():
    """adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    State.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    conn = engine.connect()
    session = Session(bind=conn)

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == "__main__":
    model_state_insert()
