#!/usr/bin/python3
# Task 7
"""A class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """Class BaseGeometry representation"""
    def area(self):
        """defining area method"""
        raise Exception("area() is not implimented")

    def integer_validator(self, name, value):
        """integer validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
