#!/usr/bin/python3
# Task 7
"""A class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """class BaseGeometry representation"""

    def area(self):
        """if not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validation
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
