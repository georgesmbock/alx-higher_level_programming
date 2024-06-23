#!/usr/bin/python3
# Mapping a python script to MySQL database
import sys
import MySQLdb

if __name__ == '__main__':
    """ List all states """
    mysql_username = sys.argv[1]
    mySql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            user=mySql_username,
            port=3306,
            password=mySql_password,
            db=database_name
            )

    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY id ASC")

    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()
