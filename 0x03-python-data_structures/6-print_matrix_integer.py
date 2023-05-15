#!/usr/bin/python3
# Task 6

def print_matrix_integer(matrix=[[]]):
    """
    prints the matrix of integers
    """
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="")
            else:
                print("{:d}".format(row[i]), end=" ")
        print()
