#!/usr/bin/python3
"""defines a name-printing function"""


def say_my_name(first_name, last_name=""):
    """print a name

    Args:
      first_name: the first name to print
      last_name: the last name to print
    Raises:
      a TypeError if either the first name or the last name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {first_name} {last_name}".format(first_name, last_name))
