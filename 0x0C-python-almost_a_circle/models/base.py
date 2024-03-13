#!/usr/bin/python3
"""create a class"""


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
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
