#!/usr/bin/python3
"""This defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """This checks if an object is an instance or inherited instance of a class

    Args:
        obj (any): This is the object to check
        a_class (type): This is the class to match the type of obj to check
    Returns:
        if obj is an instance or inherited instance of a_class - True
        otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
