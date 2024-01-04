#!/usr/bin/python3
i=122
while i >= 97:
    if i % 2 != 0:
        i = i - 32
        print(chr(i))
    else:
        print(chr(i))
    i = i - 1
