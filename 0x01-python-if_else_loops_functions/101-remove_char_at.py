#!/usr/bin/python3
def remove_char_at(str, n):
    str_2 = ""
    if n >= 0 and n < len(str):
        for indx in range(n + 1):
            if n != indx:
                str_2 += str[indx]
        for indx in range(n + 1, len(str)):
            str_2 += str[indx]
        return str_2
    return str
