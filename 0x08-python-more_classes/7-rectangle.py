#!/usr/bin/python3
class Rectangle:
    'Defining Rectangle class with width, height, perimeter and area'
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        'Method to retrieve width'
        return self.__width

    @width.setter
    def width(self, value):
        'Method to set width'
        self.__width = value

    @property
    def height(self):
        'Method to retrieve height'
        return self.__height

    @height.setter
    def height(self, value):
        'Method to set height'
        self.__height = value

    def area(self):
        'Method for rectangle area'
        return self.__width * self.__height

    def perimeter(self):
        'Method for rectangle perimeter'
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*self.__width + 2*self.__height

    def __str__(self):
        s = str(self.print_symbol)
        'str that print will output'
        if self.__width == 0 or self.__height == 0:
            return ("")
        return (s*self.__width+'\n')*(self.__height-1)+s*self.__width

    def __repr__(self):
        'repr Method'
        if self.__width == 0 or self.__height == 0:
            return ("")
        return str("Rectangle({:d}, {:d})").format(self.__width, self.__height)

    def __del__(self):
        'del Method'
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
