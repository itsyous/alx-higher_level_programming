#!/usr/bin/python3
for i in range(00, 100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{:02d}".format(i), end = ', ')
