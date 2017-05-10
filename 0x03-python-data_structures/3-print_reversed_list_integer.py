#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0 or my_list == None:
        my_list.reverse()
        for item in (my_list):
            print("{:d}".format(item))
