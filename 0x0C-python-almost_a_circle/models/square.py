#!/usr/bin/python3
"""define a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent a class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a class

        Args:
         size: the size of the square
         x: the x coordinate of the square
         y: the y coordinate of the square
         id (int): the id if the square
         """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}/{} - {}".format(self.id,
                                                  self.x, self.y
                                                  self.size)
