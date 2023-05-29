#!/usr/bin/python3
# Task 7

import sys

def safe_print_integer_err(value):
    """
    prints an integer with error message
    """
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
