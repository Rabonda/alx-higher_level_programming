#!/usr/bin/python3
"""
Definition of a class, named Square
"""


class Square:
    """
    Initialization method
    """
    def __init__(self, size=0):
        """Creates new instances of square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2
