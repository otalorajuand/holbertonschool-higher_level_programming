#!/usr/bin/python3
'''
This module lists all states from the database hbtn_0e_0_usa
sorted in ascending order by states.id
'''
import MySQLdb
import sys

def select_states():
    """This function connects to the database and lists all states
       from the database hbtn_0e_0_usa
       sorted in ascending order by states.id"""
       
    db = MySQLdb.connect(host="localhost",
                        port=3306, 
                        user=sys.argv[0], 
                        passwd=sys.argv[1], 
                        db=sys.argv[2])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    db_connection.close()

if __name__ == "__main__":
    select_states()