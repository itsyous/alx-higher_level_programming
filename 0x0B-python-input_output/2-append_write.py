#!/usr/bin/python3
"""define append_write"""


def append_write(filename="", text=""):
    """append filename"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
