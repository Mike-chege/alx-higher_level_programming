#!/usr/bin/python3
# Task 3

def safe_print_division(a, b):
    """
    A function that divides two integers and prints the result
    """
    try:
        result = a / b
    except (ValueError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return(result)
