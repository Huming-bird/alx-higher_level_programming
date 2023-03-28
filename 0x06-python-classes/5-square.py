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
        """ This defines the size attribute of the square object"""

        return self.__size

    @size.setter
    def size(self, value):
        """ This sets the size attribute of the square object"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) == int and value > 0:
            self.__size = value

    def my_print(self):
        """ This prints the square object to stdout"""

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print('#' * self.__size)
