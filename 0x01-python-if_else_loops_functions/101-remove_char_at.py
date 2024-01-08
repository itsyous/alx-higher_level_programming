#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) - 1:
        return str
    else:
        str2 = str.replace(str[n], '')
    return str2
