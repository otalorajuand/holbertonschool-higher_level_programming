#!/usr/bin/python3
'''
This module lists all states from the database hbtn_0e_0_usa
sorted in ascending order by states.id
'''
import MySQLdb
from sys import argv


def select_states_with_N():
    """This function connects to the database and lists all states
       from the database hbtn_0e_0_usa
       sorted in ascending order by states.id"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states LIKE 'N%' ORDER BY states.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    select_states_with_N()
