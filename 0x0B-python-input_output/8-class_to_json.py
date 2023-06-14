#!/usr/bin/python3
# Task 8
"""Returns dictionary description with simple data structure"""


def class_to_json(obj):
    """Returning dictionary representation"""
    return obj.__dict__
