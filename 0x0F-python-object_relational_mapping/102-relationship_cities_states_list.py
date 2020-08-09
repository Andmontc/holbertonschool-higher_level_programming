#!/usr/bin/python3
"""   script that lists all City objects from the database  """

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
    dbase = session.query(City).order_by(City.id)
    for cities in dbase:
        print("{}: {} -> {}".format(cities.id, cities.name, cities.state.name))
    session.commit()
    session.close()
