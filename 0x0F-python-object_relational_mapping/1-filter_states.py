#!/usr/bin/python3
'''Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:'''

import sys
import MySQLdb


def listStatesN(userName, password, database):
    '''function to list states starting with N'''
    # connect to database
    db = MySQLdb.connect(
            'host=localhost', port=33306, user=username,
            passwd=password, db=database)

    # create cursor object
    cursor = db.cursor()

    # SQL statement to get states
    cursor.execute(
            "SELECT * FROM states "
            "WHERE states.name LIKE 'N%' ORDER BY states.id ASC")

    # Fetch and print all the states
    states = cursor.fetchall()
    for state in states:
        print(state)

    # close cursor and database
    cursor.close()
    db.close()


if '__name__' == '__main__':
    if (len(sys.argv) < 4):
        print("Fewer arguments")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # call function to list states
    listStatesN(username, password, database)
