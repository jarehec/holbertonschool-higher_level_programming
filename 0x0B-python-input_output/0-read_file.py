#!/usr/bin/python3
def read_file(filename=""):
    'Reads a text file and prints to stdout'
    with open(filename, 'r', encoding='utf-8') as fname:
        print(fname.read(), end='')
