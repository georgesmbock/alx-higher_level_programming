#!/usr/bin/python3
"""This script lists all states with a name starting with N(upper N)
from database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Set arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    # Set connection
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            password=password,
            db=database_name,
            port=3306
            )
    # Set cursor
    cur = db.cursor()
    # SQL request
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")
    # Rquest result
    states = cur.fetchall()
    # Display result
    for state in states:
        print(state)

    # Close cursor and db
    cur.close()
    db.close()
