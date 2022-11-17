#!/usr/bin/python3
"""
This module contains the function relationship_states_cities()
"""
from relationship_state import Base, State
from relationship_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def relationship_states_cities():
    """adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    State.metadata.create_all(engine)
    City.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    conn = engine.connect()
    session = Session(bind=conn)

    new_state = State(name='California')
    new_city = City(name="san fransico")
    new_state.cities = [new_city]
    session.add_all([new_state])
    print(new_city.__dict__)
    session.commit()


if __name__ == "__main__":
    relationship_states_cities()
