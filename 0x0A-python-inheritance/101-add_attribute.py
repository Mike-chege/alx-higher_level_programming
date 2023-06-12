#!/usr/bin/python3
# Task 13
"""Adds a new attribute to an object if possible"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it's posssible
    and raises TypeError Exception
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
