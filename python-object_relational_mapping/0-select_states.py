#!/usr/bin/python3
'''
This module lists all states from the database hbtn_0e_0_usa
sorted in ascending order by states.id
'''
import MySQLdb
from sys import argv

def select_states():
    """This function connects to the database and lists all states
       from the database hbtn_0e_0_usa
       sorted in ascending order by states.id"""

    '''   
    db = MySQLdb.connect(host="localhost",
                         port=3306, 
                         user=sys.argv[1], 
                         password=sys.argv[2], 
                         database=sys.argv[3])
    '''

    sql_usrname, sql_password, sql_database = argv[1], argv[2], argv[3]
    host = "localhost"
    port = 3306

    """ SETTING MySQLdb Connection """
    db_connection = MySQLdb.connect(
        port=port,
        host=host,
        user=sql_usrname,
        password=sql_password,
        database=sql_database)

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    db_connection.close()

if __name__ == "__main__":
    select_states()