#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
     """
    Prints all integers of a list in reverse order.

    Args:
        my_list (list of int): The list of integers to print in reverse order.
            Defaults to an empty list if not provided.
    """
    if type(my_list) is list:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
