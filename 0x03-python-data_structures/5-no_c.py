#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for cha in my_string:
        if cha != "c" and cha != "C":
            newString = newString + cha
    return newString
