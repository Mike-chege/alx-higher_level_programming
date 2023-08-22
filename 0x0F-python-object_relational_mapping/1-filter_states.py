#!/usr/bin/python3
"""
This script Lists states with a name starting with (N)
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    crs = db.cursor()
    crs.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in crs.fetchall() if state[1][0] == "N"]
