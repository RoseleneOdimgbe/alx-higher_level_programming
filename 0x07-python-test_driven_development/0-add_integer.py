#!/usr/bin/python3

"""This defines an integer addition function"""


def add_integer(a, b=98):
    """This returns the integer addition of a and b

    Float arguments are typecasted to ints before the addition is performed

    Raises:
        TypeError: if either a or b is a non-int and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
