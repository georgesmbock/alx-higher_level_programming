#!/usr/bin/python3
# Mapping a python script to MySQL database
import sys
import MySQLdb

db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        password=sys.argv[2],
        db=sys.argv[3]
        )
c = db.cursor()

c.execute("SELECT * FROM states ORDER BY id ASC")

states = c.fetchall()
for state in states:
    print(state)
c.close()
db.close()
