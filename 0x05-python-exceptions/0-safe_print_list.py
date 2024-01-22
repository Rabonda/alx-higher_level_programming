#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index = 0; index < x; index++:
            print("{:d}".format(my_list[index]), end="")
    except Exception as e:
        break
    print()
    return index
