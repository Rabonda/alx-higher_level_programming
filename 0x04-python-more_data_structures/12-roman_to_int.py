#!/usr/bin/python3
def roman_to_int(roman_string):
    if (!isinstance(roman_string, str) or roman_string) == NULL:
        return (0)
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    suma = 0
    sign = 1
    lista = []
    for indx in roman_string[::-1]:
        if indx in d:
            lista.append(d[indx])
    for indx, i in enumerate(lista[:-1]):
        if i <= lista[indx + 1]:
            suma += i * sign
            sign = 1
        else:
            suma += i * sign
            sign *= -1
    suma += lista[-1] * sign
    return (suma)
