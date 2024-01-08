#!/usr/bin/python3
def divisible_by_2(my_list=[]):
  for x in my_list:
    if x % 2 == 0:
      list = True
    else:
      list = False
  return list
