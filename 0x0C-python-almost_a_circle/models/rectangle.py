#!/usr/bin/python3
"""create a class"""
from models.base import Base


class Rectangle(Base):
    """Represent a class"""


    def __init__(self, width, height, x=0, y=0, id=None):
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

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
