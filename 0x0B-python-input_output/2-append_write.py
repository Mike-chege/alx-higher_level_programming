#!/usr/bin/python3
# Task 2
"""Appends a string at the end of a text file(UTF8)"""


def append_write(filename="", text=""):
    """Appending a string at the end"""
    with open(filename, "a", encoding="utf-8") as newfile:
        return newfile.write(text)
