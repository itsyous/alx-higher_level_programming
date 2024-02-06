#!/usr/bin/python3
"""module for my list class"""


class MyList(list):
    """represent my list class"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
