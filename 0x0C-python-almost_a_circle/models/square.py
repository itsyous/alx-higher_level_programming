#!/usr/bin/python3
"""define a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent a class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """represent a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y
                                                  self.width)
