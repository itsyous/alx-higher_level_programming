#!/usr/bin/python3
"""define a class"""


class LockedClass:
    """
    prevent user from instantiating new LockedClass
    attributtes
    """

    __slots__ = ["first_name"]
