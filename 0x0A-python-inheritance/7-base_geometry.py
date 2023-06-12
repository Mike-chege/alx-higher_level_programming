#!/usr/bin/python3
# Task 7
"""A class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """Class BaseGeometry representation"""
    def area(self):
        """raising exception not implemnted"""
        raise Exception("area() is not implimented")

    def integer_validator(self, name, value):
        """
        integer validation
        raise:
        TypeError: If value is not an integer
        ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError(name + "must be an integer")
        elif value <= 0:
            raise ValueError(name + "must be greater than 0")
