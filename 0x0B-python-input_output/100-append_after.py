#!/usr/bin/python3
"""define a text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """insert text after each line containing a string

    Args:
    filename: name of a file
    search_string: the string to search
    new_string: the string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
