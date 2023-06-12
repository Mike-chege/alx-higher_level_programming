#!/usr/bin/python3
# Task 8
"""A class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Class Rectange representation"""
    def __init__(self, width, height):
        """inititalizinng the Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

