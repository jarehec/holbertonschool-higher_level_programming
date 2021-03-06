#!/usr/bin/python3
class Rectangle:
    'Defining Rectangle class with width and height'
    def __init__(self, width=0, height=0):
        'Initializing data'
        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        'Method to retrieve width'
        return self.__width

    @width.setter
    def width(self, value):
        'Method to set width'
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        'Method to retrieve height'
        return self.__height

    @height.setter
    def height(self, value):
        'Method to set height'
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
