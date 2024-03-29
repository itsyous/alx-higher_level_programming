#!/usr/bin/python3
"""create a class"""
import json


class Base:
    """Represent a class

    Private class attribute:
     __nb_objects: Number of instantiated Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a class

        Args:
         id (int): the id of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """convert from json string to dictionary"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)
