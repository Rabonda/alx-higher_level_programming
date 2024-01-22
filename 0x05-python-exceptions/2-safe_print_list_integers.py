#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    indx = 0
    iCount = 0
    while indx < x:
        try:
            print("{:d}".format(my_list[iCount]), end='')
            indx += 1
            iCount += 1
        except (TypeError, ValueError):
            pass
    print()
    return indx
