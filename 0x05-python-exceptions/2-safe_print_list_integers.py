#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    indx = 0
    i = 0
    while indx < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            i += 1
        except (TypeError, ValueError):
            pass
        else:
            indx = indx + 1
    print()
    return indx
