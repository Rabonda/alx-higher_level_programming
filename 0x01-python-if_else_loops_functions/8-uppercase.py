#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        char = ord(alpha)
        if ord(alpha) <= 96 or ord(alpha) >= 123:
          pass
        else:
          char = ord(alpha) - 32
        print("{:c}".format(char), end="")
    print()
