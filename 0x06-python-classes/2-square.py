#!/usr/bin/python3

class Square:
    """ This class, when called upon, instantiates a square object"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) == int and size > 0:
            self.__size = size

