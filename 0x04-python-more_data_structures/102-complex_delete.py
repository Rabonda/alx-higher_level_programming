#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for dic_key in list(a_dictionary):
        if a_dictionary[dic_key] == value:
            del a_dictionary[dic_key]
    return a_dictionary
