#!/usr/bin/python3
"""The square module"""


class Square:
    """This defines a square"""

    def __init__(self, size=0):
        """Constructor
        Args:
            size: this is the length of side of the square
        """
        self.__size = size

    @property
    def size(self):
        """The properties for the length of side of a square
        Raises:
            TypeError: if the size is not an integer
            ValueError: If the size < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square
        Returns:
            the size squared
        """
        return self.__size ** 2
