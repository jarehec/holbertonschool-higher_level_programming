#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    temp = []
    new_m = []
    list_len = len(matrix[0])
    for i_list in matrix:
        for i in i_list:
            if isinstance(i, float) is not True and isinstance(i, int) is not True:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if isinstance(div, float) is not float and isinstance(div, int) is not True:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            temp.append(round(i / div, 2))
        if list_len != len(temp):
            raise TypeError("Each row of the matrix must have the same size")
        new_m += [temp]
        temp = []
    return new_m
