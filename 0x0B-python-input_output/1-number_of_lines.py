#!/usr/bin/python3
def number_of_lines(filename=""):
    'counts the number of lines in a text file'
    with open(filename, 'r') as fname:
        return len(fname.readlines())
