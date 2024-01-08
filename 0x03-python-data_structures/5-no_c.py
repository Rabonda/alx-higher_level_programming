#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for num in my_string:
        if num is not 'c' and num is not 'C':
            newString = newString + num
    return newString
