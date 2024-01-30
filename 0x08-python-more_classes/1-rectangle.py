#!/usr/bin/python3
"""
This contains a definition for the class rectangle
"""


class Rectangle:
    """Definition of the class rectangle
       Attributes:
           width(int): the rectangle width
           height(int): the rectangle height
    """
    def __init__(self, width=0, height=0):
        """
            This initializes a new Class Rectangle instance
            Args:
                width(int): the rectangle width
                height(int): the rectangle height
            Raises:
                TypeError: if the width/height is not int
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
            getter function for private attribute width
            Returns: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for private attribute width
            Args:
                value(int) new width value
            Raises:
                TypeError: if the value is not int
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
            getter function for private attribute height
            Returns: the height of the triangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for private attribute height
            Args:
                value(int) new width value
            Raises:
                TypeError: if the value is not int
                ValueError: if the value is not >= 0
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value
