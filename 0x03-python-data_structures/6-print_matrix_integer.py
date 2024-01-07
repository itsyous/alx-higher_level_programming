#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for k in matrix:
            for l in k:
                print("{:d}".format(l), end=' ')
            print()
