#!/usr/bin/python3
"""This script lists all states from the database hbnt_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    """The Mysql Connecting"""
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost',
            user=username,
            password=password,
            db=database_name,
            port=3306
            )
    # Set cursor
    cursor = db.cursor()
    # SQL request
    cursor.execute("SELECT * FROM states")
    # Result of SQL request
    states = cursor.fetchall()
    # Display result
    for state in states:
        print(state)
    # close cursor and database
    cursor.close()
    db.close()
