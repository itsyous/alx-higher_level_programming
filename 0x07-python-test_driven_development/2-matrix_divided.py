#!/usr/bin/python3
"""defines a function that divide a matrix"""


def matrix_divided(matrix, div):
   """
   Args:
    matrix: the list of lists of integers or floats
    div: the number to be divided to

   Raises:
    TypeError: if a matrix contains a non-integers numbers
    TypeError: if each row contains different size of the matrix
    TypeError: if div is not a number
    ZeroDivisionError: if div is equal to 0
   Return:
    the new matrix containing the result of division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all((isinstance(i, list) for i in matrix or
            not all((isinstance(j, int) or isinstance(j, float))
                for j in [num for i in matrix for num in i])):
            raise TypeError("matrix must be a matrix (list of lists)
            of integers/floats")

    if not all(len(i) == len(matrix[0]) for i in matrix):
       raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
       raise TypeError("div must be a number")

    if div == 0:
       raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), i)) for i in matrix])
