#!/usr/bin/python3
'''
This module lists all states from the database hbtn_0e_0_usa
sorted in ascending order by states.id
'''
import MySQLdb
from sys import argv


def my_filter_states():
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
    query = "SELECT id, name FROM states WHERE BINARY name = '{}' \
             ORDER BY states.id ASC".format(argv[4])
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    my_filter_states()
