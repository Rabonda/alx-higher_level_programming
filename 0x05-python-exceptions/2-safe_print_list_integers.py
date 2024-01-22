#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    indx = 0
    coun = 0
    while indx < x:
        try:
            print("{:d}".format(my_list[coun]), end="")
            indx = indx + 1
        except (TypeError, ValueError):
            pass
        coun++;
    print()
    return indx
