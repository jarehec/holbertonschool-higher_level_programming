#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        str_a = []
        for i in lists:
            str_a.append(str(i))
        print(" ".join(str_a))
