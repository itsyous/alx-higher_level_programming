#!/usr/bin/python3
"""containing class"""


class Student:
    """represent a class"""
    def __init__(self, first_name, last_name, age):
        """initialize a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get a dictionary representation of the student

        If attrs is a list of strings,only attribute names
        contained in this list must be retrieved.

        Args:
          attrs (lis): the attributtes to represent
        """
        if (type(attrs) is list and
           all(type(i) is str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attributtes of the student

        Args:
         json (dict): the key/value pairs to replace attributes with
        """
         for j, i in json.items():
             setattr(self, j, i)
