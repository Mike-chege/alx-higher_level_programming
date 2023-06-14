#!/usr/bin/python3
# Task 13
"""Inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserting text to the file after each line
    containing a specific string
    """
    with open(filename) as newfile:
        for line in newfile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wri:
        wri.write(text)
