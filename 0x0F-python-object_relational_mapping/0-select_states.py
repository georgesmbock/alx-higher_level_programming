#!/usr/bin/python3
# Mapping a python script to MySQL database
import sys
import MySQLdb

if __name__ == '__main__':
    """ List all states """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            port=3306,
            password=password,
            db=database
            )

    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY id ASC")

    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()
