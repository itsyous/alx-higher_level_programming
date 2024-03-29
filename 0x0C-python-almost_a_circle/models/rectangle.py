#!/usr/bin/python3
"""create a class"""
from models.base import Base


class Rectangle(Base):
    """Represent a class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """display the rectangle"""
        for i in range(0, self.y):
            print("")

        for k in range(0, self.height):
            for x in range(0, self.x):
                print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        x = 0
        for arg in args:
            if x == 0:
                self.id = arg
            elif x == 1:
                self.width = arg
            elif x == 2:
                self.height = arg
            elif x == 3:
                self.x = arg
            elif x == 4:
                self.y = arg
            x += 1

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = height
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """return the dictionary representation"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)
