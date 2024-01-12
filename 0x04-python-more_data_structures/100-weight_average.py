#!/usr/bin/python3
def weight_average(my_list=[]):
    if !my_list:
        return 0
    ave = 0
    divide = 0
    for tup in my_list:
        ave += tup[0] * tup[1]
        divide += tup[1]
    return float(ave / divide)
