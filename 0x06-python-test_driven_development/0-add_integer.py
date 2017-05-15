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
    if isinstance(a, float) is not True and isinstance(a, int) is not True:
        raise TypeError("a must be an integer")
    if isinstance(b, float) is not True and isinstance(b, int) is not True:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
