#!/usr/bin/python3
import random
rand_number = random.randint(-10, 10)
if rand_number < 0:
    print(rand_number, "is negative")
elif rand_number == 0:
    print(rand_number, "is zero")
else:
    print(rand_number, "is positive")
