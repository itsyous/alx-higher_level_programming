#!/usr/bin/python3
"""module for base geometry"""


class BaseGeometry:
    """represent a class"""
    def area(self):
        """compute area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method for validating value

        Args:
         name (str): the name of the value
         value (int): the value to be validated
         
        Raises:
         TypeError: if the value is not an integer
         ValueError: if the value is <= 0
         """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
