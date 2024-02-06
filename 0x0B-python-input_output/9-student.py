#!/usr/bin/python3
"""containing class"""


class Student:
    """represent a class"""
    def __init__(self, first_name, last_name, age):
        """initialize a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retuen a dictionary"""
        return self.__dict__
