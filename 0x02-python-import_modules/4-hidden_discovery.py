#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    n = dir()
    for i in range(0, len(n)):
        if n[i][:2] != "__":
            print("{:s}".format(n[i]))
