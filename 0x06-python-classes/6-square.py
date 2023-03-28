#!/usr/bin/python3

class Square:
    """ This class, when called upon, instantiates a square object"""

    def __init__(self, size=0, position=(0, 0):
        self.__size = size
        self.__position = position

    def area(self):
        area = self.__size ** 2
        return area

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) == int and value > 0:
            self.__size = value

    
    @position.setter
    def position(self, value):
        if type(position) != tuple or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
        for a in range(position[0]):
            print(" " * position[0], end='')
            for i in range(self.__size):
                print('#' * self.__size)
