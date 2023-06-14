#!/usr/bin/python3
# Task 12
"""Returns a list of lists of integers representing pascal's triangle n"""


def pascal_triangle(n):
    """
    Defining pascal's triangle of size n
    Return a list of lists of integers rep pascal's triangle
    """
    if n <= 0:
        return []

    pascal_t = [[1]]
    while len(pascal_t) != n:
        triangle = pascal_t[-1]
        lists = [1]
        for i in range(len(triangle) - 1):
            lists.append(triangle[i] + triangle[i + 1])
        lists.append(1)
        pascal_t.append(lists)
    return pascal_t
