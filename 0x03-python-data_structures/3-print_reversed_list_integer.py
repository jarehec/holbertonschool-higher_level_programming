#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        my_list.sort(reverse=True)
        for item in (my_list):
            print("{:d}".format(item))
