#!/usr/bin/python3
"""module for inherits_from"""


def inherits_from(obj, a_class):
    """determine if an object is a subclass"""
    return isinstance(obj, a_class) and type(obj) != a_class
