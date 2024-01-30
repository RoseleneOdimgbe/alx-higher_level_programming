#!/usr/bin/python3
"""
This contains a definition for the class rectangle
"""


class Rectangle:
    """Definition of the class rectangle
       Args:
           number_of_instances: the counter for objects in existence
           print_symbol(any): the symbol for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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

    def area(self):
        """Public instance method to compute the area of rectangle
           Returns: the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method to compute the perimeter of triangle
           Returns: the perimeter of triangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the string representation of a rectangle
        """
        rect = ''
        if self.__height == 0 or self.__width == 0:
            return ""
        for n in range(0, self.__height):
            rect += (str(self.print_symbol) * self.__width)
            if n != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """Returns the string representation of a rectangle
            This should be able to create a new instance using eval()
        """

        return '{self.__class__.__name__}({self.width}, {self.height})'.\
            format(self=self)

    def __del__(self):
        """Prints the string to STDOUT when rectangle object is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest triangle based on area
           or rect_1 if both are of the same size
        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectanlge): the second rectangle
        Raises:
            TypeError: if neither of the rect is of instance Rectangle Class
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
