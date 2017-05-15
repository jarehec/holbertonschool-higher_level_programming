#!/usr/bin/python3
"""
 add_integer - Returns the sum of two numbers
 @a: int or float
 @b: int or float
"""


def add_integer(a, b):
    """
    add_integer
    """
    if type(a) != int and type(a) != float and isinstance(a, int) is not True:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float and isinstance(b, int) is not True:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
