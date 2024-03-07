#!/usr/bin/python3
"""module for Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent a class"""

    def __init__(self, width, height):
        """initialize a class

        Args:
        width: the width of the rectangle
        height: the height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return print() and str()"""
        return f"[Rectangle] {self.__width}/{self.__height}"
