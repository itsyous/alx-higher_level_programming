#!/usr/bin/python3
"""defines a function that prints 2 new lines
after each of these characters '.', '?' and ':'
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after
    of these characters '.', '?' and ':'

    Args:
      text (str): the input string to be examined

    Raises:
      TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join(
                [line.strip("") for line in text.split(delim)])

    print(text, end="")
