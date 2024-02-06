#!/usr/bin/python3
"""define write_file"""


def write_file(filename="", text=""):
    """read filename"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
