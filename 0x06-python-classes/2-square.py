#!/usr/bin/python3
"""The square module"""


class Square:
    """This defines a square"""

    def __init__(self, size=0):
        """Constructor
        Args:
            size: this is the length of side of the square
        Raises:
            TypeError: if the size is not an integer
            ValueError: If the size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size =
