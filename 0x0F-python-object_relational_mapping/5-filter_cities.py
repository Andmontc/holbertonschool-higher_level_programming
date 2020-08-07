#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    statename = sys.argv[4]
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
              JOIN states ON cities.state_id=states.id\
			  WHERE states.name=%s ORDER BY cities.id",(statename,))
    r = c.fetchall()
    print(", ".join([row[1] for row in r]))
    c.close()
    db.close()
