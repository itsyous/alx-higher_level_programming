#!/usr/bin/python3
"""containing 'class_to_json' function"""


def class_to_json(obj):
    """return the dictionary description with data structure"""
    return obj.__dict__
