#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    new_list = my_list.copy()
    for i in range(0, len(my_list) - 1):
        if my_list[i] == search:
            new_list[i] = replace
    return new_list
