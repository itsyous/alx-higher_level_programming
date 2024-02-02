#!/usr/bin/python3
"""Define an empty class rectangle"""


class Rectangle:
    """representation of a Rectangle"""

    def __init__(self, width=0, height=0):
        """initialize a rectangle"""

        self.height = height
        self.width = width

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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

