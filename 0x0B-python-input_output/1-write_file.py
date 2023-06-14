#!/usr/bin/python3
# Task 1
"""Writes a string to a text file(UTF8) & returns writen characters"""


def write_file(filename="", text=""):
    """Writing a string to a text file"""
    with open(filename, "w", encoding="utf-8") as newfile:
        return newfile.write(text)
