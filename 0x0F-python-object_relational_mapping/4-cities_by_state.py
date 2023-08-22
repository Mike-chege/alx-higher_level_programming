#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
And takes three arguments
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    crs = db.cursor()
    crs.execute('''
            SELECT cty.id,
            cty.name, ste.name FROM cities as cty
            INNER JOIN states as ste
            ON cty.state_id=ste.id
            ORDER BY cty.id''')
    [print(city) for city in crs.fetchall()]
