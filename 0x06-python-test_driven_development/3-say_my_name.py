#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if isinstance(first_name, str) is not True:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")
    print("My name is {:s}".format(first_name + ' ' + last_name))
