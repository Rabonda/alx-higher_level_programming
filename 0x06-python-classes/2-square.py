#!/usr/bin/python3
"""Definition of a class, named Square"""


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    """ 
    def __init__(self, size=0):
        """Initializes the __size variable with the size value."""
        if size < 0:
            raise ValueError("size must be >= 0") 
        elif not isinstance(size, int):
            raise TypeError("size must be an integer") 
        self.__size = size
