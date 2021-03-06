#!/usr/bin/python3
""" script that lists all State objects with the letter a from the database """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    dbase = session.query(State).order_by(State.id)
    for state in dbase:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
    session.close()
