#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = 0
    for i in range(1, len(argv)):
        n = n + int(argv[i])
    print("{}".format(n))
