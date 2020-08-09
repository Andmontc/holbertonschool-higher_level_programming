#!/usr/bin/python3
"""   script that lists all objects contained in the database  """

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    dbase = session.query(State).order_by(State.id)
    for states in dbase:
        print("{}: {}".format(states.id, states.name))
        for city in states.cities:
            print("    {}: {}".format(city.id, city.name))
    session.commit()
    session.close()
