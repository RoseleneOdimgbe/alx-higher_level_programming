#!/usr/bin/python3
"""The square module"""


class Square:
    """This defines a square"""

    def __str__(self):
        """The string representation constructor of this square"""
        self.my_print()

    def __init__(self, size=0, position=(0, 0)):
        """Constructor
        Args:
            size(int): this is the length of side of the square
            position(int tuple): the position of the square
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """The properties for the length of side of a square
        Raises:
            TypeError: if the size is not an integer
            ValueError: If the size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """The setter function for private attribute size
           Args:
                value: the size value to set to
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """The property for square position
        Raises:
            TypeError: If the value is not tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """The setter function for private attribute position
           Args:
                value: the position value to set to
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be tuple of 2 positive integers")

    def area(self):
        """The area of the square
        Returns:
            the size squared
        """
        return self.__size ** 2

    def my_print(self):
        """This prints square with char #"""
        if self.__size == 0:
            print()
        else:
            i, j = 0, 0
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * self.__position[0],
                                    "#" * self.__size))
