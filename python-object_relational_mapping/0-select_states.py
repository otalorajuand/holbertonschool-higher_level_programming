#!/usr/bin/python3
'''
This module lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys


db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[0], passwd=sys.argv[1], db=sys.argv[2])
cur = db.cursor()
cur.execute("SELECT id, name FROM states")

rows = cur.fetchall()
for row in rows:
    print(row)