#!/usr/bin/python3
# Task 5
"""unit testing module for 6-max_integer_test.py
"""


import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Define class for testing 6-max_integer_test.py
    """

    def test_max_integer(self):
        """ Test case of positive ordered list of integers
        """
        test_list = [1, 2, 3, 8, 4]
        self.assertEqual(max_int(test_list), 8)

    def test_max_integer_n(self):
        """ Test case for normal list of integers with negatives
        """
        test_list = [1, 2, 3, 8, 4, -40, -400, -12, 0]
        self.assertEqual(max_int(test_list), 8)

    def test_max_integer_empty(self):
        """ Test case for an empty list
        """
        self.assertEqual(max_int([]), None)
