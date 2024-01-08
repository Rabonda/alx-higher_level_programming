#!/usr/bin/python3
import random
rand_number = random.randint(-10000, 10000)
if rand_number >= 0:
    last_digit = rand_number % 10
else:
    last_digit = rand_number % -10
print("Last digit of", rand_number, "is", last_digit, end=' ')
if last_digit < 6:
    print("and is less than 6 and not 0")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is greater than 5")
