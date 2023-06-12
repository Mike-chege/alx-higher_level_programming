#!/usr/bin/python3
# Task 2
"""A function that returns True or False"""


def is_name_class(obj, a_class):
    """Returns True or False depending on the output"""
    if not isinstance(a_class, type):
        raise TypeError("a_class must be of type 'type'")
    return (type(obj) is a_class)
