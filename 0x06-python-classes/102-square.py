#!/usr/bin/python3

"""This defines a class square"""


class Square:
    """This represents a square"""

    def __init__(self, size=0):
        """This initializes a new square

        Args:
            size (int): This is the size of the new square
        """
        self.size = size

    @property
    def size(self):
        """This gets/sets the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This returns the current area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """This defines the == comparison to a square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """This defines the != comparison to a square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """This defines the < comparison to a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """This defines the <= comparison to a square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """This defines the > comparison to a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """This defines the >= comparison to a square"""
        return self.area() >= other.area()
