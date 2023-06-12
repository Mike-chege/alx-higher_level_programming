#!/usr/bin/python3
# Task 2
"""A function that checks if an object is an instance a class"""


def is_same_class(obj, a_class):
    """
    checking if an object is exactly an instance of
    a class"""
    if type(obj) == a_class:
        return True
    return False
