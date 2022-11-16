#!/usr/bin/python3
"""
This module contains the function model_state_delete_a()
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker


def model_state_delete_a():
    """deletes all State objects with a name containing the
      letter a from the database hbtn_0e_6_usa"""

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    State.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    conn = engine.connect()
    session = Session(bind=conn)

    '''
    objs = session.query(State).order_by('id').all()

    for obj in objs:
        if 'a' in obj.name:
            session.delete(obj)

    session.commit()
    session.close()
    '''
    instances = session.query(State).order_by(
        'id').filter(State.name.contains('a'))

    for instance in instances:
        session.delete(instance)
    session.commit()


if __name__ == "__main__":
    model_state_delete_a()
