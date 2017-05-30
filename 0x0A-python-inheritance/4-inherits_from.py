#!/usr/bin/python3
def inherits_from(obj, a_class):
    """determines if object is an instance of a
    class that inherited (directly or indirectly) from a_class"""
    return isinstance(obj, a_class) and obj.__class__ != a_class
