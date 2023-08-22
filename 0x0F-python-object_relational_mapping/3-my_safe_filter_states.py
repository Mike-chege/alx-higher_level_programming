#!/usr/bin/python3
"""
This script displays all in the states table
But this time, is safe from MySQL injections!
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
    crs.execute("SELECT * FROM states")
    # Implementing a list comprehension to print the output
    # And iterate through the state table
    [print(state) for state in crs.fetchall() if state[1] == sys.argv[4]]
