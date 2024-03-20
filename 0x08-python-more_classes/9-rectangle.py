#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle:
    """representation of a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a rectangle"""

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get the private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """represent the rectangle

        Represent rectangle with '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        return '\n'.join(str(self.print_symbol) * self.__width
                         for i in range(0, self.__height))

    def __repr__(self):
        """return a string of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """display message for deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """return a new Rectangle with width and height equal to size"""
        return Rectangle(size, size)
