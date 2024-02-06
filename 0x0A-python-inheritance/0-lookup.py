#!/usr/bin/python3
"""This defines an object attribute lookup function"""


def lookup(obj):
    """This returns a list of the object's available attributes"""
    return (dir(obj))
