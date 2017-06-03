#!/usr/bin/python3
def append_write(filename="", text=""):
    'appends a string to the end of a text file'
    with open(filename, 'a') as fname:
        return fname.write(text)
