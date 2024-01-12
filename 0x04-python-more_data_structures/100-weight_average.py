#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        multiply = 0
        sum = 0
        for indx in my_list:
            multiply = indx + i[0] * indx[1]
            sum = sum + indx[1]
        return (multiply / sum)
    else:
        return (0)
