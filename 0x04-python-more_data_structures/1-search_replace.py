#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for i in my_list:
        if i == search:
            i = replace
        n_list.append(i)
    return n_list
