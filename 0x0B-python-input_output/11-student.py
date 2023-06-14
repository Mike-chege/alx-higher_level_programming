#!/usr/bin/python3
# Task 11
"""Class defintion based on 10-student.py"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {ky: getattr(self, ky) for ky in attrs if hasattr(self, ky)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student
        """
        for ky, v in json.items():
            setattr(self, ky, v)
