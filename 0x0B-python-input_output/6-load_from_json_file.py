#!/usr/bin/python3
# Task 6
"""Creates an object from a "JSON file" """
import json


def load_from_json_file(filename):
    """Creating a python object file from json file"""
    with open(filename) as newfile:
        return json.load(newfile)
