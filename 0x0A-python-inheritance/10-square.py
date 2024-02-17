#!/usr/bin/python3
"""module for Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a class"""

    def __init__(self, size):
        """initialize a class

        Args:
        size (int): the size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
