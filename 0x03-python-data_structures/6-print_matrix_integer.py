#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None or matrix != []:
        c = 1
        for lists in matrix:
            for i in lists:
                print("{:d}".format(i), end='')
                if c % len(lists) != 0:
                    c += 1
                    print(' ', end='')
                else:
                    c = 1
            print("")
