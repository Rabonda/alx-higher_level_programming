#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_2 = []
    if my_list:
        list_2 = list(map(lambda l: l if l != search else replace, my_list))
    return list_2
