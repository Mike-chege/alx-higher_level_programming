#!/usr/bin/python3
# Task 11

def delete_at(my_list=[], idx=0):
    """
    deletes the item at a specific position in a list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        return my_list[:idx] + my_list[idx+1:]
