#!/usr/bin/python3
""" script that takes in an argument and displays all values """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    statename = sys.argv[4]
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id"
              .format(statename))
    r = c.fetchall()
    for rows in r:
        print(rows)
    c.close()
    db.close()
