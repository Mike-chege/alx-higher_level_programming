#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    # Implementing the cursor
    crs = db.cursor()
    crs.execute("SELECT * FROM states \
            WHERE BINARY name ='{}'".format(sys.argv[4]))
    # Implementing a list comprehension to print the output
    # And also iterate through the values in states with a for loop
    [print(state) for state in crs.fetchall()]
