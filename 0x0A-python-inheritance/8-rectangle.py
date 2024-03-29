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
