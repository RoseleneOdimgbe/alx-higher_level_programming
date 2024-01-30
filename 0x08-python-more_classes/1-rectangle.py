#!/usr/bin/python3

"""
This contains the definition for a class rectangle
"""


class Rectangle:
    """The definition of class rectangle
       Attributes:
           width(int): this is the rectangle width
           height(int): this is the rectangle height
    """
    def __init__(self, width=0, height=0):
        """
            This initializes a new Class Rectangle instance
            Args:
                width(int): this is the rectangle width
                height(int): this is the rectangle height
            Raises:
                TypeError: if the width/height is not an int
                ValueError: if the width/ height is not >= 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
            The getter function for private attribute width
            Returns: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            The setter function for private attribute width
            Args:
                The value(int) new width value
            Raises:
                TypeError: if the value is not an int
                ValueError: if the value is not >= 0
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            The getter function for private attribute height
            Returns: The height of the triangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            The setter function for private attribute height
            Args:
                The value(int) new width value
            Raises:
                TypeError: if the value is not an int
                ValueError: if the value is not >= 0
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value
