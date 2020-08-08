#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the database """

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
    newname = State(name="Louisiana")
    session.add(newname)
    dbase = session.query(State).filter_by(name="Louisiana").first()
    print(dbase.id)
    session.commit()
    session.close()
