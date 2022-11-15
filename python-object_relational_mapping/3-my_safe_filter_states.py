#!/usr/bin/python3
'''
This module contains the function my_safe_filter_states
'''
import MySQLdb
from sys import argv


def my_safe_filter_states():
    """This function connects to the database and displays all 
    values in the states table of hbtn_0e_0_usa where name matches 
    the argument. But this time, write one that is safe from MySQL injections!"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3])

    if ';' in argv[4]:
        return

    cur = db.cursor()
    query = "SELECT id, name FROM states WHERE BINARY name = '{}' \
             ORDER BY states.id ASC".format(argv[4])
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
