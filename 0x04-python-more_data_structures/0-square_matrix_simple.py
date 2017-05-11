#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nre = []
    for i in matrix:
        nre += ([[n**2 for n in i]])
    return nre
