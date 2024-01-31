#!/usr/bin/python3
"""define a class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialize a square

        Args:
        size: the lenght of a side of square
        """
        self.__size = size

    @property
    def size(self):
        """retrieve the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the squared size"""
        return (self.__size ** 2)
