#!/usr/bin/python3

"""This defines a locked class"""


class LockedClass:
    """
    This prevents the user from instantiating new LockedClass attributes
    for anything other than attributes called 'first_name'
    """

    __slots__ = ["first_name"]
