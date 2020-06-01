#!/bin/bash/python3
"""
This is the "2-matrix_divided" module.
Module contain only one fuction provided:"Matrix_divided"
"""


def matrix_divided(matrix, div):
    """Return a list that contain all elm of matrix divided"""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ValueError("division by zero")
    for elm in matrix:
        if type(elm) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
        if len(elm) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for i in elm:
            if type(i) is not int and float:
                raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    return([list(map(lambda x: round(x/div, 2), row)) for row in matrix])
