#!/usr/bin/python3
# Mapping a python script to MySQL database
import sys
import MySQLdb

# List all states
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        port=3306,
        password=mysql_password,
        db=database_name
         )

c = db.cursor()

c.execute("SELECT * FROM states ORDER BY id ASC")

states = c.fetchall()
for state in states:
    print(state)
c.close()
db.close()
