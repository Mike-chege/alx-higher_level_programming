#!/usr/bin/python3
# Task 8

import sys


def safe_function(fct, *args):
    """
    This function excecutes a function safely
    and
    Returns the result of the function(count)
    otherwise
    None
    """
    try:
        count = fct(*args)
        return count
    except: 
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
