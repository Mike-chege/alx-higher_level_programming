#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 4:
        print(
                "Usage: {} <username> <password> <dbname>".format(args[0])
        )
        exit(1)

    username = args[1]
    password = args[2]
    data = args[3]
    content = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=data,
            port=3306)

    # Implementing the cursor
    cursor = content.cursor()
    row_vals = cursor.execute("SELECT * FROM states ORDER BY states.id")
    # Fetching all results
    results = cursor.fetchall()
    for row in results:
        print(row)
