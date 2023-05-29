#!/usr/bin/python3
# Task 4

def list_division(my_list_1, my_list_2, list_length):
    """
    A function that divides two lists element by element
    """
    i = 0
    new_list = []
    count = 0
    for i in range(0, list_length):
        try:
            count = (my_list_1[i] / my_list_2[i])
        except TypeError:
            count = 0
            print("wrong type")
        except ZeroDivisionError:
            count = 0
            print("division by 0")
        except IndexError:
            count = 0
            print("out of range")
        finally:
            new_list.append(count)
    return (new_list)
