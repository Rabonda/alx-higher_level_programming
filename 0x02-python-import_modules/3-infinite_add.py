#!/usr/bin/python3
def total(args):
    tot = 0
    for lists in args[1:]:
        tot = tot + int(lists)
    print tot

if __name__ == "__main__":
    import sys
    total(sys.argv)
