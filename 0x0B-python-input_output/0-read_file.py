#!/usr/bin/python3
"""define read_file function"""


def read_file(filename=""):
    """read filename with uft-8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
