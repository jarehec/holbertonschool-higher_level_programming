#!/usr/bin/python3
class Square:
    'Square with area method'
    def __init__(self, size=0):
        'Initialize data'
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        'Method to square self.__size'
        return self.__size**2
