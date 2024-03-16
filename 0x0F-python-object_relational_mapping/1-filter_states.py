#!/usr/bin/python3
'''function to list states starting with N'''
import sys
import MySQLdb


def listStatesN(username, password, database):
    '''Function to list states starting with N'''
    # Connect to the database
    db = MySQLdb.connect(
            host='localhost', port=3306, user=username,
            passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to retrieve states starting with 'N' and ordered by ID
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the matching states
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states
    listStatesN(username, password, database)
