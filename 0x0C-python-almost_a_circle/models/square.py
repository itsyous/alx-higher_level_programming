#!/usr/bin/python3
"""define a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent a class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize a class"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.size

    @setter.size
    def size(self, value):
        self.size = value
        self.size = value

    def __str__(self):
        """represent a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

