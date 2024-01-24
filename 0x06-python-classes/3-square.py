#!/usr/bin/python3
class Square:
    """Definition of a class named Square"""

    def __init__(self, size=0):
        """initialization"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """area of a square method"""
        a = self.__size**2
        return a
