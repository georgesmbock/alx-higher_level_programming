#!/usr/bin/python3
"""This script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument"""
import sys
import MySQLdb
if __name__ == '__main__':
    # Set arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    name = sys.argv[4]
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
    query = "SELECT * FROM states \
            WHERE name =  %s \
            ORDER BY states.id ASC"

    cur.execute(query, (name,))
    # Set result
    states = cur.fetchall()
    for state in states:
        print(state)

    # close cursor and db
    cur.close()
    db.close()
