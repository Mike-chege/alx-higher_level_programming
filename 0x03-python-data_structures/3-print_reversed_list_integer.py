#!/usr/bin/python3
# Task 3

def print_reversed_list_integer(my_list=[]):
    """
    output is all the integers of a list in reverse order.
    """
    if type(my_list) is list:
        new_l = my_list[0:]
        new_l.reverse()
        for i in range(len(new_l)):
            print("{:d}".format(new_l[i]))
