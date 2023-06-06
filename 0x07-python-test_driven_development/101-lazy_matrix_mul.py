#!/usr/bin/python3
# Task 7 lazy matrix multiplication
"""A function that multiplies 2 matrices by using the module NumPy"""


from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """Returns the output of two multiplied matrices"""
    return matmul(m_a, m_b)
