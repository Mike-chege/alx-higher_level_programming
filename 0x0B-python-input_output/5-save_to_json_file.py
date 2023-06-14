#!/usr/bin/python3
# Task 5
"""Writing an object to text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Wring an object to a text file"""
    with open(filename, "w") as newfile:
        json.dump(my_obj, newfile)
