#!/usr/bin/python3
"""create a class"""
from models.base import Base


class Rectangle(Base):
    """Represent a class"""


    def __init__(self, width, height, x=0, y=0, id=None)
        """Initialize a class

        Args:
         height: the height of the rectangle
         width: the width of the rectangle
         x (int): the x coordinate of the rectangle
         y (int): the y coordinate to the rectangle
         id (int): the id of the new Base
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super.__init__(id)
