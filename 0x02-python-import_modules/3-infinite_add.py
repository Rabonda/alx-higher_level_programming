#!/usr/bin/python3
def add():
    total = 0
    for indx in range(1, len(sys.argv)):
        total = total + int(sys.argv[indx])
    print(total)


if __name__ == "__main__":
    import sys
    add()
