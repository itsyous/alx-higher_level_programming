#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    while i <= len(my_list) - 1:
        if i == (-1):
            break
        print("{:d}".format(my_list[i]))
        i = i - 1