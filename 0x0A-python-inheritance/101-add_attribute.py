#!/usr/bin/python3
"""define a function that adds attributes"""


def add_attribute(obj, att, value):
    """add a new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
