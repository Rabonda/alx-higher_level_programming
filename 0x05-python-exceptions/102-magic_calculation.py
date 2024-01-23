#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for indx in range(1, 3):
        try:
            if indx > a:
                raise Exception('Too far')
            r += a ** b / indx
        except:
            r = a + b
            break
    return r
