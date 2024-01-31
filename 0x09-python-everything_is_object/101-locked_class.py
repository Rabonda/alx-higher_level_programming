#!/usr/bin/python3
# 101-locked_class.py

"""Defines a class named lockedClass."""

class LockedClass:
    """
    The user is prohibited from creating new LockedClass
    attributes for any other attribute, except for 'first_name'.
    """

    __slots__ = ["first_name"]
