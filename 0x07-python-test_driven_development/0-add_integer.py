#!/usr/bin/python3
"""define a function  containing addition of integers"""


def add_integer(a, b=98):
    """Return addtition of a and b

    Raises:
       TypeErroe: if either a and b is non-integer and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
