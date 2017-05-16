#!/usr/bin/python3
"""Module that prints text with two lines after '.', '?', ':'
"""


def text_indentation(text):
    """Function that prints text with two lines after '.', '?', ':'
        @text: text string
    """
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")
    c = 0
    while c < len(text):
        print("{:s}".format(text[c]), end='')
        if text[c] == '.' or text[c] == ':' or text[c] == '?':
            print("\n")
            if c + 1 < len(text):
                c += 1
        c += 1
