#!/usr/bin/python3
def print_last_digit(number):
    real_value = abs(number) % 10
    print(real_value, end="")
    return real_value
