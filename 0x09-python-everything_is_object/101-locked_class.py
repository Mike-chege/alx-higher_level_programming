#!/usr/bin/python3
# Task 30
"""Class LockedClass definition with no class or object attribute"""


class LockedClass:
    """
    class LockedClass with no class or object attribute
    which  prevents the user from dynamically creating new
    instance attributes, except if the new instance attribute
    is called first_name
    """
    __slots__ = ["first_name"]
