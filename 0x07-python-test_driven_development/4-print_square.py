#!/usr/bin/python3
"""defines a function that print square"""


def print_square(size):
    """print a square with '#' character

    Args:
      size (int): the height/width of the square
    Raises:
      TypeError: if the size is not an integer
      ValueError: if the size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
