#!/usr/bin/python3
# Task 3
"""A function that checks if an object is an instance"""


def is_kind_of_class(obj, a_class):
    """checking if an object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
