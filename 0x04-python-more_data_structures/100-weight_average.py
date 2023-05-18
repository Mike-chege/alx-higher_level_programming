#!/usr/bin/python3
# Task 13

def weight_average(my_list=[]):
    """
    calculate the weighted average of the list
    """
    if not my_list:
        return 0
    numerator = sum(score * weight for score, weight in my_list)
    denominator = sum(weight for score, weight in my_list)
    return numerator / denominator
