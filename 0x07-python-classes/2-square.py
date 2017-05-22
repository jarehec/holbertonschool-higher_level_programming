#!/usr/bin/python3
class Square:
    'Square class with validated size'
    def __init__(self, size=0):
        'Initialize size'
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
