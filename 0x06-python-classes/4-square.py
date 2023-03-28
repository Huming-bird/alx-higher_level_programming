#!/usr/bin/python3

class Square:
    """ This class, when called upon, instantiates a square object"""

    def __init__(self, size=0):
        """ This instantiates a square object"""

        self.__size = size

    def area(self):
        """ This method calculates the area of a square object"""

        area = self.__size ** 2
        return area

    @property
    def size(self):
        """ This defines the square size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """ This sets the size of the square object"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) == int and value > 0:
            self.__size = value
