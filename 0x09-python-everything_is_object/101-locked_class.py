#!/usr/bin/python3
# Task 30
"""Class LockedClass definition with no class or object attribute"""


class LockedClass:
    """
    LockedClass with no class or object attribute
    """
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
