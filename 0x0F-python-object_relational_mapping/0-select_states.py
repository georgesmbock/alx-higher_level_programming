#!/usr/bin/python3
# Mapping a python script to MySQL database
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            port=3306,
            password=password,
            db=database
            )
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY id ASC")

    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()
