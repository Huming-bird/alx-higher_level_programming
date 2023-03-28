#!/usr/bin/python3

class Square:
    """ This class, when called upon, instantiates a square object"""

    def __init__(self, size=0, position=(0, 0)):
        """ This instantiates a square object"""

        self.__size = size
        self.__position = position

    def area(self):
        """ This calculates the area of the square object"""

        area = self.__size ** 2
        return area

    @property
    def size(self):
        """ This sets the size attribute of the object"""

        return self.__size

    @property
    def position(self):
        """ This sets the position attrib of the object"""

        return self.__position

    @size.setter
    def size(self, value):
        """ This gives a value to the size attribute"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) == int and value > 0:
            self.__size = value

    @position.setter
    def position(self, value):
        """ This gives a value to the position attrib"""

        if type(position) != tuple or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        """ This prints the size of the square to stdout"""

        if self.__size == 0:
            print("")
        else:
            for a in range(self.__position[0]):
                print(" " * self.__position[0], end='')
                for i in range(self.__size):
                    print('#' * self.__size)
                    break
