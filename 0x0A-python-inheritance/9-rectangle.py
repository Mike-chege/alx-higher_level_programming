#!/usr/bin/python3
"""A class Rectangle that inherits from(7-base_geometry.py)"""



BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle which inherits from basegeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        using the str method for str and print
        """
        string = "[Rectangle] "
        string += str(self.__width) + '/' + str(self.__height)
        return string

    def area(self):
        """
        method area overrides parent's method
        """
        return (self.__width * self.__height)
