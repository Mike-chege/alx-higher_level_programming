#!/usr/bin/python3
# Task 7

def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds two tuples
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
