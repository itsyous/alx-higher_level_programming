#!/usr/bin/python3
"""
contains class MyInt
"""


class MyInt(int):
    """rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """create an instance of class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is !="""
        return int(self) == other
