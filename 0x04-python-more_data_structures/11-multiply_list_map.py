#!/usr/bin/python3
# Task 11

def multiply_list_map(my_list=[], number=0):
    """use map to multiply each value in the list by the number"""
    return list(map(lambda x: x * number, my_list))
