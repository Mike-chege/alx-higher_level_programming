#!/usr/bin/python3
# Task 4
"""Function definition"""


def inherits_from(obj, a_class):
    """Returns True or False depending on the output"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
