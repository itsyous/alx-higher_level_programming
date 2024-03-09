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
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the square

        Args:
         1st argument represent id attribute
         2nd argument represent size attribute
         3rd argument represent x attribute
         4th argument represent y attribute
         """
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    self.id = arg
                elif x == 1:
                    self.size = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
                x += 1

    def __str__(self):
        """represent a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
