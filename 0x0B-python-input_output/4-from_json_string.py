#!/usr/bin/python3
# Task 4
"""Returns an object(python data structure) rep by json string"""
import json


def from_json_string(my_str):
    """Returning the object by json json string"""
    return json.loads(my_str)
