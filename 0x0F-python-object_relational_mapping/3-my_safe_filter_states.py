#!/usr/bin/python3
'''Displays values in the states table where name matches the argument given'''

import sys
import MySQLdb


def listStatesArg(username, password, database, arg):
    '''lists all states like arg'''
    # connect to SQL server
    db = MySQLdb.connect(
            host='localhost', port=3306, user=username,
            passwd=password, db=database)

    # Create cursor object
    cursor = db.cursor()

    # SQL statement
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (arg, ))

    # Fetch all and print
    states = cursor.fetchall()
    for state in states:
        print(state)

    # close cursor and database
    cursor.close()
    db.close()


if __name__ == '__main__':
    if (len(sys.argv) < 5):
        print("fewer: arguments")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    arg = sys.argv[4]

    # call list function
    listStatesArg(username, password, database, arg)
