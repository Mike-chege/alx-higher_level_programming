#!/usr/bin/python3
# Task 0
"""function that returns the list of available attributes/methods"""


def lookup(obj):
    """Returns a list of available attributes and methods"""
    attributes = [attr for attr in dir(obj) if not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    return sorted(attributes + methods)
