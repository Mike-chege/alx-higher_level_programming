#!/usr/bin/python3
# Task 7

import sys


def safe_print_integer_err(value):
    """
    prints an integer with error message
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
