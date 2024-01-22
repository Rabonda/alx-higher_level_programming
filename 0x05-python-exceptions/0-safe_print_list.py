#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ind = 0

    try:
        for ; ind < x; ind++:
            print("{:d}".format(my_list[ind]), end="")
    except:
        pass
    print()
    return ind
