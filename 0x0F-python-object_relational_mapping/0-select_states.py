#!/usr/bin/python3
"""This script list all rows of tables of the database named hbtn_0e_0_usa"""
# Import libraries
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

    # Initialization of cursor
    cur = db.cursor()
    # SQL request
    cur.execute("SELECT * FROM states")
    # Result
    states = cur.fetchall()
    # Display all rows
    for state in states:
        print(state)
    # Close cursor and database
    cur.close()
    db.close()
