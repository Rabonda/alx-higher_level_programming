#!/usr/bin/python3
def no_c(my_string):
    newString = " "
    for cha in my_string:
        if cha is not 'c' and cha is not 'C':
            newString = newString + cha
        return newString
