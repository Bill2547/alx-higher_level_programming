#!/usr/bin/python3
"""Define class square."""

class square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialise a new square.
        Args:
            size (int):the size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
