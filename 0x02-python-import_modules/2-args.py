#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
            print("0 arguments.")
    else:
        if (len(sys.argv)) == 2:
                print(len(sys.argv) - 1, "argument:")
        else:
            print(len(sys.argv) - 1, "arguments:")

        for i, a in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, a))
