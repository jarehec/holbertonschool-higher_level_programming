#!/usr/bin/python3
class BaseGeometry:
    'parent class'
    def area(self):
        'returns the area'
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        'validates int type for value'
        if (value.__class__ is not int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    'class rectangle'
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
