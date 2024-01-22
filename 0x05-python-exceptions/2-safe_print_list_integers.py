#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    indx = 0
    for iCount in range(0, x):
        try:
            print("{:d}".format(my_list[iCount]), end='')
        except IndexError:
            raise
        except:
            pass
        else:
            indx += 1
    print()
    return indx
