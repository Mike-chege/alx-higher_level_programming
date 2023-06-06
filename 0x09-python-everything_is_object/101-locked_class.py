#!/usr/bin/python3
# Task 30
"""LockedClass definition with no class or object attribute"""


class LockedClass:
    """
    No setting instance attributes in LockedClass
    """
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
