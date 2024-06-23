#!/usr/bin/python3
# Mapping a python script to MySQL database
import sys
import MySQLdb

def list_states(username, password, database):
    
    db = MySQLdb.connect(
            host="localhost",
            user= username,
            port=3306, 
            password= password, 
            db = database
            )
    c = db.cursor()

    c.execute("SELECT * FROM states")

    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(usernamme, password, database)
