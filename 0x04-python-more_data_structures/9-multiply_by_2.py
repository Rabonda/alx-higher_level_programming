#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_new = {}
    if a_dictionary:
        for lists in a_dictionary:
            dictionary_new[lists] = a_dictionary[lists] * 2
    return (dictionary_new)
