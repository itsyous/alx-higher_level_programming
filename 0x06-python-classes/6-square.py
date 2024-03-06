#!/usr/bin/python3
"""define a class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a square

        Args:
        size: the size of a new square
        position: the position of the new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieve the position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise ValueError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(ele, int) and ele >= 0 for ele in value:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the squared size"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with '#'"""
        if self.__size == 0:
            print("")
            return

        for x in range(0, self.__position[1]):
            print("")

        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
