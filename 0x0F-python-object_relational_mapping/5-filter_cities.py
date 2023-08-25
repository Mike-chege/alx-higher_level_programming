#!/usr/bin/python3
"""
This script takes in the name of a state as an
argument and lists all cities of that state
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
    crs.execute('''
            SELECT * FROM cities as cty
            INNER JOIN states as ste
            ON cty.state_id=ste.id
            ORDER BY cty.id''')

    print(
            ", ".join(
                [cval[2] for cval in crs.fetchall() if cval[4] == sys.argv[4]]
            )
    )
