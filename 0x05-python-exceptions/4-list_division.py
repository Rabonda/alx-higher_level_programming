#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotients = []
    iCount = 0
    while iCount < list_length:
        try:
            quotient = my_list_1[iCount] / my_list_2[iCount]
        except TypeError:
            quotient = 0
            print("wrong type")
        except IndexError:
            quotient = 0
            print("out of range")
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        finally:
            quotients.append(quotient)
        iCount += 1
    return quotients
