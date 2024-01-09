#!/usr/bin/python3
for table in range(26, 0, -1):
    if table % 2 != 0:
        print("{:c}".format(table + 64), end="")
    else:
        print("{:c}".format(table + 96), end="")
