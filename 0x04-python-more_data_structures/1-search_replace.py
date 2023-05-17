#!/usr/bin/python3
# Task 2

def search_replace(my_list, search, replace):
    """
    replace all occurrences of the search element with the replace element
    """
    result = [elem for elem in my_list]
    for i in range(len(result)):
        if result[i] == search:
            result[i] = replace

    return result
