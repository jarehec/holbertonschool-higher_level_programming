#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for lists in matrix:
            for i in lists:
                print("{:d}".format(i), end='')
                if i % len(lists) != 0:
                    print(' ', end='')
            print("")
