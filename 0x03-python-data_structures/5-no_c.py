#!/usr/bin/python3
def no_c(my_string):
    newString = " "
    for char in my_string:
        if char is not 'c' and char is not 'C':
            newString = newString + char
        return newString
