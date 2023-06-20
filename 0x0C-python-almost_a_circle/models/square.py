#!/usr/bin/python3
# Task 14 Square
"""Updating square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square defintion
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        builder = "[Square] ({}) {}/{} - {}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width)
        return builder

    def update(self, *args, **kwargs):
        """
        using *args argument and **kwargs arguments respectively
        to create the dictionary effectively
        """
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        getting the dictionary
        representation of the square class
        """
        new_d = super().to_dictionary()
        del new_d['height']
        del new_d['width']
        new_d['size'] = self.size
        return new_d

    def to_csv(self):
        """
        Returning a list which contains csv
        representation of the class rectangle
        """
        return [self.id, self.size, self.x, self.y]

    @property
    def size(self):
        """Returning the properties of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
