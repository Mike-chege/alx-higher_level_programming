#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    # Implementing the cursor
    crs = db.cursor()
    crs.execute("SELECT * FROM states ORDER BY states.id")
    # Using list comprehension to print arg[0] and fetch results
    [print(state) for state in crs.fetchall()]
