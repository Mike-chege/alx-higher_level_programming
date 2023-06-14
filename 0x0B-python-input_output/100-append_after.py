#!/usr/bin/python3
# Task 13
"""Inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserting a line of text to the file after each line
    containing a specific string
    """
    insert=""
    with open(filename) as newfile:
        for line in newfile:
            insert += line
            if search_string in line:
                insert += new_string
    with open(filename, "w") as wri:
        wri.write(insert)
