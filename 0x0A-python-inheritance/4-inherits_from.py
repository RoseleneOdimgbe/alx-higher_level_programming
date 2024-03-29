#!/usr/bin/python3
"""This defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """This checks if an object is an inherited instance of a class

    Args:
        obj (any): This is the object to check
        a_class (type): This is the class to match the type of obj to check
    Returns:
        if obj is an inherited instance of a_class - True
        otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
