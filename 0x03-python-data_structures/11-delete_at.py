#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list[idx] is not None:
        del my_list[idx]
        return my_list
