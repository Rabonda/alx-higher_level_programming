#!/usr/bin/python3
"""Definition of a class, named Square"""


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    """ 
    def __init__(self, size=0):
        """Initializes the __size variable with the size value."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise valueError("size must be >= 0")
        else:
            self.__size = size
