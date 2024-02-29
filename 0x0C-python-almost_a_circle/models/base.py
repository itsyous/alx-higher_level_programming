#!/usr/bin/python3
"""create a class"""


class Base:
    """Initialize a class"""
    Base.__nb_objects = 0
    def __init__(self, id=None):
        """constructor"""
        if self.id is not None:
            self.id = id
