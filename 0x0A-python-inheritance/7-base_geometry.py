#!/usr/bin/python3
"""module for base geometry"""


class BaseGeometry:
    """represent a class"""
    def area(self):
        """compute area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method for validating value"""
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
