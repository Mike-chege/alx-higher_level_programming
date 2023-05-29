#!/usr/bin/python3
# Task 1

def safe_print_integer(value):
    """
    prints an integer with "{:d}".format()
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
