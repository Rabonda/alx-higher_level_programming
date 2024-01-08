#!/usr/bin/python3
def max_integer(my_list = []):
  list_size = len(my_list)
  if list_size == 0:
    return
  my_list.sort()
  return (my_list.pop())
