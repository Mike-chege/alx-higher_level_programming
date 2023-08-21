#!/usr/bin/python3
"""
This script Lists states with a name starting with (N)
"""

import sys
import MySQLdb


if __name__ == '__main__':
    args = sys.argv
    username = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=data,
            port=3306)

    # Implementing the cursor
    crs = db.cursor()
    # Listing all states starting with the name N
    row_vals = crs.execute('''
            SELECT * FROM states
            WHERE states.name LIKE 'N%'
            ORDER BY states.id
            ''')
    rows = crs.fetchall()
    for row in rows:
        print(row)
