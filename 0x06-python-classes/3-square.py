#!/usr/bin/python3
"""define a class"""

class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialize a square

        Args:
        size: lenght of a side of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

        def area(self):
            """return a squared size"""
            return (self.__size ** 2)
